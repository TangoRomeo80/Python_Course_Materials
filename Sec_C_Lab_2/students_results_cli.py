"""
Docstring for students_results_cli
This is an application for calculatingand storing student results.
This will run in the CLI.
If possible we will also save it in a .csv file.
"""

def print_menu() -> None:
    print("---------- Student Result Calculator ----------")
    print("1) Add student result + calculate results")
    print("2) List all student results")
    print("3) Search student by Id")
    print("4) Delete student by Id")
    print("5) Save results to .csv file")
    print("6) Exit")

def main() -> None:
    while True:
        print_menu()
        choice: str = input("Enter your choice (1-6): ").strip()
        # Match case is only available after python 3.10
        match choice:
            case "1":
                print("Adding student result...")
                # Here you would add the logic to add a student result
                pass
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