"""
This is a CLI application to calculate student results.
And (Possibly) to export them to a .csv file.
"""

# Helper functions


# App functionalities implementation
# def add_students(students: list[dict]) -> None:


# CLI menu printing function
def print_menu() -> None:
    print("=== Student Results CLI ===")
    print("1) Add student + compute results")
    print("2) View students and result summary")
    print("3) Search student by Id")
    print("4) Delete student by Id")
    print("5) Export results to CSV file")
    print("6) Exit")

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
                print("Adding student...")
            case "2":
                print("Viewing students and result summary...")
            case "3":
                print("Searching student by Id...")
            case "4":
                print("Deleting student by Id...")
            case "5":
                print("Exporting results to CSV file...")
            case "6":
                print("Exiting application.")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
