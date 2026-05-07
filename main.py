from models import Bug # Bring somthing from another file, in this case the Bug class from models

# This will manage multiple bugs
class BugTracker:
    def __init__(self): # Runs when a tracker is craeted
        self.bugs = [] # Empty list to store bugs
        self.next_id = 1 # Start counting bugs from 1

    def create_bug(self, title, description, severity): # This function creates a new bug with the given details
        bug = Bug(self.next_id, title, description, severity) # Create a new bug using the data given
        self.bugs.append(bug) # The list.add bug to list. Store this bug inside the tracker
        self.next_id += 1 # Add 1 to the next_id so next bug gets a new number
        return bug # Return the bug just created
    
    def list_bugs(self): # This fuction will show all bugs in the tracker
        for bug in self.bugs: # For loop to go through each bug in the list
            print(bug) 

# Test manually
if __name__ == "__main__": # Only run this code if this file is run directly
    tracker = BugTracker() # Create a BugTracker object, make a new tracker

    tracker.create_bug("Login error", "User can't log in", "High") # Tell tracker to create a bug with this info
    tracker.create_bug("UI glitch", "Button misaligned", "Low") # Create another bug with different info

    tracker.list_bugs() # Show all bugs in the tracker, should show the two we just created