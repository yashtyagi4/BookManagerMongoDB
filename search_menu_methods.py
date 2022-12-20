import book_dao

# Display all the books
def search_all_books():
    results = list(book_dao.findAll())

    # Display results
    if (len(results) != 0):
        print("The following are the ISBNs and titles of all books: ")
        for item in results:
            print(item['ISBN'], item['title'])
        print("The end of books.")
    else:
        print("No Books Exist")

# Display books by their title
def search_by_title():
    # Query Info Input
    title = input("Enter the exact title of the book: ")

    results = list(book_dao.findByTitle(title))

    # Display results
    if (len(results) != 0):
        print("The following are the ISBNs and titles of all books: ")
        for item in results:
            print(item['ISBN'], item['title'])
        print("The end of books.")
    else:
        print("No Books Exist with that title.")

# Display books by their Publisher
def search_by_publisher():
    # Query Info Input
    publisher_name = input("Enter Publisher of the book: ")

    results = list(book_dao.findByPublisher(publisher_name))

    # Display results
    if (len(results) != 0):
        print("The following are the ISBNs and titles of all books: ")
        for item in results:
            print(item['ISBN'], item['title'])
        print("The end of books.")
    else:
        print("No Books Exist with that Publisher Name.")

# Display books by a price range
def search_by_price_range():
    # Query Info Input
    min = float(input("Enter minimum Price: "))
    max = float(input("Enter maximum Price: "))
    
    results = book_dao.findByPriceRange(min, max)

    # Display results
    if (len(results) != 0):
        print("The following are the ISBNs and titles of all books: ")
        for item in results:
            print(item['ISBN'], item['title'])
        print("The end of books.")
    else:
        print("No Books Exist within that price range.")

# Display books by the title and publisher
def search_by_title_publisher():
    # Query Info Input
    title = input("Enter Title of the book: ")
    publisher_name = input("Enter Publisher name of the book: ")

    results = list(book_dao.findByTitlePublisher(title, publisher_name))

    # Display results
    if (len(results) != 0):
        print("The following are the ISBNs and titles of all books: ")
        for item in results:
            print(item['ISBN'], item['title'])
        print("The end of books.")
    else:
        print("No Books Exist with that Title and Publisher name")