from models import Bug # Bring somthing from another file, in this case the Bug class from models
import sqlite3

# This will manage multiple bugs
class BugTracker:
    def __init__(self): # Runs when a tracker is craeted
        self.connection = sqlite3.connect("bugs.db") # Connect to the database file, if it doesn't exist it will be created
        self.cursor = self.connection.cursor()

    def create_bug(self, title, description, severity): # This function creates a new bug with the given details
        bug = Bug(self.next_id, title, description, severity) # Create a new bug using the data given
        self.bugs.append(bug) # The list.add bug to list. Store this bug inside the tracker
        self.next_id += 1 # Add 1 to the next_id so next bug gets a new number
        return bug # Return the bug just created
    
    def find_bug_by_id(self, bug_id):
        for bug in self.bugs:
            if bug.id == bug_id:
                return bug
            
        return None

    def update_bug_status(self, bug_id, new_status):
        bug = self.find_bug_by_id(bug_id)
        
        if bug:
            bug.update_status(new_status)
            return True
        
        return False
    
    def add_bug_comment(self, bug_id, comment):
        bug = self.find_bug_by_id(bug_id)
        
        if bug:
            bug.add_comment(comment)
            return True
        
        return False # This function will change the status of a bug    
         # This function will find a bug by its ID number
    
    def list_bugs(self): # This function will show all bugs in the tracker
        for bug in self.bugs: # For loop to go through each bug in the list
            print(bug) 

# Test manually
if __name__ == "__main__": # Only run this code if this file is run directly
    tracker = BugTracker() # Create a BugTracker object, make a new tracker

    tracker.create_bug("Login error", "User can't log in", "High") # Tell tracker to create a bug with this info
    tracker.create_bug("UI glitch", "Button misaligned", "Low")
    
    tracker.update_bug_status(1, "In Progress")
    
    tracker.add_bug_comment(1, "Develop investigating issues") # Create another bug with different info

    tracker.list_bugs() # Show all bugs in the tracker, should show the two we just created