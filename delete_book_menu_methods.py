import book_dao

# Option 1 -> Delete book by ISBN
def option1(ISBN):
    book_dao.deleteBookByISBN(ISBN)

    # Display results
    print("The book was successfully deleted!")

# Option 2 -> Delete book by Title
def option2(title):
    book_dao.deleteBookByTitle(title)

    # Display results
    print("The book was successfully deleted!")