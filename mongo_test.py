#בודק אם את מצליחה להתחבר ל־MongoDB ומדפיס את כל בסיסי הנתונים במערכת .

from pymongo import MongoClient

# מחרוזת החיבור שלך
uri = "mongodb+srv://brainbridgens:BrainBridge25!@brainbridge0.oanx3ni.mongodb.net/?retryWrites=true&w=majority&appName=BrainBridge0"

# יצירת לקוח
client = MongoClient(uri)
db = client["ADHD_app"]

# הדפסת שמות הדאטהבייסים
print("📂 Databases in your cluster:")
for db_name in client.list_database_names():
    print(f"  - {db_name}")

