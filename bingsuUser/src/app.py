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
    user_uuid = str(uuid4())
    user_item = PynamoBingsuUser(
        user_id = user_uuid,
        username = item['username'],
        password = item['password'],
        grab_points = 0,
        robinhood_points = 0,
        foodpanda_points = 0,
        coins = item['coins'],
        email = item['email'],
        phone_number = item['phone_number'],
        grab_id = item.get('grab_id', None),
        robinhood_id = item.get('robinhood_id', None),
        foodpanda_id = item.get('foodpanda_id', None),
        co2_amount = item['co2_amount'],
        total_amount_tree = 0,
        total_co2_offset_amount = 0
    )
    user_item.save()
    return {'status': 200, 'user_id': user_uuid}

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
    
    tier_dict = {'diamond': 4000,
                'platinum': 3750,
                'gold': 3500,
                'silver': 3000,
                'bronze': 2000,
                'unranked':0}

    company_name = {'grab':'', 'foodpanda':'', 'robinhood':''} # empty string will return tier
    for name in company_name:
        temp = lst[0][name + '_points']
        for tier in tier_dict:
            if temp >= tier_dict[tier]:
                print(name, tier)
                company_name[name] = tier
                break
            

    return {'status': 200,
            'data': lst,
            'tier': company_name}
    
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
        co2_amount = current_dict['co2_amount'],
        total_amount_tree = current_dict['total_amount_tree'],
        total_co2_offset_amount = current_dict['total_co2_offset_amount']
    )
    user_item.save()
    return {'status': 200}

def get_all_by_ranking(event, context):
    from pandas import DataFrame
    top_100 = event['arguments']['top_100']
    company = str(event['arguments']['company']).lower()
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ.get('BINGSU_USER_TABLE_NAME'))

    # response = table.query(IndexName='robinhood_points', KeyConditionExpression=Key('robinhood_points').lt(500), ScanIndexForward=False)
    
    response = table.scan()
    df = DataFrame(response['Items'])
    df = df.sort_values(by=company + '_points', ascending=False).reset_index(inplace=False)
    df['index'] = df.index
    if top_100:
        df_rank = df.head(100)
    else:
        user_position = df.index[df['user_id'] == event['arguments']['user_id']].tolist()[0]
        if user_position < 50:
            user_lower = 0
        else:
            user_lower = user_position - 50

        df_rank = df[user_lower:user_position + 50]

    response_rank = df_rank.to_json(orient = 'records')
    response_rank_json = json.loads(response_rank)

    return {'status': 200, 'data': response_rank_json}

def authorise_user(event, context):
    item = event['arguments']
    email_or_phone = item['email_or_phone']
    password = item['password']
    if '@' in email_or_phone:
        iterator = PynamoBingsuUser.email_index.query(email_or_phone)
    else:
        iterator = PynamoBingsuUser.phone_number_index.query(email_or_phone)
    iterator_list = list(iterator)
    lst = []
    if len(iterator_list) > 0:
        for i in iterator_list:
            lst.append(i.returnJson())
    else:
        return {'status': 400}
    if password == lst[0]['password']:
        return {'status': 200,
                'user_id': lst[0]['user_id']}
    return {'status': 400}

def get_user_count(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(os.environ.get('BINGSU_USER_TABLE_NAME'))
    
    response = table.scan()
    user_number = len(response['Items'])
    return {'status': 200, 'user_number': user_number}