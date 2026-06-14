from src.models import Topic
import json
import logging

def save_data(topics_dict):
    with open("study_data.json","w") as file:
        data_to_save = {}
        for topic_name, topic_object in topics_dict.items():
            data_to_save[topic_name] = topic_object.to_dict()
        json.dump(data_to_save, file, indent=4)
        # Dump is used to write the data to the file in json format jason.dump(data, file location)
    logging.info("Data has been saved successfully!")
    print("Data has been saved successfully!")

def load_data():
    try:
        with open("study_data.json","r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError: # If the json file does not exist, return an empty dictionary
        print("No existing data found. Starting with an empty topic list.")
        logging.warning("No existing data found. Starting with an empty topic list.")
        return {}
    except json.JSONDecodeError: # If the json file is empty or has invalid format, return an empty dictionary
        print("Existing data is invalid. Starting with an empty topic list.")
        logging.warning("Existing data is invalid. Starting with an empty topic list.")
        return {}
