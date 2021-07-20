from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
import os

class PynamoBingsuUser(Model):
    ''' database to store user '''
    class Meta:
        table_name = os.environ.get('BINGSU_USER_TABLE_NAME')
        region = 'ap-southeast-1'
    user_id = UnicodeAttribute(hash_key = True)
    username = UnicodeAttribute()
    password = UnicodeAttribute()
    grab_points = NumberAttribute()
    robinhood_points = NumberAttribute()
    foodpanda_points = NumberAttribute()
    coins = NumberAttribute()
    email = UnicodeAttribute()
    phone_number = UnicodeAttribute()
    grab_id = UnicodeAttribute(null=True)
    robinhood_id = UnicodeAttribute(null=True)
    foodpanda_id = UnicodeAttribute(null=True)
    co2_amount = NumberAttribute()
    
class GrabPointsIndex(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    """
    class Meta:
        index_name = 'grab_points'
        read_capacity_units = 1
        write_capacity_units = 1
        # All attributes are projected
        projection = AllProjection()

    grab_points = NumberAttribute(hash_key=True)
    
class RobinhoodPointsIndex(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    """
    class Meta:
        index_name = 'robinhood_points'
        read_capacity_units = 1
        write_capacity_units = 1
        # All attributes are projected
        projection = AllProjection()

    robinhood_points = NumberAttribute(hash_key=True)
    
class FoodpandaPointsIndex(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    """
    class Meta:
        index_name = 'foodpanda_points'
        read_capacity_units = 1
        write_capacity_units = 1
        # All attributes are projected
        projection = AllProjection()

    foodpanda_points = NumberAttribute(hash_key=True)
    