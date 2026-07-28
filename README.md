# 💰 Personal Finance Tracker

A command-line personal finance tracker built as a team project. It lets you
log income, add and manage expenses, and check whether you're staying within
budget — all through a simple interactive menu.

## Features

- 📥 Add monthly income
- 🧾 Add, update, and adjust expenses (with category, amount, and date)
- 🔍 Search expenses by category
- 📊 Display all expenses, or only those above 500 ZMW
- ⚠️ Budget check with an overspending alert
- 🧮 Calculate remaining balance after expenses
- 🚫 Input validation — rejects negative expense amounts

## Getting started

### Prerequisites

- Python 3.7+ (no external dependencies — uses only the standard library)

### Installation

```bash
git clone https://github.com/<your-username>/personal-finance-tracker.git
cd personal-finance-tracker
```

### Usage

```bash
python financial_tracker_project_code.py
```

You'll see a menu like this:

```
--- Personal Finance Tracker ---
1. Add Income
2. Add Expense
3. Update Expense
4. Display All Expenses
5. Search Expenses by Category
6. Adjust Expense
7. Check Budget
8. Calculate Balance
9. Exit
Enter choice:
```

Follow the prompts to enter income and expenses, then use the other menu
options to review, search, or update your data.

## Project structure

```
personal-finance-tracker/
├── financial_tracker_project_code.py   # Main application
├── README.md
└── LICENSE
```

## Team contributions

This was built collaboratively:

| Contributor | Responsibility |
|---|---|
| Student A | Core variables, data entry setup, expense entry |
| Student B | Expense list, updating & searching expenses |
| Student C | Display/filter loops, input validation |
| Student D | Budget checking, balance calculation |
| Student E | Menu-driven user interface |

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
