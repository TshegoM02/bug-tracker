from models import Bug # Bring somthing from another file, in this case the Bug class from models
import sqlite3

# This will manage multiple bugs
class BugTracker:
    def __init__(self): # Runs when a tracker is craeted
        self.connection = sqlite3.connect("bugs.db") # Connect to the database file, if it doesn't exist it will be created
        self.cursor = self.connection.cursor()

    def create_bug(self, title, description, severity): # This function creates a new bug with the given details
        self.cursor.execute("""
        INSERT INTO bugs (title, description, severity, status)
        VALUES (?, ?, ?, ?)
        """, (title, description, severity, "Open"))
        
        self.connection.commit()
    
    def find_bug_by_id(self, bug_id):
        self.cursor.execute(
            "SELECT * FROM bugs WHERE id = ?",
            (bug_id,)
        )
        
        return self.cursor.fetchone()

    def update_bug_status(self, bug_id, new_status):
        self.cursor.execute("""
        UPDATE bugs
        SET status = ?
        WHERE id = ?
        """, (new_status, bug_id))

        self.connection.commit()
    
    def add_bug_comment(self, bug_id, comment):
        self.cursor.execute("""
        INSERT INTO comments (bug_id, comment)
        VALUES (?, ?)
        """, (bug_id, comment))

        self.connection.commit()

    def show_bug_comments(self, bug_id):
        self.cursor.execute("""
        SELECT comment FROM comments
        WHERE bug_id = ?
        """, (bug_id,))

        comments = self.cursor.fetchall()
        
        for comment in comments:
            print(comment[0])

    def list_bugs(self):
        self.cursor.execute("SELECT * FROM bugs")
        
        bugs = self.cursor.fetchall()
        
        for bug in bugs: # For loop to go through each bug in the list
            print(bug) 

# Test manually
if __name__ == "__main__": # Only run this code if this file is run directly
    tracker = BugTracker() # Create a BugTracker object, make a new tracker

    tracker.create_bug("Login error", "User unable tologin", "High") # Tell tracker to create a bug with this info
    tracker.update_bug_status(9, "In Progress")
    tracker.add_bug_comment(9, "Developer investigating issue")

    tracker.list_bugs() # Show all bugs in the tracker, should show the two we just created

    print("\nComments for Bug 1:") # Print a header for the comments
    tracker.show_bug_comments(9) # Show comments for bug with id 1