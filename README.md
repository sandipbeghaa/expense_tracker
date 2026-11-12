# Graphical Expense Tracker

A simple desktop expense tracker built with Python and Tkinter. It lets you record daily expenses with categories and notes, view all entries in a live table, and see automatic totals broken down by category. All data is saved locally in a JSON file so nothing gets lost when you close the app.

## What's Inside

- **Add Expenses:** Record the amount, category, and custom notes through a clean graphical form.
- **Live Expense Table:** View all logged expenses in an organized on-screen table that updates immediately.
- **Category Totals:** Automatically calculates how much you have spent in each category.
- **Automatic JSON Storage:** Saves every entry to a local `.json` file automatically and reloads your history the next time you open the app.
- **Zero External Dependencies:** Built purely with Python's standard library (`tkinter` and `json`).

## Built With

- Python 3
- Tkinter (GUI interface)
- JSON (local data persistence)

## Project Structure

```text
expense_tracker/
├── expense_tracker.py
└── README.md
```

## How to Run It on Your Computer

1. Make sure you have **Python 3** installed on your computer.
2. Clone or download this repository:
   ```bash
   git clone https://github.com/sandipbeghaa/expense_tracker
   ```
3. Open the project folder and run the Python script:
   ```bash
   cd expense_tracker
   python expense_tracker.py
   ```

## What I Practiced & Learned

- Designing a multi-section desktop layout with forms, tables, and summary totals in Tkinter.
- Reading and writing structured data to a local JSON file (`json.load` and `json.dump`) so user data persists across sessions.
- Grouping and summing expense records dynamically by category.

## Author

- **GitHub:** [github.com/sandipbeghaa](https://github.com/sandipbeghaa)
- **Portfolio:** [sandipbeghaa.github.io](https://sandipbeghaa.github.io/)
