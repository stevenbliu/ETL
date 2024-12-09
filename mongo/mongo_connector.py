from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://root:example@localhost:27017/admin")

# Select the database and collection
db = client.mydatabase
collection = db.users

# Insert a document
document = {"name": "Dave2", "age": 35}
result = collection.insert_one(document)

print(f"Inserted document with _id: {result.inserted_id}")
