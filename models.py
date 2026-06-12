class Bug:

    def __init__(self, bug_id, title, description, severity, status="Open"):
        self.id = bug_id
        self.title = title
        self.description = description
        self.severity = severity
        self.status = status

def __str__(self): # Controls how the bug is printed.
    return f"[{self.id}] {self.title} - {self.severity} - {self.status}"