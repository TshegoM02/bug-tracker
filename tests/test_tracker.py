import unittest
from tracker import BugTracker

class TestBugTracker(unittest.TestCase):
    def test_create_bug(self):
        tracker = BugTracker()
        bug_id = tracker.create_bug("Login Issue", "User cannot login", "High")
        bug = tracker.find_bug_by_id(bug_id)

        self.assertIsNotNone(bug)

    def test_update_bug_status(self):
        tracker = BugTracker()
        bug_id = tracker.create_bug("Login Issue", "User cannot login", "High")
        tracker.update_bug_status(bug_id, "Resolved")
        bug = tracker.find_bug_by_id(bug_id)

        self.assertEqual(bug[4], "Resolved")

    def test_add_bug_comment(self):
        tracker = BugTracker()
        bug_id = tracker.create_bug("UI Issue", "Button btoken", "Low")
        tracker.add_bug_comment(bug_id, "Developer investigating")
        comments = tracker.show_bug_comments(bug_id)
        self.assertEqual(len(comments), 1)

