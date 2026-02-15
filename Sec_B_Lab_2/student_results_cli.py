"""
This is a CLI application to calculate student results.
And (Possibly) export to a .csv file.
"""

# Helper functions
# function to prompt user to provide non-empty value
def prompt_non_empty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        else:
            print("Empty input is not allowed. Try again.")

# App actions implementation
# Function to add student
def add_students(students: list[dict]) -> None:
    # Collect student infor from user and compute results
    sid =  prompt_non_empty("Enter Student Id: ")
    

# CLI menu printing function
def print_menu() -> None:
    print("=== Student Results Calculator ===")
    print("1) Add student + compute results")
    print("2) List students and result summary")
    print("3) Search student by ID")
    print("4) Delete student by ID ")
    print("5) Export all results to CSV")
    print("6) Exit")

def main() -> None:
    # List to contain students' information
    students: list[dict] = [] # With annotation
    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()
        #match-case is only available after Python 3.10+
        match choice:
            case "1":
                print("Adding a new student...")
            case "2":
                print("Listing all students...")
            case "3":
                print("Searching for a student by ID...")
            case "4":
                print("Deleting a student by ID...")
            case "5":
                print("Exporting all results to CSV...")
            case "6":
                print("Exiting the application.")
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()