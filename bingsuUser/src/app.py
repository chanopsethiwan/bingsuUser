import json
from .bingsuUser import PynamoBingsuUser
import boto3
from boto3.dynamodb.conditions import Key
import os
from uuid import uuid4

def lambda_handler(event, context):
    return {'data': 'Hello World'}

def add_user(event, context):
    item = event['arguments']
    username_iterator = PynamoBingsuUser.username_index.query(item['username'])
    username_list = list(username_iterator)
    if len(username_list) > 0:
        return {'status': 400}
    user_item = PynamoBingsuUser(
        user_id = str(uuid4()),
        username = item['username'],
        password = item['password'],
        grab_points = item.get('grab_points', None),
        robinhood_points = item.get('robinhood_points', None),
        foodpanda_points = item.get('foodpanda_points', None),
        coins = item['coins'],
        email = item['email'],
        phone_number = item['phone_number'],
        grab_id = item.get('grab_id', None),
        robinhood_id = item.get('robinhood_id', None),
        foodpanda_id = item.get('foodpanda_id', None),
        co2_amount = item['co2_amount']
    )
    user_item.save()
    return {'status': 200}

def get_user_by_id(event, context):
    item = event['arguments']
    user_id = item['user_id']
    iterator = PynamoBingsuUser.query(user_id)
    user_list = list(iterator)
    lst = []
    if len(user_list) > 0:
        for user in user_list:
            lst.append(user.returnJson())
    else:
        return {'status': 400}
    return {'status': 200,
            'data': lst}
    
def update_user(event, context):
    item = event['arguments']
    username = item.get('username', None)
    if username:
        username_iterator = PynamoBingsuUser.username_index.query(username)
        username_list = list(username_iterator)
        if len(username_list) > 0:
            return {'status': 400}
    user_id = item['user_id']
    iterator = PynamoBingsuUser.query(user_id)
    user_list = list(iterator)
    lst = []
    if len(user_list) > 0:
        for user in user_list:
            lst.append(user.returnJson())
    else:
        return {'status': 400}
    current_dict = lst[0]
    for i in item:
        current_dict[i] = item[i]
    
    user_item = PynamoBingsuUser(
        user_id = current_dict['user_id'],
        username = current_dict['username'],
        password = current_dict['password'],
        grab_points = current_dict.get('grab_points', None),
        robinhood_points = current_dict.get('robinhood_points', None),
        foodpanda_points = current_dict.get('foodpanda_points', None),
        coins = current_dict['coins'],
        email = current_dict['email'],
        phone_number = current_dict['phone_number'],
        grab_id = current_dict.get('grab_id', None),
        robinhood_id = current_dict.get('robinhood_id', None),
        foodpanda_id = current_dict.get('foodpanda_id', None),
        co2_amount = current_dict['co2_amount']
    )
    user_item.save()
    return {'status': 200}

