import unittest
from tracker import BugTracker

class TestBugTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = BugTracker()
        
    def test_create_bug(self):
        bug_id = self.tracker.create_bug("Login Issue", "User cannot login", "High")
        bug = self.tracker.find_bug_by_id(bug_id)

        self.assertIsNotNone(bug)

    def test_update_bug_status(self):
        bug_id = self.tracker.create_bug("Login Issue", "User cannot login", "High")
        self.tracker.update_bug_status(bug_id, "Resolved")
        bug = self.tracker.find_bug_by_id(bug_id)

        self.assertEqual(bug[4], "Resolved")

    def test_add_bug_comment(self):
        bug_id = self.tracker.create_bug("UI Issue", "Button btoken", "Low")
        self.tracker.add_bug_comment(bug_id, "Developer investigating")
        comments = self.tracker.show_bug_comments(bug_id)

        self.assertEqual(len(comments), 1)

    def test_new_bug_starts_open(self):
        bug_id = self.tracker.create_bug("Signup Error", "Cannot create account", "High")
        bug = self.tracker.find_bug_by_id(bug_id)
        self.assertEqual(bug[4], "Open")