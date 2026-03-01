"""
This module will contain all the functionalities related to exporting to csv.
"""
from __future__ import annotations
import csv

def export_to_csv(students: list[dict], filename: str) -> None:
    fields = ["id", "name", "subjects", "marks", "total", "percentage", "grade", "status"]
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for student in students:
            row = student.copy()
            row["subjects"] = ";".join(student["subjects"])
            row["marks"] = ";".join(str(m) for m in student["marks"])
            writer.writerow(row)

    print(f"Exported {len(students)} students to {filename}.")
