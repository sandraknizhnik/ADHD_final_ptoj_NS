# seed_data.py
#קובץ ש"זורע" נתוני התחלה (seed) – יוצר:
from mongo_test import db
from bson import ObjectId

# יצירת בית ספר
school_id = db.schools.insert_one({
    "name": "רמות חיפה"
}).inserted_id

# יצירת מורה
teacher_id = db.teachers.insert_one({
    "name": "מרינה כהן",
    "email": "marina@school.com",
    "school_id": school_id
}).inserted_id

# יצירת כיתה
class_id = db.classes.insert_one({
    "name": "ה'2",
    "school_id": school_id,
    "teacher_ids": [teacher_id]
}).inserted_id

# יצירת תלמיד
student_id = db.students.insert_one({
    "name": "איתי לוי",
    "class_id": class_id,
    "school_id": school_id,
    "progress": [],
    "recommendations": [],
    "tasks": []
}).inserted_id

# יצירת הורה
parent_id = db.parents.insert_one({
    "name": "אורלי לוי",
    "phone": "050-0000000",
    "email": "orly@example.com",
    "student_ids": [student_id] , # אם ההורה מקושר לכמה ילדים
    "school_ids": [school_id] , # שלומדים בכמה בתי ספר שונים  מקושר לכמה ילדים
    "tasks": []
}).inserted_id

def link_parent_to_student(parent_id: str, student_id: str):
    parent = db.parents.find_one({"_id": ObjectId(parent_id)})
    
    if parent is None:
        print(f"הורה עם ID {parent_id} לא נמצא")
        return

    current_students = parent.get("student_ids", [])

    if ObjectId(student_id) in current_students:
        print(f"התלמיד כבר מקושר להורה.")
        return

    db.parents.update_one(
        {"_id": ObjectId(parent_id)},
        {"$push": {"student_ids": ObjectId(student_id)}}
    )

    print(f"התלמיד נוסף בהצלחה להורה {parent.get('first_name', '')} {parent.get('last_name', '')}")

def add_or_link_parent(first_name: str, last_name: str, email: str, phone: str, student_id: str):
    # בדיקה אם ההורה כבר קיים לפי אימייל
    existing_parent = db.parents.find_one({"email": email})
    
    if existing_parent:
        parent_id = existing_parent["_id"]
        print(f"הורה קיים: {first_name} {last_name} (ID: {parent_id})")
    else:
        # יצירת הורה חדש
        parent_id = db.parents.insert_one({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "student_ids": []
        }).inserted_id
        print(f"הורה חדש {first_name} {last_name} נוסף (ID: {parent_id})")

    # קישור תלמיד להורה (אם עדיין לא מקושר)
    link_parent_to_student(parent_id, student_id)
    return parent_id


print("Seed data inserted successfully.")
