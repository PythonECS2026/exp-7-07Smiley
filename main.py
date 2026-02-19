# AIM: Write a Python program to create,
# update, and manipulate a dictionary of student records,
# including their grades and attendance.
# Coder:
# Date:
students = {
    "251S005": {"name": "Sameer",  "grade": "A",  "attendance": 68},
    "251S055": {"name": "Abdulla", "grade": "B",  "attendance": 88},
    "251S026": {"name": "Katrina", "grade": "A-", "attendance": 55}
}

# Add / overwrite student using del + add
uin = input().strip()
name = input().strip()
grade = input().strip()
attendance = int(input().strip())

# if student already exists, delete first
if uin in students:
    del students[uin]

# add student
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

print(f"Final Student Records: {students}")
# Write your code here
# TODO: Add a new Student Record 

# TODO: Update the Grade of Student of UIN 251P055

# TODO: Remove Student with UIN 251P026


# Stop coding here








