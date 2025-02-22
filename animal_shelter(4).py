from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, host, port, database, collection):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = '1214lg'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32583
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            # inserts data into dictonary
            insert = self.database.animals.insert_one(data)  # data should be dictionary 
            # checks if data was properly inserted
            if insert.acknowledge == False:
                return False
            else:
                return True
        # throws exception if nothing was inputted into paramter fields
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
            
# Create method to implement the R in CRUD.
    def read(self, query):
        # finds matching queries
        data = self.database.animals.find(query)
        # returns data in a list form
        return data
    
    
 # Method to implement U in CRUD
    def update(self, query, updated):
        # checks if there is a matching query
        if query is not None:
            # takes the query and updates it with the 'updated' value
            data = self.database.animals.update_many(query, {'$set': updated})
            # returns how many documents were modified
            print({data.modified_count}, " document(s) modified")
            
# Method to implement D in CRUD 
    def delete(self, query):
        # checks if there is a matching query
        if query is not None:
            # deletes the query
            data = self.database.animals.delete_many(query)
            # returns how many documents were deleted
            print({data.deleted_count}, " document(s) deleted")