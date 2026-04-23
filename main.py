from models import Bug

class BugTracker:
    def __init__(self):
        self.bugs = []
        self.next_id = 1

    def create_bug(self, title, description, severity):
        bug = Bug(self.next_id, title, description, severity)
        self.bugs.append(bug)
        self.next_id += 1
        return bug
    
    def list_bugs(self):
        for bug in self.bugs:
            print(bug)

# Test manually
if __name__ == "__main__":
    tracker = BugTracker()

    tracker.create_bug("Login error", "User can't log in", "High")
    tracker.create_bug("UI glitch", "Button misaligned", "Low")

    tracker.list_bugs()