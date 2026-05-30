books = []


def show_menu():
    print("""
██████╗  ██████╗  ██████╗ ██╗  ██╗
██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝
██████╔╝██║   ██║██║   ██║█████╔╝
██╔══██╗██║   ██║██║   ██║██╔═██╗
██████╔╝╚██████╔╝╚██████╔╝██║  ██╗
╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝

         B O O K V E R S E
    Where Every Book Has a Home
""")

    print("1. Register New Book")
    print("2. View Library Catalog")
    print("3. Find Book By Title")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. View Borrowed Books")
    print("7. View Available Books")
    print("8. Remove Book")
    print("9. Library Statistics")
    print("10. Exit")


def register_book():
    code = f"BK-{len(books) + 1:03d}"
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    category = input("Enter book category: ")

    book = {
        "code": code,
        "title": title,
        "author": author,
        "category": category,
        "status": "Available",
        "borrower": ""
    }

    books.append(book)
    print(f"Book registered successfully! Book Code: {code}")


def view_catalog():
    if len(books) == 0:
        print("No books found in the library.")
        return

    print("\n--- Library Catalog ---")
    for book in books:
        print(f"Code: {book['code']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Category: {book['category']}")
        print(f"Status: {book['status']}")
        if book["borrower"] != "":
            print(f"Borrower: {book['borrower']}")
        print("-" * 30)


def find_book_by_title():
    title = input("Enter book title to search: ").lower()
    found = False

    for book in books:
        if title in book["title"].lower():
            print(f"\nCode: {book['code']}")
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Category: {book['category']}")
            print(f"Status: {book['status']}")
            found = True

    if not found:
        print("Book not found.")


def find_book_by_code(code):
    for book in books:
        if book["code"] == code:
            return book
    return None


def borrow_book():
    code = input("Enter book code: ")
    book = find_book_by_code(code)

    if book is None:
        print("Book not found.")
        return

    if book["status"] == "Borrowed":
        print("This book is already borrowed.")
        return

    borrower = input("Enter borrower name: ")
    book["status"] = "Borrowed"
    book["borrower"] = borrower
    print("Book borrowed successfully!")


def return_book():
    code = input("Enter book code: ")
    book = find_book_by_code(code)

    if book is None:
        print("Book not found.")
        return

    if book["status"] == "Available":
        print("This book is already available.")
        return

    book["status"] = "Available"
    book["borrower"] = ""
    print("Book returned successfully!")


def view_borrowed_books():
    found = False

    print("\n--- Borrowed Books ---")
    for book in books:
        if book["status"] == "Borrowed":
            print(f"{book['code']} | {book['title']} | Borrower: {book['borrower']}")
            found = True

    if not found:
        print("No borrowed books found.")


def view_available_books():
    found = False

    print("\n--- Available Books ---")
    for book in books:
        if book["status"] == "Available":
            print(f"{book['code']} | {book['title']} | {book['author']}")
            found = True

    if not found:
        print("No available books found.")


def remove_book():
    code = input("Enter book code to remove: ")
    book = find_book_by_code(code)

    if book is None:
        print("Book not found.")
    else:
        books.remove(book)
        print("Book removed successfully!")


def library_statistics():
    total_books = len(books)
    available_books = 0
    borrowed_books = 0

    for book in books:
        if book["status"] == "Available":
            available_books += 1
        else:
            borrowed_books += 1

    print("\n--- Library Statistics ---")
    print(f"Total Books: {total_books}")
    print(f"Available Books: {available_books}")
    print(f"Borrowed Books: {borrowed_books}")


while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        register_book()
    elif choice == "2":
        view_catalog()
    elif choice == "3":
        find_book_by_title()
    elif choice == "4":
        borrow_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        view_borrowed_books()
    elif choice == "7":
        view_available_books()
    elif choice == "8":
        remove_book()
    elif choice == "9":
        library_statistics()
    elif choice == "10":
        print("Thank you for using BookVerse. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
    