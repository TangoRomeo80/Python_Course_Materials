"""
This module contains the function to export student results to a CSV file. It uses the csv module from the Python standard library to write the student data to a file in CSV format. The function takes a list of student dictionaries and a filename as input and writes the student data to the specified CSV file. Each student dictionary should contain keys such as 'Id', 'Name', 'Total Marks', 'Grade', and 'Status' for the export to work correctly.
"""
from __future__ import annotations
from csv import DictWriter

def export_to_csv(students: list[dict], filename: str) -> None:
    fields = ['Id', 'Name', 'Subjects', 'Marks', 'Total', 'Percentage', 'Grade', 'Status']

    with open(filename, mode='w', newline='') as f:
        writer = DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for student in students:
            row = student.copy()
            row['Subjects'] = ', '.join(student['Subjects'])
            row['Marks'] = ', '.join(str(m) for m in student['Marks'])
            writer.writerow(row)

    print(f"Student results have been exported to {filename}")
    
