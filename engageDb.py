import pymongo


# Database
client = pymongo.MongoClient('localhost', 27017)
db = client['user_file_db']
collection = db['user_file_objects']
dict = {"key": "value"}
collection.insert_one(dict)