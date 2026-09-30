# 🍽️ Restaurant Management System

A simple, menu-driven console application written in Python for managing a restaurant menu, taking customer orders, and generating itemised bills.

---

## 📖 Overview

The Restaurant Management System is a command-line program that simulates the basic day-to-day operations of a small restaurant. Staff can take a customer's order, view the menu, and print a formatted bill with the total amount. The menu itself can be edited at runtime: new dishes can be added, existing dishes removed, and prices updated.

The project is built with plain Python (no external libraries), which makes it a good beginner-friendly example of functions, dictionaries, lists, loops, and user input handling.

---

## ✨ Features

**Customer Order**
- Record the customer's name and table number
- Display the current menu with prices
- Add multiple items with quantities to a single order
- Automatic calculation of item totals and the grand total
- Formatted bill showing customer, table number, items, quantities, and amounts

**Menu Management**
- Add a new food item with a price
- Remove an existing food item
- Update the price of an existing item
- Display the current menu

**General**
- Clean, text-based main menu with looped navigation
- Case-insensitive item names (input is converted to Title Case)
- Input validation for invalid menu choices and unavailable items

**Default Menu**

| Item       | Price |
|------------|-------|
| Burger     | $4    |
| Pizza      | $8    |
| Pasta      | $5    |
| Fried Rice | $6    |
| Coffee     | $7    |

---

## 🛠️ Technologies / Tools Used

- **Language:** Python 3.6 or higher
- **Libraries:** Python standard library only (no third-party packages required)
- **Data structures:** `dict` (menu), `list` (orders)
- **Interface:** Command-line / terminal
- **Editor (any):** VS Code, PyCharm, IDLE, or any text editor

---

## ⚙️ Installation and Setup

### 1. Prerequisites

Make sure Python 3 is installed. Check with:

```bash
python --version
```

or

```bash
python3 --version
```

If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

### 2. Get the project

Clone the repository (or simply download the files):

```bash
git clone <your-repository-url>
cd restaurant-management-system
```

### 3. Install dependencies

None. The project uses only built-in Python modules.

---

## ▶️ How to Run

From the project folder, run:

```bash
python restaurant.py
```

(or `python3 restaurant.py` on macOS/Linux). Replace `restaurant.py` with whatever you named the file.

### Sample usage

```
**************************************
            RESTAURANT
         MANAGEMENT SYSTEM
====================================
 MAIN MENU
====================================
1. Customer Order
2. Manage Menu
3. Exit
Enter your choice:1
```

1. Choose **1** to take an order: enter the customer name and table number, type item names from the menu, enter quantities, and press `q` to finish and print the bill.
2. Choose **2** to manage the menu (add, remove, update, or display items).
3. Choose **3** to exit.

---

## 🧪 Instructions for Testing

The project has no automated test suite, so testing is done manually by running the program and checking the output for each scenario below.

### Main menu
| Test | Input | Expected result |
|------|-------|-----------------|
| Invalid choice | `9` | "Invalid choice. Please try again." and menu is shown again |
| Exit | `3` | Thank-you message and program ends |

### Customer order
| Test | Input | Expected result |
|------|-------|-----------------|
| Valid order | Option `1`, name `Alex`, table `5`, item `pizza`, quantity `2`, then `q` | Bill shows 2 x Pizza = $16 and total $16 |
| Multiple items | `burger` x1, `coffee` x2, then `q` | Total = $4 + $14 = $18 |
| Unavailable item | `sushi` | "The item is not available." |
| Empty order | Press `q` immediately | Bill prints with total $0 |
| Case-insensitive names | `FRIED rice` | Recognised as "Fried Rice" |

### Menu management
| Test | Input | Expected result |
|------|-------|-----------------|
| Add item | Option `2` → `1`, name `Salad`, price `3` | "Salad has been added to the menu." and it appears in Display Menu |
| Remove item | Option `2` → `2`, name `Pasta` | Item removed and no longer shown |
| Remove missing item | Name `Steak` | "The item is not avaiable in the menu." |
| Update price | Option `2` → `3`, item `Burger`, new price `10` | Price updated to $10 |
| Update missing item | Item `Steak` | "The item is not available in the menu." |
| Back | Option `5` | Returns to the main menu |

### Edge cases to be aware of
- Entering non-numeric text for a **price** or **quantity** (for example `abc`) currently raises a `ValueError` and stops the program.
- Menu changes are stored in memory only and reset when the program is closed.

---

## 🚀 Possible Future Improvements

- Handle invalid numeric input with `try`/`except`
- Save the menu and order history to a file or database (JSON, CSV, SQLite)
- Add tax, discounts, and tip calculation
- Support decimal prices
- Add automated tests using `unittest` or `pytest`
- Build a GUI or web interface

---

## 📁 Project Structure

```
restaurant-management-system/
├── restaurant.py    # main program
└── README.md        # project documentation
```

---

## 📄 License

This project is open for learning and personal use. Add a license of your choice (for example MIT) if you plan to distribute it.
