"""
This is a CLI application to calculate student results.
And (Possibly) to export them to a .csv file.
"""

# Helper functions
def prompt_non_empty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Empty input is not allowed. Try again.")

def clean_name(raw_name: str) -> str:
    return raw_name.strip().title()

def prompt_int(prompt: str, min_val: int = 0, max_val: int | None = None) -> int:
    while True:
        raw = input(prompt).strip()
        try:
            val = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if val < min_val:
            print(f"Value must be at least {min_val}. Try again.")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be at most {max_val}. Try again.")
            continue
        return val
    
def prompt_float(prompt: str, min_val: float = 0.0, max_val: float | None = None) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            val = float(raw)
        except ValueError:
            print("Please enter a valid number.")
            continue
        if val < min_val:
            print(f"Value must be at least {min_val}. Try again.")
            continue
        if max_val is not None and val > max_val:
            print(f"Value must be at most {max_val}. Try again.")
            continue
        return val
    
def compute_total_and_percentage(marks: list[float]) -> tuple[float, float]:
    # total = sum(marks)
    total = 0.0
    for m in marks:
        total += m
    percentage = total / len(marks)
    return total, percentage

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
    
# App functionalities implementation
def add_students(students: list[dict]) -> None:
    sid = prompt_non_empty("Enter student Id: ")
    name = clean_name(prompt_non_empty("Enter student name: "))
    n = prompt_int("Enter number of subjects: ", min_val=1, max_val=10)

    subjects: list[str] = []
    marks: list[float] = []

    for i in range(n):
        sub = prompt_non_empty(f"Enter name of subject {i + 1}: ")
        sub = sub.strip().title()
        subjects.append(sub)

        mk = prompt_float(f"Enter marks for {sub}: ", min_val=0.0, max_val=100.0)
        marks.append(mk)

        # compute
        total, pct = compute_total_and_percentage(marks)
        grade = grade_from_percentage(pct)
        status = "Pass" if grade != "F" else "Fail"

        student = {
            "Id": sid,
            "Name": name,
            "Subjects": subjects,
            "Total": total,
            "Percentage": pct,
            "Grade": grade,
            "Status": status
        }
        students.append(student)


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
                add_students(students)
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
