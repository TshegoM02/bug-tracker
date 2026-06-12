from models import Bug # Bring somthing from another file, in this case the Bug class from models
import sqlite3
from tracker import BugTracker

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
                comments = tracker.show_bug_comments(bug_id)
                for comment in comments:
                    print(comment[0])
            else:
                print("Bug not found.")

        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose an option from 1-6.")