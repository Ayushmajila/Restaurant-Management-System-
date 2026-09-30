# Project Statement: Restaurant Management System

## 1. Problem Statement

Small restaurants and cafés often handle orders, menu changes, and billing manually using pen and paper. This is slow and error-prone: prices get miscalculated, bills are written inconsistently, and updating the menu means rewriting lists by hand. There is a need for a simple, easy-to-use tool that lets staff take orders, calculate totals accurately, and manage the menu without any technical setup.

## 2. Objective

To design and develop a console-based Restaurant Management System in Python that automates order taking, menu management, and bill generation, reducing manual effort and calculation errors.

## 3. Scope

**In scope**
- Recording customer name and table number
- Displaying the menu with prices
- Taking orders with multiple items and quantities
- Calculating item totals and the grand total
- Generating a formatted bill
- Adding, removing, and updating menu items at runtime
- Menu-driven, looped navigation with basic input handling

**Out of scope (current version)**
- Permanent storage of menu, orders, or sales history
- User login or role-based access
- Taxes, discounts, and tips
- Graphical or web interface
- Inventory and staff management

## 4. Proposed Solution

A menu-driven Python program built from small, single-purpose functions:

| Function | Purpose |
|----------|---------|
| `get_customer_details()` | Collects customer name and table number |
| `display_menu()` | Prints the current menu and prices |
| `add_item()` / `remove_item()` / `update_price()` | Modify the menu |
| `manage_menu()` | Sub-menu for menu management |
| `place_order()` | Takes items and quantities, returns the order and total |
| `generate_bill()` | Prints the formatted bill |
| `main_menu()` | Main loop connecting all features |

The menu is stored in a dictionary (item → price) and each order is stored as a list of `[item, quantity, amount]` entries.

## 5. Expected Outcomes

- Faster and more accurate order processing
- Consistent, readable bills for every customer
- Easy menu updates without editing the source code
- A clear, beginner-friendly example of Python functions, dictionaries, lists, loops, and conditionals

## 6. Tools and Technologies

- Python 3 (standard library only)
- Command-line interface
- Any code editor or IDE (VS Code, PyCharm, IDLE)

## 7. Limitations

- Data is stored in memory only and is lost when the program closes
- Non-numeric input for price or quantity raises an error and stops the program
- Prices are whole numbers only
- Single-user, single-session use

## 8. Future Enhancements

- Input validation with `try`/`except`
- Saving menu and order history to JSON, CSV, or a database
- Tax, discount, and tip calculation
- Decimal price support
- Automated tests
- GUI or web-based interface

## 9. Conclusion

The Restaurant Management System demonstrates how a small, well-structured Python program can streamline the core tasks of a restaurant: ordering, billing, and menu management. It provides a solid foundation that can be extended with persistent storage, validation, and a richer interface.
