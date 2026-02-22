"""
This module contains functionalities related to student list manipulation.
"""

from __future__ import annotations
from utils import prompt_non_empty, prompt_float, prompt_int, clean_name
from grading import compute_total_and_percentage, grade_from_percentage, status_from_percentage
# import utils
# from utils import *

def print_student_report(student: dict) -> None:
    print("\n" + "-" * 50)
    print(f"Student: {student['name']} | ID: {student['id']}")
    print(f"Subjects: {', '.join(student['subjects'])}")
    print(f"Marks: {', '.join(str(m) for m in student['marks'])}")
    print(f"Total: {student['total']:2f}")
    print(f"Percentage: {student['percentage']:.2f}%")
    print(f"Grade: {student['grade']}")
    print(f"Status: {student['status']}")
    print("-" * 50 + "\n")
    
def list_students(students: list[dict]) -> None:
    if len(students) == 0:
        print("No students to display.")
        return
    print("\n=== All Student (Summary) ===")
    # for student in students:
    # for i in range(0, len(students)):
    #     student = students[i]
    #     print(f"{i + 1}. {student['id']} | {student['name']} | {student['percentage']:.2f}% | {student['grade']} | {student['status']}")
    #     print()
    for idx, student in enumerate(students, start=1):
        print(f"{idx}. {student['id']} | {student['name']} | {student['percentage']:.2f}% | {student['grade']} | {student['status']}")
        print()

def add_students(students: list[dict]) -> None:
    # Collect student infor from user and compute results
    sid =  prompt_non_empty("Enter Student Id: ")
    # raw_name = prompt_non_empty("Enter Student Name: ")
    # name = clean_name(raw_name)
    name = clean_name(prompt_non_empty("Enter Student Name: "))
    n = prompt_int("Enter number of subjects: ", min_val=1, max_val=10)
    subjects: list[str] = []
    marks: list[float] = []

    # We write a for loop to collect subjects + marks
    for i in range(0, n):
        sub = prompt_non_empty(f"Subject {i + 1} name: ")
        subject = sub.strip().title()
        subjects.append(subject)

        mark = prompt_float(f"Enter marks for {subject}: ", min_val=0.0, max_val=100.0)
        marks.append(mark)

    # Compute
    total, pct = compute_total_and_percentage(marks)
    grade = grade_from_percentage(pct)
    status = status_from_percentage(pct)

    student = {
        "id": sid,
        "name": name,
        "subjects": subjects,
        "marks": marks,
        "total": total,
        "percentage": pct,
        "grade": grade,
        "status": status
    }
    students.append(student)
    print_student_report(student)