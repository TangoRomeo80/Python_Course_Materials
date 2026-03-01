"""
This is a CLI application to calculate student results.
And (Possibly) export to a .csv file.
"""
from __future__ import annotations
from data_processor import add_students, list_students, search_student, delete_student
from utils import prompt_non_empty
from export_csv import export_to_csv

# CLI menu printing function
def print_menu() -> None:
    print("=== Student Results Calculator ===")
    print("1) Add student + compute results")
    print("2) List students and result summary")
    print("3) Search student by ID")
    print("4) Delete student by ID ")
    print("5) Export all results to CSV")
    print("6) Exit")

def export_prompt_menu(students: list[dict]) -> None:
    if not students:
        print("No students to export.")
        return
    filename = prompt_non_empty("Enter filename to export (e.g., results.csv): ")
    export_to_csv(students, filename)

def main() -> None:
    # List to contain students' information
    students: list[dict] = [] # With annotation
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        #match-case is only available after Python 3.10+
        match choice:
            case "1":
                add_students(students)
            case "2":
                list_students(students)
            case "3":
                search_student(students)
            case "4":
                delete_student(students)
            case "5":
                export_prompt_menu(students)
            case "6":
                print("Exiting the application.")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()