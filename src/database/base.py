import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config import db_config


client = MongoClient(
    db_config.DATABASE_URL, serverSelectionTimeoutMS=5000, server_api=ServerApi('1'))

try:
    conn = client.server_info()
    print(f'Connected to MongoDB {conn.get("version")}')
except Exception:
    print("Unable to connect to the MongoDB server.")

Mongo_database = client[db_config.MONGO_INITDB_DATABASE]


Captured_data_raw = Mongo_database.captured_data_raw
Captured_data_raw.create_index([("id", pymongo.ASCENDING)], unique=True)


# Raw_data = Mongo_database.raw_data
# Raw_data.create_index([("id", pymongo.ASCENDING)], unique=True)

# Train_data = Mongo_database.train_data
# Train_data.create_index([("id", pymongo.ASCENDING)], unique=True)

# Train_result = Mongo_database.train_result
# Train_result.create_index([("id", pymongo.ASCENDING)], unique=True)
