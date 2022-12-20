import sys
import search_menu_methods
import book_dao
import main_menu_methods
from pymongo_connector import collection_book
from pymongo_connector import collection_publisher

# -------------------- Menu Options --------------------

# Main Menu Options
menu_options = {
    1: 'Add a Publisher',
    2: 'Add a Book',
    3: 'Edit a Book',
    4: 'Delete a Book',
    5: 'Search Books',
    6: 'Exit',
}

# Search Book Menu Options
search_menu_options = {
    1: 'All Books',
    2: 'Title',
    3: 'Publisher',
    4: 'Price Range',
    5: 'Title and Publisher',
    6: 'Exit'
}

# Edit Book Menu Options
edit_book_menu_options = {
    1: 'Edit ISBN',
    2: 'Edit Title',
    3: 'Edit Year',
    4: 'Edit Publisher',
    5: 'Edit Previous Edition',
    6: 'Edit Price',
    7: 'Exit'
}

# Delete Book Menu Options
delete_book_menu_options = {
    1: 'Delete by ISBN',
    2: 'Delete by Title',
    3: 'Exit'
}

# ------------------------- Print Menus ----------------------------

# Dislaying main menu
def print_menu():
    print()
    print("-----------------Book Manager Software-----------------")
    print("|                                                     |")
    print("|  " + str(1)+'.', menu_options[1] + "               " + str(2)+'.', menu_options[2] + "     |")
    print("|  " + str(3)+'.', menu_options[3] + "                   " + str(4)+'.', menu_options[4] + "  |")
    print("|  " + str(5)+'.', menu_options[5] + "                  " + str(6)+'.', menu_options[6] + "           |")
    print("|                                                     |")
    print("|  Please make a number selection 1-6 from the menu   |")
    print("|                                                     |")
    print("-------------------------------------------------------")
    print()

# Displaying edit book menu
def print_edit_menu():
    print()
    print("-----------------Edit Book Information-----------------")
    print("|                                                     |")
    print("|  " + str(1)+'.', edit_book_menu_options[1] + "                   " + str(2)+'.', edit_book_menu_options[2] + "       |")
    print("|  " + str(3)+'.', edit_book_menu_options[3] + "                   " + str(4)+'.', edit_book_menu_options[4] + "   |")
    print("|  " + str(5)+'.', edit_book_menu_options[5] + "       " + str(6)+'.', edit_book_menu_options[6] + "       |")
    print("|  " + str(7)+'.', edit_book_menu_options[7] + "                                            |")
    print("|                                                     |")
    print("|  Please make a number selection 1-7 from the menu   |")
    print("|                                                     |")
    print("-------------------------------------------------------")
    print()

# Displaying delete book menu
def print_delete_menu():
    print()
    print("----------------------Delete Book----------------------")
    print("|                                                     |")
    print("|  " + str(1)+'.', delete_book_menu_options[1] + "              " + str(2)+'.', delete_book_menu_options[2] + "  |")
    print("|  " + str(3)+'.', delete_book_menu_options[3] + "                                            |")
    print("|                                                     |")
    print("|  Please make a number selection 1-3 from the menu   |")
    print("|                                                     |")
    print("--------------------------------------------------------")
    print()

# Displaying search book menu
def print_search_menu():
    print()
    print("----------------------------------Search Book----------------------------------")
    print("|                                                                             |")
    print("|  " + str(1)+'.', search_menu_options[1] + "                                             " + str(2)+'.', search_menu_options[2] + "          |")
    print("|  " + str(3)+'.', search_menu_options[3] + "                                             " + str(4)+'.', search_menu_options[4] + "    |")
    print("|  " + str(5)+'.', search_menu_options[5] + "                                   " + str(6)+'.', search_menu_options[6] + "           |")
    print("|                                                                             |")
    print("|              Please make a number selection 1-6 from the menu               |")
    print("|                                                                             |")
    print("-------------------------------------------------------------------------------")
    print()

# ------------------------- Executing Print Menus Options ----------------------------

# Check what choice was entered in the main menu
def checkOptions(option):
    if   option == 1:
        main_menu_methods.option1() # Add a publisher
    elif option == 2:
        main_menu_methods.option2() # Add a book
    elif option == 3:               # Edit a book
        ISBN = input("Enter ISBN of the book you want to edit: ")

        # Checking if the book doesn't exists:
        if collection_book.count_documents({ "ISBN": ISBN }) == 0:
            print("Error: Book doesn't exists with that ISBN! Returning back to the main menu.")
            return

        # Checking if the book ISBN input is null or empty string:
        if (ISBN.lower() == "null" or ISBN == ""):
            print("Error: Empty Input of ISBN! Returning back to the Main menu.")
            return

        # Loop for keep editing on the same book
        # until specified to go back to the main menu
        while(True):
            print_edit_menu()
            option = ''
            try:
                option = int(input('Enter your choice: '))
                ISBN = main_menu_methods.option3(option, ISBN)
            
                if option == 7:
                    break
            except KeyboardInterrupt:
                print('Interrupted')
                sys.exit(0)
            except:
                print('Wrong input or constraints were violated! Try Again')
                print("Please enter a number 1-7")

    elif option == 4: # Delete Book
        # Loop for keep deleting books
        # until specified to go back to the main menu
        while(True):
            print_delete_menu()
            option = ''
        
            # Delete a book
            try:
                option = int(input('Enter your choice: '))
                # Delete a book
                main_menu_methods.option4(option) 
                if option == 3:
                    break
            except KeyboardInterrupt:
                print('Interrupted')
            except:
                print('Wrong input or constraints were violated! Try Again')
                print("Please enter a number 1-3")

    elif option == 5: # Search book
        while(True):
            print_search_menu()
            option = ''

            try:
                option = int(input('Enter your choice: '))
                # Search a book
                main_menu_methods.option5(option) 
                if option == 6:
                    break
            except KeyboardInterrupt:
                print('Interrupted')
            except:
                print('Wrong input or constraints were violated! Try Again')
                print("Please enter a number 1-6")

    elif option == 6:
        # Exit
        print('Thanks your for using our database services! Bye\n')
        return None
    else:
        print('Invalid option. Please enter a number between 1 and 6.')

# Main method
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''

        try:
            option = int(input('Enter your choice: '))
            checkOptions(option)
            if option == 6:
                break
        except KeyboardInterrupt:
            print('Interrupted')
            sys.exit(0)
        except:
            print('Wrong input or constraints were violated! Try Again')
            print("Please enter a number 1-6")











