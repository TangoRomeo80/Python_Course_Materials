"""
This module contains all data manipulation functionalities
"""
from __future__ import annotations
from utils import prompt_non_empty, clean_name, prompt_int, prompt_float
# import utils
# from utils import *
from grading import compute_total_and_percentage, grade_from_percentage

def print_student_report(student: dict) -> None:
    print("\n" + "-" * 50)
    print(f"Student Id: {student['Id']}")
    print(f"Name: {student['Name']}")
    print(f"Subjects: {', '.join(student['Subjects'])}")
    print(f"Marks: {', '.join(str(m) for m in student['Marks'])}")
    print(f"Total: {student['Total']}")
    print(f"Percentage: {student['Percentage']:.2f}%")
    print(f"Grade: {student['Grade']}")
    print(f"Status: {student['Status']}")

def list_students(students: list[dict]) -> None:
    if not students:
        print("No students found.")
        return
    for student in students:
        print_student_report(student)

def add_student(students: list[dict]) -> None:
    sid = prompt_non_empty("Enter student Id: ")
    name = clean_name(prompt_non_empty("Enter student name: "))

    n = prompt_int("Enter number of subjects: ", min_val=1)

    subjects: list[str] = []
    marks: list[float] = []

    for i in range(n):
        sub = prompt_non_empty(f"Enter name of subject {i + 1}: ")
        sub = sub.strip().title()
        subjects.append(sub)

        mk = prompt_float(f"Enter marks for {sub}: ", min_val=0.0, max_val=100.0)
        marks.append(mk)

    # Compute
    total, pct = compute_total_and_percentage(marks)
    grade = grade_from_percentage(pct)
    status = "Pass" if grade != "F" else "Fail"

    student = {
        "Id": sid,
        "Name": name,
        "Subjects": subjects,
        "Marks": marks,
        "Total": total,
        "Percentage": pct,
        "Grade": grade,
        "Status": status
    }
    students.append(student)
    print_student_report(student)

def find_student_by_id(students: list[dict], sid: str) -> dict | None:
    for student in students:
        if student["Id"] == sid:
            return student
    return None

def search_student(students: list[dict]) -> None:
    sid = prompt_non_empty("Enter student Id to search: ")
    student = find_student_by_id(students, sid)
    if student is None:
        print(f"No student found with Id: {sid}")
    else:
        print_student_report(student)


