import json
def show_menu():
    print("welcome to to PythonStudyBuddy")
    print("1. Add Topic")
    print("2. List Topics")
    print("3. Search Topics")
    print("4. Add Notes")
    print("5. Update Status")
    print("6. Save Data")
    print("7. Exit")

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
        details = topics_dict[search_key]
        print(f"Topic: {search_key}")
        print(f"Description: {details['description']}")
        print(f"Status: {details['status']}")
        if not details['notes']:
            print("No notes available for this topic.")
        else:
            for i in range(len(details['notes'])):
                print(f"Note {i+1}: {details['notes'][i]}")
    else:
        print("Topic not found")

def add_notes(topics_dict):
    topic_name = input("Please enter the name of the topic: ")
    if topic_name in topics_dict:
        notes = input("Please Add your notes: ")
        topics_dict[topic_name]["notes"].append(notes)
        print("Notes has been added successfully!")
    else:
        print("Topic not found")

def update_status(topics_dict):
    topic_name = input("Please enter the name of the topic: ")
    if topic_name in topics_dict:
        print("Update your status:")
        print("Enter 1 for Learning")
        print("Enter 2 for Revised")
        print("Enter 3 for Mastered")
        status_update = int(input("Please enter your choice: "))
        if status_update == 1:
            topics_dict[topic_name]["status"] = "Learning"
            print("Status has been updated successfully!")
        elif status_update == 2:
            topics_dict[topic_name]["status"] = "Revised"
            print("Status has been updated successfully!")
        elif status_update == 3:
            topics_dict[topic_name]["status"] = "Mastered"
            print("Status has been updated successfully!")
        else:
            print("Invalid choice")
    
    else:
        print("Topic not found")



topics = {}

while True:

    show_menu()

    choice = int(input("Please Enter your choice in number: "))
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
        print("Add Notes has been Selected")
        add_notes(topics)
    elif (choice == 5):
        print("Updating Status")
        update_status(topics)
    elif (choice == 6):
        print("Save Data has been Selected")
        # Implement save data functionality here
    elif (choice == 7):
        print("You have exited the Menu")
        break
    else:
        print("Invalid choice")
 
    



