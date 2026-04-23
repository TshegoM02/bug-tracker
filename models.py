class Bug:
    def __init__(self, bug_id, title, description, severity):
        self.id = bug_id
        self.title = title
        self.description = description
        self.severity = severity
        self.status = "Open"
        self.comment = []

    def add_comment(self, comment):
        self.comment.append(comment)

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"[{self.id}] {self.title} - {self.severity} - {self.status}"