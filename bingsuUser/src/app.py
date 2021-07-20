import json
from .bingsuUser import PynamoBingsuUser

def lambda_handler(event, context):
    return {'data': 'Hello World'}

def add_user(event, context):
    item = event['arguments']
    user_id = item['user_id']
    username = item['username']
    password = item['password']
    grab_points = item.get('grab_points', None)
    robinhood_points = item.get('robinhood_points', None)
    foodpanda_points = item.get('foodpanda_points', None)
    coins = item['coins']
    email = item['email']
    phone_number = item['phone_number']
    grab_id = item.get('grab_id', None)
    robinhood_id = item.get('robinhood_id', None)
    foodpanda_id = item.get('foodpanda_id', None)
    co2_amount = item['co2_amount']
    
    
    user_item = PynamoBingsuUser(
        user_id = user_id,
        username = username,
        password = password,
        grab_points = grab_points,
        robinhood_points = robinhood_points,
        foodpanda_points = foodpanda_points,
        coins = coins,
        email = email,
        phone_number = phone_number,
        grab_id = grab_id,
        robinhood_id = robinhood_id,
        foodpanda_id = foodpanda_id,
        co2_amount = co2_amount
    )
    user_item.save()
    return {'data': 'Hello World'}

def update_user(event, context):
    
    
    return {'data': 'Hello World'}

