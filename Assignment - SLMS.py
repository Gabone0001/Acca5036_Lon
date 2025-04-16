# Simple Library Management System (For Thonny or Any Python IDE)
# This console-based app uses lists and dictionaries for managing data [1][2]

# Data Storage (in-memory using Python lists and dictionaries) [2][3]
book_list = []
customer_list = []

# Generate Unique Customer IDs [3]
def generate_customer_id():
    return f"C{len(customer_list)+1:03}"

# Main Menu Function (Menu-driven CLI structure) [4]
def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Search Book")
        print("3. View Books")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Add Customer")
        print("7. View Customers")
        print("8. Rent Book")
        print("9. Return Book")
        print("0. Exit")

        choice = input("Enter your choice: ")

        # Menu Navigation Logic [4]
        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            view_books()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            add_customer()
        elif choice == "7":
            view_customers()
        elif choice == "8":
            rent_book()
        elif choice == "9":
            return_book()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

# Add Book Function
def add_book():
    # Input with exit handling for user-friendly navigation [5]
    title = input("Enter book title (or 'exit' to cancel): ")
    if title.lower() == 'exit': return

    author = input("Enter author name (or 'exit' to cancel): ")
    if author.lower() == 'exit': return

    ui_no = input("Enter unique book ID (UI No.) (or 'exit' to cancel): ")
    if ui_no.lower() == 'exit': return

    # Prevent duplicate UI Nos. [3]
    for book in book_list:
        if book['ui_no'] == ui_no:
            print("Book already exists.")
            return

    # Append book to the in-memory list [2]
    book = {"title": title, "author": author, "ui_no": ui_no, "status": "available"}
    book_list.append(book)
    print("Book added successfully.")

# Search Book Function
def search_book():
    term = input("Enter book title, author, or UI No. to search (or 'exit'): ")
    if term.lower() == 'exit': return

    for book in book_list:
        if term.lower() in book['title'].lower() or term.lower() in book['author'].lower() or term == book['ui_no']:
            print(book)
            return
    print("Book not found.")

# View Books Function
def view_books():
    if not book_list:
        print("No books available.")
    else:
        for book in book_list:
            print(book)

# Update Book Details
def update_book():
    ui_no = input("Enter UI No. of the book to update (or 'exit'): ")
    if ui_no.lower() == 'exit': return

    for book in book_list:
        if book['ui_no'] == ui_no:
            # Optional updates [1]
            title = input("Enter new title (or press Enter to skip): ")
            author = input("Enter new author (or press Enter to skip): ")
            if title: book['title'] = title
            if author: book['author'] = author
            print("Book updated successfully.")
            return
    print("Book not found.")

# Delete Book
def delete_book():
    ui_no = input("Enter UI No. to delete (or 'exit'): ")
    if ui_no.lower() == 'exit': return

    for book in book_list:
        if book['ui_no'] == ui_no:
            confirm = input("Are you sure? (yes/no): ")
            if confirm.lower() == 'yes':
                book_list.remove(book)
                print("Book deleted.")
            return
    print("Book not found.")

# Add Customer Function
def add_customer():
    name = input("Enter customer name (or 'exit'): ")
    if name.lower() == 'exit': return

    phone = input("Enter phone number (or 'exit'): ")
    if phone.lower() == 'exit': return

    customer_id = generate_customer_id()
    customer = {"id": customer_id, "name": name, "phone": phone}
    customer_list.append(customer)
    print("Customer added successfully with ID:", customer_id)

# View All Customers
def view_customers():
    if not customer_list:
        print("No customers found.")
    else:
        for customer in customer_list:
            print(customer)

# Rent Book Function (Link book to customer ID)
def rent_book():
    customer_id = input("Enter customer ID (or 'exit'): ")
    if customer_id.lower() == 'exit': return

    ui_no = input("Enter book UI No. to rent (or 'exit'): ")
    if ui_no.lower() == 'exit': return

    for customer in customer_list:
        if customer['id'] == customer_id:
            for book in book_list:
                if book['ui_no'] == ui_no:
                    if book['status'] == 'available':
                        book['status'] = f"borrowed by {customer_id}"
                        print("Book rented successfully.")
                    else:
                        print("Book is not available.")
                    return
            print("Book not found.")
            return
    print("Customer not found.")

# Return Book Function
def return_book():
    ui_no = input("Enter book UI No. to return (or 'exit'): ")
    if ui_no.lower() == 'exit': return

    for book in book_list:
        if book['ui_no'] == ui_no:
            if book['status'].startswith("borrowed"):
                book['status'] = "available"
                print("Book returned successfully.")
            else:
                print("This book is already available.")
            return
    print("Book not found.")

# Program Entry Point
main_menu()
