import book_dao

# Option 1 -> Change ISBN of the book
def option1(oldISBN):
    # Query Info Input
    newISBN = input("Enter the new ISBN of the book: ")

    if (newISBN.lower() == "null" or newISBN == ""):
        print("Error: New ISBN can't be null!")
        return

    book_dao.editBookISBN(oldISBN, newISBN)

    # Display results
    print("The book's ISBN was successfully updated!")
    return newISBN

# Option 2 -> Change Title of the book
def option2(ISBN):
    # Query Info Input
    title = input("Enter the new Title of the book: ")

    book_dao.editBookTitle(ISBN, title)

    # Display results
    print("The book's title was successfully updated!")

# Option 3 -> Change Year of the book
def option3(ISBN):
    # Query Info Input
    year = input("Enter the new Year of the book: ")

    book_dao.editBookYear(ISBN, year)

    # Display results
    print("The book's year was successfully updated!")

# Option 4 -> Change Publisher of the book
def option4(ISBN):
    # Query Info Input
    publisher = input("Enter the new Publisher Name of the book: ")

    book_dao.editBookPublisher(ISBN, publisher)

    # Display results
    print("The book's publisher was successfully updated!")

# Option 5 -> Change Previous Edition of the book
def option5(ISBN):
    # Query Info Input
    previous_edition = input("Enter the new Previous Edition ISBN of the book: ")

    book_dao.editBookPreviousEdition(ISBN, previous_edition)

    # Display results
    print("The book's previous edition was successfully updated!")

# Option 6 -> Change Price of the book
def option6(ISBN):
    # Query Info Input
    price = input("Enter the new Price of the book: ")

    book_dao.editBookPrice(ISBN, price)

    # Display results
    print("The book's price was successfully updated!")