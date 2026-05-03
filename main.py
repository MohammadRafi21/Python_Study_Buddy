def show_menu():
    print("welcome to to PythonStudyBuddy")
    print("1. Add Topic")
    print("2. List Topics")
    print("3. Exit")

topics = {}

while True:

    show_menu()

    choice = int(input("Please Enter your choice "))
    print(f"You chose : {choice}")


    if (choice == 1):
        print("Add Topic has been Selected")
        topic1 = input("Enter the topic name: ")
        descrip1 = input("Enter the topic description: ")
        topics.update({topic1: descrip1})
        print("Topic added successfully!")
    elif (choice == 2):
        print("List Topic has been Selected")
        for topic1, descrip1 in topics.items():
            print(f"Topic: {topic1}, Description: {descrip1}")
    elif (choice == 3):
        print("You have exited the Menu")
        break
    else:
        print("Invalid choice")
 
    



