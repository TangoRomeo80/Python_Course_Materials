"""This module contains functionalities for data processing"""

from __future__ import annotations

# import utils
# from utils import *
# from hudai.utils import prompt_non_empty, format_name, prompt_int, prompt_float
from utils import prompt_non_empty, format_name, prompt_int, prompt_float
from grading import compute_total_and_percentage, grade_from_percentage, status_from_percentage

def print_student_report(student: dict) -> None:
    print("\n" + "-" * 50)
    print(f"Student: {student['Name']} (Id: {student['Id']})")
    print(f"Subjects: {', '.join(student['Subjects'])}")
    print(f"Marks: {', '.join(str(m) for m in student['Marks'])}")
    print(f"Total: {student['Total']:.2f}")
    print(f"Percentage: {student['Percentage']:.2f}%")
    print(f"Grade: {student['Grade']}")
    print(f"Status: {student['Status']}")
    print("-" * 50 + "\n")

def add_student(students: list[dict]) -> None:
    sid = prompt_non_empty("Enter student Id: ")
    name = format_name(prompt_non_empty("Enter student name: "))

    n = prompt_int("Enter number of subjects: ", min_value=1)

    subjects: list[str] = []
    marks: list[float] = []

    for i in range(n):
        sub = prompt_non_empty(f"Enter name of subject {i+1}: ")
        sub = sub.strip().title()
        subjects.append(sub)

        mk = prompt_float(f"Enter marks for {sub}: ", min_value=0.0, max_value=100.0)
        marks.append(mk)

    #Computation
    total, pct = compute_total_and_percentage(marks)
    grade = grade_from_percentage(pct)
    status = status_from_percentage(pct)

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
