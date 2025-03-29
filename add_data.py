from pymongo import MongoClient
from bson import ObjectId
#הקובץ שבו נמצאות הפונקציות הכלליות שמאפשרות לך להוסיף עוד

# 🔗 הכניסי כאן את כתובת ה־URI שלך ממונגו אטלס (שימי לב להחליף שם משתמש, סיסמה ו-cluster name)
uri = "mongodb+srv://brainbridgens:BrainBridge25!@brainbridge0.oanx3ni.mongodb.net/?retryWrites=true&w=majority&appName=BrainBridge0"
client = MongoClient(uri)
db = client["ADHD_app"]

def add_class(school_id: str, class_name: str):
    class_id = db.classes.insert_one({
        "name": class_name,
        "school_id": ObjectId(school_id)
    }).inserted_id
    print(f"כיתה '{class_name}' נוספה לבית הספר (ID: {class_id})")
    return class_id

def add_student(first_name: str, last_name: str, class_id: str, parent_ids=None):
    if parent_ids is None:
        parent_ids = []
    student_id = db.students.insert_one({
        "first_name": first_name,
        "last_name": last_name,
        "class_id": ObjectId(class_id),
        "parent_ids": [ObjectId(p) for p in parent_ids]
    }).inserted_id
    print(f"תלמיד {first_name} {last_name} נוסף (ID: {student_id})")
    return student_id

def add_parent(first_name: str, last_name: str, email: str, phone: str):
    parent_id = db.parents.insert_one({
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone
    }).inserted_id
    print(f"הורה {first_name} {last_name} נוסף (ID: {parent_id})")
    return parent_id

def add_teacher(first_name: str, last_name: str, school_id: str, class_ids=None, email=""):
    if class_ids is None:
        class_ids = []
    teacher_id = db.teachers.insert_one({
        "first_name": first_name,
        "last_name": last_name,
        "school_id": ObjectId(school_id),
        "class_ids": [ObjectId(c) for c in class_ids],
        "email": email
    }).inserted_id
    print(f"מורה {first_name} {last_name} נוסף (ID: {teacher_id})")
    return teacher_id


