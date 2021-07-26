from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.indexes import GlobalSecondaryIndex, AllProjection
import os

class PhoneNumberIndex(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    """
    class Meta:
        index_name = 'phone_number'
        read_capacity_units = 1
        write_capacity_units = 1
        # All attributes are projected
        projection = AllProjection()

    phone_number = UnicodeAttribute(hash_key=True)

class EmailIndex(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    """
    class Meta:
        index_name = 'email'
        read_capacity_units = 1
        write_capacity_units = 1
        # All attributes are projected
        projection = AllProjection()

    email = UnicodeAttribute(hash_key=True)

class UsernameIndex(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    """
    class Meta:
        index_name = 'username'
        read_capacity_units = 1
        write_capacity_units = 1
        # All attributes are projected
        projection = AllProjection()

    username = UnicodeAttribute(hash_key=True)
    
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
        
    user_id = UnicodeAttribute(hash_key=True)    
    grab_points = NumberAttribute(range_key=True)
    
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

    user_id = UnicodeAttribute(hash_key=True)  
    robinhood_points = NumberAttribute(range_key=True)
    
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

    user_id = UnicodeAttribute(hash_key=True)  
    foodpanda_points = NumberAttribute(range_key=True)

class GrabIdIndex(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    """
    class Meta:
        index_name = 'grab_id'
        read_capacity_units = 1
        write_capacity_units = 1
        # All attributes are projected
        projection = AllProjection()

    grab_id = UnicodeAttribute(hash_key=True)
    
class RobinhoodIdIndex(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    """
    class Meta:
        index_name = 'robinhood_id'
        read_capacity_units = 1
        write_capacity_units = 1
        # All attributes are projected
        projection = AllProjection()

    robinhood_id = UnicodeAttribute(hash_key=True)
    
class FoodpandaIdIndex(GlobalSecondaryIndex):
    """
    This class represents a global secondary index
    """
    class Meta:
        index_name = 'foodpanda_id'
        read_capacity_units = 1
        write_capacity_units = 1
        # All attributes are projected
        projection = AllProjection()

    foodpanda_id = UnicodeAttribute(hash_key=True)
    
class PynamoBingsuUser(Model):
    ''' database to store user '''
    class Meta:
        table_name = os.environ.get('BINGSU_USER_TABLE_NAME')
        region = 'ap-southeast-1'
    user_id = UnicodeAttribute(hash_key = True)
    username = UnicodeAttribute()
    password = UnicodeAttribute()
    grab_points = NumberAttribute(null=True)
    robinhood_points = NumberAttribute(null=True)
    foodpanda_points = NumberAttribute(null=True)
    coins = NumberAttribute()
    email = UnicodeAttribute()
    phone_number = UnicodeAttribute()
    grab_id = UnicodeAttribute(null=True)
    robinhood_id = UnicodeAttribute(null=True)
    foodpanda_id = UnicodeAttribute(null=True)
    co2_amount = NumberAttribute()
    total_amount_tree = NumberAttribute()
    total_co2_offset_amount = NumberAttribute()
    
    username_index = UsernameIndex()
    grab_points_index = GrabPointsIndex()
    robinhood_points_index = RobinhoodPointsIndex()
    foodpanda_points_index = FoodpandaPointsIndex()
    grab_id_index = GrabIdIndex()
    robinhood_id_index = RobinhoodIdIndex()
    foodpanda_id_index = FoodpandaIdIndex()
    email_index = EmailIndex()
    phone_number_index = PhoneNumberIndex()
    
    def returnJson(self):
        return vars(self).get('attribute_values')
    

    