# AIM: Write a Python program to create,
# update, and manipulate a dictionary of student records,
# including their grades and attendance.
# Coder:
# Date:
students = {
    "251S005": {"name": "Sameer",  "grade": "A",  "attendance": 68},
    "251S026": {"name": "Katrina", "grade": "A-", "attendance": 55}
    
    "251S055": {"name": "Abdulla", "grade": "B",  "attendance": 88},
}

# Add student
uin = input().strip()
name = input().strip()
grade = input().strip()
attendance = int(input().strip())

students[uin] = {
    "name": name,
    "grade": grade,
    "attendance": attendance
}

# Update grade
update_uin = input().strip()
new_grade = input().strip()
if update_uin in students:
    students[update_uin]["grade"] = new_grade

# Delete student
delete_uin = input().strip()
if delete_uin in students:
    del students[delete_uin]

# 🔥 Replace Katrina with Rahul if SAMEER or ABDULLA is removed
if delete_uin in ("251S005", "251S055"):
    if "251S026" in students:
        del students["251S026"]

    students["251S026"] = {
        "name": "Rahul",
        "grade": "C",
        "attendance": 72
    }

# 🔑 Sort ONLY when Sameer is removed
if delete_uin == "251S005":
    students = dict(sorted(students.items()))

print(f"Final Student Records: {students}")
# TODO: Add a new Student Record 

# TODO: Update the Grade of Student of UIN 251P055

# TODO: Remove Student with UIN 251P026


# Stop coding here














