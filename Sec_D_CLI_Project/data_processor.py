"""
This module contains functionalities for data processing
"""
from __future__ import annotations

from utils import prompt_non_empty, clean_name, prompt_int, prompt_float
from grading import compute_total_and_percentage, grade_from_percentage
# import utils
# from utils import *

def print_student_report(student: dict) -> None:
    print("\n" + "-" * 50)
    print(f"Student: {student['Name']} | Id: {student['Id']}")
    print(f"Subjects: {', '.join(student['Subjects'])}")
    print(f"Marks: {', '.join(str(m) for m in student['Marks'])}")
    print(f"Total: {student['Total']:.2f}")
    print(f"Percentage: {student['Percentage']:.2f}%")
    print(f"Grade: {student['Grade']}")
    print(f"Status: {student['Status']}")
    print("-" * 50 + "\n")

def list_students(students: list[dict]) -> None:
    if len(students) == 0:
        print("No students added yet.")
        return

def add_students(students: list[dict]) -> None:
    sid = prompt_non_empty("Enter student Id: ")
    name = clean_name(prompt_non_empty("Enter student name: "))
    n = prompt_int("Enter number of subjects: ", min_val=1, max_val=10)

    subjects: list[str] = []
    marks: list[float] = []

    for i in range(n):
        sub = prompt_non_empty(f"Enter name of subject {i + 1}: ")
        sub = sub.strip().title()
        subjects.append(sub)

        mk = prompt_float(f"Enter marks for {sub}: ", min_val=0.0, max_val=100.0)
        marks.append(mk)

    # compute
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