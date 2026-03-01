"""
This mpodule contains functionalities for exporting to csv file
"""
from __future__ import annotations
from csv import DictWriter

def export_to_csv(students: list[dict], filename: str) -> None:
    fields = ["Id", "Name", "Subjects", "Marks", "Total", "Percentage", "Grade", "Status"]

    with open(filename, "w", newline="") as f:
        writer = DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for student in students:
            row = student.copy()
            row["Subjects"] = ";".join(student["Subjects"])
            row["Marks"] = ";".join(str(m) for m in student["Marks"])
            writer.writerow(row)

    print(f"Exported {len(students)} students to {filename}.")