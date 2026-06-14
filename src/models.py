class Topic:
    def __init__(self, name, description): # This runs automatically when a new object is created.
        self.name = name
        self.description = description
        self.status = "Learning"
        self.notes = []
    def add_note(self, note): # method is fuction 
        #that belongs to a class and can be called on 
        # an instance of the class. 
        # It is used to perform operations related to 
        # the class and its attributes.
        self.notes.append(note) # The append() method is used to add an item to the end of a list.
    def update_status(self, new_status):
        self.status = new_status
    # def __str__(self):
    #     return f"Topic: {self.name}, Description: {self.description}, Status: {self.status}, Notes: {self.notes}"
    def display(self):
        print(f"Topic: {self.name}")
        print(f"Description: {self.description}")
        print(f"Status: {self.status}")
        if not self.notes:
            print("No notes available for this topic.")
        else:
            for i in range(len(self.notes)):
                print(f"Note {i+1}: {self.notes[i]}")
    def to_dict(self):
        return {
            "description": self.description,
            "status": self.status,
            "notes": self.notes
        }
    def load_from_dict(self, data):
        self.description = data.get("description","")
        self.status = data.get("status","Learning") #after the comma is the default value if the key is not found in the dictionary
        self.notes = data.get("notes",[])
    
    # now we are doing this because we are creating a object form a dictionary that object does not exist yet, so we are reusing the topic class to create 
    # a new object and then we are loading the data from the dictionary to that object.
    # We use from_dict because the object does not exist yet.
    # This method creates a new Topic object from dictionary data.
    @classmethod
    def from_dict(cls,name,data):
        topic = cls(name, data.get("description",""))
        # for learning purposes
        # topic.status = data.get("status","Learning")
        # topic.notes = data.get("notes",[])
        topic.load_from_dict(data) # just reusing the load_from_dict method to load the data from the dictionary to the topic object.
        return topic

        
        

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
# saved_data = {
#     "description": "A programming language",
#     "status": "Revised",
#     "notes": ["Learn variables", "Practice loops"]
# }
# python_topic = Topic.from_dict("Python", saved_data)
# python_topic.display()



