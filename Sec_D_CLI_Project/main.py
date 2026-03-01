"""
This is a CLI application to calculate student results.
And (Possibly) to export them to a .csv file.
"""
from __future__ import annotations

from data_processor import add_students, search_student, delete_student, list_students
from utils import prompt_non_empty
from export_csv import export_to_csv

# CLI menu printing function
def print_menu() -> None:
    print("=== Student Results CLI ===")
    print("1) Add student + compute results")
    print("2) View students and result summary")
    print("3) Search student by Id")
    print("4) Delete student by Id")
    print("5) Export results to CSV file")
    print("6) Exit")

def export_menu_prompt(students: list[dict]) -> None:
    if not students:
        print("No students to export.")
        return
    filename = prompt_non_empty("Enter filename to export (e.g. results.csv): ")
    export_to_csv(students, filename)

# Main function
def main() -> None:
    # List to contain students
    students: list[dict] = []
    while True:
        print_menu()
        # Variable to store the user choice
        choice = input("Choose and option (1 - 6): ").strip()
        # match-case is only available from Python 3.10+
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
                export_menu_prompt(students)
            case "6":
                print("Exiting application.")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
