# Bug Tracker

## 📌 Overview

A Python-based bug tracking system that allows users to create, manage, and track software bugs through a command-line interface.

## Features

- Create bug reports
- Assign severity levels (Low, Medium, High)
- Update bug status (Open, In Progress, Resolved)
- Add comments to bugs
- View bug comments
- SQLite database storage
- Input validation
- Automated unit tests

## Tech Stack

- Python
- SQLite
- Unittest

## Project Structure

```text
bug_tracker/
├── main.py
├── tracker.py
├── models.py
├── database.py
├── tests/
│   ├── __init__.py
│   └── test_tracker.py
└── README.md
```

## How to Run

1. Clone the repository
2. Navigate to the project folder

```bash
python3 main.py
```

## Run Tests

```bash
python3 -m unittest discover -s tests
```

## Future Improvements

- Search bugs by severity
- Filter bugs by status
- Delete bugs
- Add timestamps
- Build a web interface

## 👩‍💻 Author

### Tshegofatso Mnguni

Software Developer | QA Enthusiast

---