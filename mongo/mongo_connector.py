from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://admin:adminpassword@localhost:27017')

# Select the database and collection
db = client.mydatabase
collection = db.users

# Insert a document
document = {"name": "Dave", "age": 35}
result = collection.insert_one(document)

print(f"Inserted document with _id: {result.inserted_id}")
