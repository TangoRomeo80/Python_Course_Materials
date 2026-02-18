"""
Docstring for students_results_cli
This is an application for calculatingand storing student results.
This will run in the CLI.
If possible we will also save it in a .csv file.
"""

def prompt_non_empty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s != "":
            return s
        print("Empty input not allowed, please try again.")

def format_name(name: str) -> str:
    return name.title()

def prompt_int(prompt: str, min_value: int = 0, max_value: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if val < min_value:
            print(f"Value must be at least {min_value}. Please try again.")
            continue
        if max_value is not None and val > max_value:
            print(f"Value must be at most {max_value}. Please try again.")
            continue
        return val

def prompt_float(prompt: str, min_value: float = 0.0, max_value: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if val < min_value:
            print(f"Value must be at least {min_value}. Please try again.")
            continue
        if max_value is not None and val > max_value:
            print(f"Value must be at most {max_value}. Please try again.")
            continue
        return val

def grade_from_percentage(pct: float) -> str:
    if pct >= 90:
        return "A"
    elif pct >= 80:
        return "B"
    elif pct >= 70:
        return "C"
    elif pct >= 60:
        return "D"
    else:
        return "F"

def add_student(students: list[dict]) -> None:
    sid = prompt_non_empty("Enter student Id: ")
    name = format_name(prompt_non_empty("Enter student name: "))

    n = prompt_int("Enter number of subjects: ", min_value=1)

    subjects: list[str] = []
    marks: list[float] = []

    for i in range(n):
        sub = prompt_non_empty(f"Enter name of subject {i+1}: ")
        sub = sub.strip().title()
        subjects.append(sub)

        mk = prompt_float(f"Enter marks for {sub}: ", min_value=0.0, max_value=100.0)
        marks.append(mk)

    #Computation


    #
def print_menu() -> None:
    print("---------- Student Result Calculator ----------")
    print("1) Add student result + calculate results")
    print("2) List all student results")
    print("3) Search student by Id")
    print("4) Delete student by Id")
    print("5) Save results to .csv file")
    print("6) Exit")

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
                print("Listing all student results...")
                # Here you would add the logic to list all student results
                pass
            case "3":
                print("Searching student by Id...")
                # Here you would add the logic to search for a student by Id
                pass
            case "4":
                print("Deleting student by Id...")
                # Here you would add the logic to delete a student by Id
                pass
            case "5":
                print("Saving results to .csv file...")
                # Here you would add the logic to save results to a .csv file
                pass
            case "6":
                print("Exiting the application...")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 6.")
                
if __name__ == "__main__":
    main()