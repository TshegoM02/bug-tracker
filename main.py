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

        return self.cursor.lastrowid
    
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

    while True:
        print("\nBug Tracker Menu")
        print("1. Create Bug")
        print("2. View Bugs")
        print("3. Update Bug Status")
        print("4. Add Comment")
        print("5. View Comments")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter bug title: ")
            description = input("Enter description: ")

            while True:
                severity = input("Enter severity (Low/Medium/High): ").title()
                if severity in ["Low", "Medium", "High"]:
                    break
                print("Invalid severity. Please choose Low, Medium, or High.")

            bug_id = tracker.create_bug(title, description, severity)

            print(f"Bug created with ID {bug_id}")

        elif choice == "2":
            tracker.list_bugs()

        elif choice == "3":
            bug_id = int(input("Enter bug ID: "))
            
            while True:
                new_status = input("Enter new status (Open/In Progress/Resolved): ").title()
                if new_status in ["Open", "In Progress", "Resolved"]:
                    break
                print("Invalid status. Please choose Open, In Progress, or Resolved.")
            bug = tracker.find_bug_by_id(bug_id)
            if bug:
                tracker.update_bug_status(bug_id, new_status)
                print("Status updated.")
            else:
                print("Bug not found.")            

        elif choice == "4":
            bug_id = int(input("Enter bug ID: "))
            comment = input("Enter comment: ")
            bug = tracker.find_bug_by_id(bug_id)
            if bug:
                tracker.add_bug_comment(bug_id, comment)
                print("Comment added.")
            else:
                print("Bug not found.")

        elif choice == "5":
            bug_id = int(input("Enter bug ID: "))
            bug = tracker.find_bug_by_id(bug_id)
            if bug:
                print(f"\nComments for Bug {bug_id}:")
                tracker.show_bug_comments(bug_id)
            else:
                print("Bug not found.")

        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose an option from 1-6.")
        