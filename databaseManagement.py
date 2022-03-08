import pymongo


# Database
client = pymongo.MongoClient('localhost', 27017)
db = client['user_file_db']
collection = db['user_file_objects']

#file repo
repo = 'text_files_repo'