import logging

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
    logging.info(f"Added topic: {topic_name}")
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
        logging.info(f"Added note to topic '{topic_name}': {notes}")
        print("Notes has been added successfully!")
    else:
        print("Topic not found")

def update_status(topics_dict):
    topic_name = input("Please enter the name of the topic: ")
    if topic_name in topics_dict:
        status_dict = {
            1: "Learning",
            2: "Revised",
            3: "Mastered",
            4: "Need to Practice"
        }
        print("Update your status:")
        print("Enter 1 for Learning")
        print("Enter 2 for Revised")
        print("Enter 3 for Mastered")
        print("Enter 4 for Need to Practice")
        try:
            status_update = int(input("Please enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        if status_update in status_dict:
            topics_dict[topic_name]["status"] = status_dict[status_update]
            logging.info(f"Updated status for topic '{topic_name}': {status_dict[status_update]}")
            print("Status has been updated successfully!")
        else:
            print("Invalid choice")
    
    else:
        print("Topic not found")
def delete_topic(topics_dict):
    topic_name = input("Please enter the name of the topic: ")
    # if topic_name in topics_dict:
    #     del topics_dict[topic_name]
    #     logging.info(f"Deleted topic: {topic_name}")
    #     print("Topic has been deleted successfully!")
    if topic_name in topics_dict:
        topics_dict.pop(topic_name)
        logging.info(f"Deleted topic: {topic_name}")
        print("Topic has been deleted successfully!")
    else:
        print("Topic not found")