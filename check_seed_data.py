from pymongo import MongoClient
#בודק מה באמת נשמר בבסיס הנתונים – מדפיס את כל בתי הספר, הכיתות, התלמידים והמורים.
# התחברות למסד הנתונים
uri = "mongodb+srv://brainbridgens:BrainBridge25!@brainbridge0.oanx3ni.mongodb.net/?retryWrites=true&w=majority&appName=BrainBridge0"
client = MongoClient(uri)
db = client["ADHD_app"]

# בדיקת בתי ספר
print("🏫 Schools:")
for school in db.schools.find():
    print(f"- {school['name']} (ID: {school['_id']})")

# בדיקת כיתות
print("\n📚 Classes:")
for cls in db.classes.find():
    print(f"- {cls['name']} | School ID: {cls['school_id']}")

# בדיקת תלמידים
print("\n👧👦 Students:")
for student in db.students.find():
    print(f"- {student.get('first_name', '---')} {student.get('last_name', '---')} | Class ID: {student.get('class_id', '---')}")

# בדיקת מורים
print("\n👩‍🏫 Teachers:")
for teacher in db.teachers.find():
    print(f"- {teacher.get('first_name', '---')} {teacher.get('last_name', '---')} | School ID: {teacher.get('school_id', '---')}")
