'''
A simple command line application to calculate student
results, and also export them to a .csv file.
'''

def prompt_non_empty(prompt: str) -> str:
    while True:
        s: str = input(prompt).strip()
        if s != "":
            return s
        print("Empty input is not allowed, try again.")

def clean_name(name: str) -> str:
    return name.title()

def prompt_int(prompt: str, min_val: int = 0, max_val: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Invalid input, please enter a valid integer.")
            continue

        if val < min_val:
            print(f"Value must be at least {min_val}.")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be at most {max_val}.")
            continue
        return val
    
def prompt_float(prompt: str, min_val: float = 0.0, max_val: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("Invalid input, please enter a valid number.")
            continue

        if val < min_val:
            print(f"Value must be at least {min_val}.")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be at most {max_val}.")
            continue
        return val
    
def grade_from_percentage(pct: float) -> str:
    if pct >= 90.0:
        return "A"
    elif pct >= 80.0:
        return "B"
    elif pct >= 70.0:
        return "C"
    elif pct >= 60.0:
        return "D"
    else:
        return "F"
    
def compute_total_and_percentage(marks: list[float]) -> tuple[float, float]:
    # total = sum(marks)
    total = 0.0
    for m in marks:
        total += m
    percentage = total / len(marks)
    return total, percentage

def add_student(students: list[dict]) -> None:
    sid = prompt_non_empty("Enter student Id: ")
    name = clean_name(prompt_non_empty("Enter student name: "))

    n = prompt_int("Enter number of subjects: ", min_val=1)

    subjects: list[str] = []
    marks: list[float] = []

    for i in range(n):
        sub = prompt_non_empty(f"Enter name of subject {i + 1}: ")
        sub = sub.strip().title()
        subjects.append(sub)

        mk = prompt_float(f"Enter marks for {sub}: ", min_val=0.0, max_val=100.0)
        marks.append(mk)

    # Compute
    total, pct = compute_total_and_percentage(marks)
    grade = grade_from_percentage(pct)
    status = "Pass" if grade != "F" else "Fail"

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


