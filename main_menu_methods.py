import book_dao
import edit_book_menu_methods
import delete_book_menu_methods
import search_menu_methods
from pymongo_connector import collection_book

# Menu options methods

# Option 1 -> Add a publisher
def option1():
    # Query Info Input
    name = input("Enter name of the publisher: ")
    phone = input("Enter phone number of the publisher: ")
    city = input("Enter city of the publisher: ")

    book_dao.insertPublisher(name, phone, city)

# Option 2 -> Add a book
def option2():
    # Query Info Input
    ISBN = input("Enter ISBN of the book: ")
    title = input("Enter Title of the book: ")
    year = input("Enter Year of the book: ")
    published_by = input("Enter Publisher of the book: ")
    previous_edition = input("Enter Previous Edition ISBN of the book: ")
    price = input("Enter Price of the book: ")

    book_dao.insertBook(ISBN, title, year, published_by, previous_edition, price)

# Option 3 -> Edit a book
def option3(option, ISBN):
    # Menu Options:
    if  option == 1:
        newISBN = edit_book_menu_methods.option1(ISBN) # Change ISBN of a Book
    elif option == 2:
        edit_book_menu_methods.option2(ISBN) # Change Title of a Book
    elif option == 3:
        edit_book_menu_methods.option3(ISBN) # Change Year of a Book
    elif option == 4:
        edit_book_menu_methods.option4(ISBN) # Change Publisher of a Book
    elif option == 5:
        edit_book_menu_methods.option5(ISBN) # Change Previous Edition of a Book
    elif option == 6:
        edit_book_menu_methods.option6(ISBN) # Change Price of a Book
    elif option == 7:
        # Exit
        print('Going back to the main menu!')
        return None
    else:
        print('Invalid option. Please enter a number between 1 and 6.')

    # Returning the appropriate ISBN
    if (option == 1):
        return newISBN
    else:
        return ISBN

# Option 4 -> Delete a book
def option4(option):
    if option == 1:
        ISBN = input("Enter ISBN of the book you want to delete: ")

        # Checking for null condition
        if (ISBN.lower() == "null" or ISBN == ""):
            print("Error! Wrong input, ISBN is null.")
            return

        # Checking if the book doesn't exists:
        if collection_book.count_documents({ "ISBN": ISBN }) == 0:
            print("Error: Book doesn't exists with that ISBN! Returning back to the main menu.")
            return

        delete_book_menu_methods.option1(ISBN)  # Delete Book by ISBN
    elif option == 2:
        title = input("Enter title of the book you want to delete: ")

        # Checking for null condition
        if (title.lower() == "null" or title == ""):
            print("Error! Wrong input, Title is null.")
            return

        # Checking if the book doesn't exists:
        if collection_book.count_documents({ "title": title }) == 0:
            print("Error: Book doesn't exists with that Title! Returning back to the main menu.")
            return

        delete_book_menu_methods.option2(title) # Delete Book by Title
    elif option == 3:
        # Exit
        print('Going back to the main menu!')
        return None
    else:
        print('Invalid option. Please enter a number between 1 and 3.')

# Option 5 -> Search books
def option5(option):
    if   option == 1:
        search_menu_methods.search_all_books()          # Search All Book
    elif option == 2:
        search_menu_methods.search_by_title()           # Search Book by Title
    elif option == 3:
        search_menu_methods.search_by_publisher()       # Search Book by Publisher
    elif option == 4:
        search_menu_methods.search_by_price_range()     # Search Book by Price Range
    elif option == 5:
        search_menu_methods.search_by_title_publisher() # Search Book by Title and Publisher
    elif option == 6:
        # Exit
        print('Going back to the main menu!')
        return None
    else:
        print('Invalid option. Please enter a number between 1 and 6.')