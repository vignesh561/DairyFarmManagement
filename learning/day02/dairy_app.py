cows = []

def add_cow():
    name = input("Enter Cow Name: ")
    age = int(input("Enter Cow Age: "))
    milk = float(input("Milk Produced Today: "))

    cow = {
        "name": name,
        "age": age,
        "milk": milk
    }

    cows.append(cow)
    print("\nCow added successfully!\n")


def view_cows():
    if not cows:
        print("\nNo cows found.\n")
        return

    print("\n----- Cow Records -----")
    for i, cow in enumerate(cows, start=1):
        print(f"{i}. {cow['name']} | Age: {cow['age']} | Milk: {cow['milk']} L")
    print()


while True:
    print("===== Dairy Farm Management =====")
    print("1. Add Cow")
    print("2. View Cows")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_cow()
    elif choice == "2":
        view_cows()
    elif choice == "3":
        print("Thank you for using Dairy Farm Management!")
        break
    else:
        print("Invalid choice. Please try again.\n")