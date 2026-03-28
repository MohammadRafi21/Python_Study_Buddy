def show_menu():
    print("welcome to to PythonStudyBuddy")
    print("1. Add Topic")
    print("2. List Topics")
    print("3. Exit")

topics = {}

show_menu()

choice = int(input("Please Enter your choice "))
print(f"You chose : {choice}")

while True:
    if (choice == 1):
        print("Add Topic has been Selected")
    elif (choice == 2):
        print("List Topic has been Selected")
    elif (choice == 3):
        print("You have exited the Menu")
        break
    else:
        print("Invalid choice")



