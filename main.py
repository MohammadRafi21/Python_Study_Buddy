def show_menu():
    print("welcome to to PythonStudyBuddy")
    print("1. Add Topic")
    print("2. List Topics")
    print("3. Exit")

def add_topic(topics_dict):
    topic1 = input("Enter the topic name: ")
    descrip1 = input("Enter the topic description: ")
    topics_dict.update({topic1: descrip1})
    print("Topic added successfully!")
def list_topics(topics_dict):
    if not topics_dict:
        print("No topics available.")
    else:
        for topic, description in topics_dict.items():
            print(f"Topic: {topic}, Description: {description}")

topics = {}

while True:

    show_menu()

    choice = int(input("Please Enter your choice "))
    print(f"You chose : {choice}")


    if (choice == 1):
        print("Add Topic has been Selected")
        add_topic(topics)
    elif (choice == 2):
        print("List Topic has been Selected")
        list_topics(topics)
    elif (choice == 3):
        print("You have exited the Menu")
        break
    else:
        print("Invalid choice")
 
    



