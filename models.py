class Bug:
    # Constructor. Values a bug must receive when created
    def __init__(self, bug_id, title, description, severity): # Object (this specific bug, its values)
        self.id = bug_id # Store bug_id in self.id, to use later in BugTracker
        self.title = title 
        self.description = description
        self.severity = severity
        self.status = "Open" # Every bug automatically starts as "Open"
        self.comment = [] # Each bug has a list of comments, but starts empty

    # Method to add a comment to the bug
    def add_comment(self, comment): # Function will add a comment to the bug's comment list
        self.comment.append(comment) # Take comment and add to the bug's comment list

    def update_status(self, new_status): # Function to update the bug's status
        self.status = new_status # Replace current bug's status with new status

    def __str__(self): # Function to return a string representation of the bug, for easy printing
        return f"[{self.id}] {self.title} - {self.severity} - {self.status}" # Formatted string