from pymongo import MongoClient

uri = "mongodb+srv://brainbridgens:BrainBridge25!@brainbridge0.oanx3ni.mongodb.net/?retryWrites=true&w=majority&appName=BrainBridge0"
client = MongoClient(uri)

# Example - access your database and collection
db = client["ADHD_app"]
students = db["students"]

# Test insert
students.insert_one({
    "name": "Demo Student",
    "attention_score": 7,
    "notes": "First test insert from ADHD project"
})

