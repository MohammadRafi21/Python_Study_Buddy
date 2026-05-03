def show_menu():
    print("welcome to to PythonStudyBuddy")
    print("1. Add Topic")
    print("2. List Topics")
    print("3. Search Topics")
    print("4. Exit")

def add_topic(topics_dict):
    topic_name = input("Enter the topic name: ")
    description = input("Enter the topic description: ")
    details =  {
        "description": description,
        "status": "Learning",
        "notes": []
    }
    topics_dict[topic_name] = details
    # topics_dict.update({topic_name: description})
    print("Topic added successfully!")
def list_topics(topics_dict):
    if not topics_dict:
        print("No topics available.")
    else:
        for topic, details in topics_dict.items():
            print(f"Topic: {topic}")
            print(f"Description: {details['description']}")
            print(f"Status: {details['status']}")
            print()

def search_topic(topics_dict):
    search_key = input("Please enter the name of the topic: ")
    if search_key in topics_dict:
        print(topics_dict[search_key])
    else:
        print("Topic not found")



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
        print("Search Topics has been Selected")
        search_topic(topics)
        # Implement search functionality here
    elif (choice == 4):
        print("You have exited the Menu")
        break
    else:
        print("Invalid choice")
 
    



