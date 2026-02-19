# AIM: Write a Python program to create,
# update, and manipulate a dictionary of student records,
# including their grades and attendance.
# Coder:
# Date:
students = {
    "251P005": {"name": "Sameer", "grade": "A", "attendance": 68},
    "251P055": {"name": "Abdulla", "grade": "B+", "attendance": 88},
    "251P026": {"name": "Katrina", "grade": "A-", "attendance": 55}
}

# add new student
uin = input()
name = input()
grade = input()
attendance = int(input())

students[uin] = {
    "name": name,
    "grade": grade,
    "attendance": attendance
}

# update grade
update_uin = input()
new_grade = input()
if update_uin in students:
    students[update_uin]["grade"] = new_grade

# delete student
delete_uin = input()
if delete_uin in students:
    del students[delete_uin]

print(f"Final Student Records: {students}")

# Write your code here
# TODO: Add a new Student Record 

# TODO: Update the Grade of Student of UIN 251P055

# TODO: Remove Student with UIN 251P026


# Stop coding here




