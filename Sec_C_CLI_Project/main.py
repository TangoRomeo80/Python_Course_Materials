"""
Docstring for students_results_cli
This is an application for calculatingand storing student results.
This will run in the CLI.
If possible we will also save it in a .csv file.
"""

from __future__ import annotations

from data_processor import add_student, list_students, search_student, delete_student
from utils import prompt_non_empty
from export_csv import export_to_csv

def print_menu() -> None:
    print("---------- Student Result Calculator ----------")
    print("1) Add student result + calculate results")
    print("2) List all student results")
    print("3) Search student by Id")
    print("4) Delete student by Id")
    print("5) Save results to .csv file")
    print("6) Exit")

def print_export_menu(students: list[dict]) -> None:
    if not students:
        print("No student results available to export.")
        return
    filename = prompt_non_empty("Enter filename to export (without extension): ")
    filename = filename.strip() + ".csv"
    export_to_csv(students, filename)

def main() -> None:
    students: list[dict] = []
    while True:
        print_menu()
        choice: str = input("Enter your choice (1-6): ").strip()
        # Match case is only available after python 3.10
        match choice:
            case "1":
                add_student(students)
            case "2":
                list_students(students)
            case "3":
                search_student(students)
            case "4":
                delete_student(students)
            case "5":
                print_export_menu(students)
            case "6":
                print("Exiting the application...")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")
                
if __name__ == "__main__":
    main()