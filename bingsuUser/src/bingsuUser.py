from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, JSONAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
import os

class PynamoBingsuUser(Model):
    ''' database to store group '''
    class Meta:
        table_name = os.environ.get('BINGSU_USER_TABLE_NAME')
        region = 'ap-southeast-1'
    userId = UnicodeAttribute(hash_key = True)
    username = UnicodeAttribute()
    password = UnicodeAttribute()
    points = NumberAttribute()
    coins = NumberAttribute()
    email = UnicodeAttribute()
    