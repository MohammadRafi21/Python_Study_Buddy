import json
import logging
import src.logger_config
from src.storage import save_data, load_data
from src.operation import add_topic, list_topics, search_topic, add_notes, update_status, delete_topic







def show_menu():
    print("welcome to to PythonStudyBuddy")
    print("1. Add Topic")
    print("2. List Topics")
    print("3. Search Topics")
    print("4. Add Notes")
    print("5. Update Status")
    print("6. Delete Topic")
    print("7. Save Data")
    print("8. Exit")


topics = load_data()

while True:

    show_menu()

    try:
        choice = int(input("Please Enter your choice in number: "))
        print(f"You chose : {choice}")
    except ValueError:
        print("Invalid input. Please enter an integer number.")
        logging.warning("invalid menu input entered by user.")
        continue

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
        print("Delete Topic has been Selected")
        delete_topic(topics)
        # Implement delete topic functionality here
    elif (choice == 7):
        print("Save Data has been Selected")
        save_data(topics)
    elif (choice == 8):
        print("You have exited the Menu")
        break
    else:
        print("Invalid choice")
 
    



