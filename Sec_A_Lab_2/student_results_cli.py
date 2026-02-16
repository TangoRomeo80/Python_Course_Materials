'''
A simple command line application to calculate student
results, and also export them to a .csv file.
'''

def prompt_non_empty(prompt: str) -> str:
    while True:
        s: str = input(prompt).strip()
        if s:
            return s
        print("Empty input is not allowed, try again.")

def add_student(students: list[dict]) -> None:
    sid: str = prompt_non_empty("Enter student Id: ")

def print_menu() -> None:
    # pass
    print("-------- Student Results Calculator --------")
    print("1. Add student + compute results")
    print("2. List students and results")
    print("3. Search student by Id")
    print("4. Delete student by Id")
    print("5. Export results to CSV")
    print("6. Exit")

def main() -> None:
    students: list[dict] = [] # List to contain student data
    while True:
        print_menu()
        choice: str = input("Choose an option (1 - 6): ").strip()
        # match-case is only available after Python 3.10
        match choice:
            case "1":
                add_student(students)
            case "2":
                print("Listing students and results...")
            case "3":  
                print("Searching student by Id...")
            case "4":
                print("Deleting student by Id...")
            case "5":
                print("Exporting results to CSV...")
            case "6":
                print("Exiting the application. Goodbye!")
                break
            case _:
                print("Invalid choice, please choose a valid option (1 - 6).")

if  __name__ == "__main__":
    main()


