from src.models import Topic

# loop_topic = Topic("Python", "A programming language")
# loop_topic.add_note("This is a sample note.")
# loop_topic.load_from_dict({"description": "Updated description", "status": "Revised", "notes": ["This is a loaded note."]})
# loop_topic.display()
# loop_topic.update_status("Mastered")
# loop_topic.display()
# slicing_topic = Topic("Data Structures", "A topic in computer science")
# slicing_topic.add_note("This is another slicing note.")
# slicing_topic.display()

# Testing the from_dict method
saved_data = {
    "description": "A programming language",
    "status": "Revised",
    "notes": ["Learn variables", "Practice loops"]
}
python_topic = Topic.from_dict("Python", saved_data)
python_topic.display()



