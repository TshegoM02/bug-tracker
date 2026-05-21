import unittest
from tracker import BugTracker

class TestBugTracker(unittest.TestCase):
    def test_create_bug(self):
        tracker = BugTracker()

        bug_id = tracker.create_bug("Login Issue", "User cannot login", "High")

        bug = tracker.find_bug_by_id(bug_id)

        self.assertIsNotNone(bug)

