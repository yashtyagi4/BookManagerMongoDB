from pymongo_connector import collection_book
from pymongo_connector import collection_publisher

# ---------------- Main Menu Options ------------------

# 1. ---------------- Add a Publisher -----------------

def insertPublisher(name, phone, city):
    # Checking if the publisher already exists:
    if collection_publisher.count_documents({ 'name': name }) > 0:
        print("Error: Publisher already exists with that name! Returning back to the main menu.")
        return

    # Fixing the null cases
    if (name.lower() == "null" or name == "" ):
        print("Error: Publisher name can't be null.")
        return
    if (phone.lower() == "null" or phone == ""):
        phone = None
    if (city.lower() == "null" or city == ""):
        city = None

    collection_publisher.insert_one({"name": name, "phone": phone, "city": city})

    # Display results
    print("Publisher was successfully added to the database")

# 2. ------------------- Add a Book -------------------

def insertBook(ISBN, title, year, published_by, previous_edition, price):
    # Checking if the book already exists:
    if collection_book.count_documents({ "ISBN": ISBN }) > 0:
        print("Error: Book already exists with that ISBN! Returning back to the main menu.")
        return

    # Fixing the null cases
    if (ISBN.lower() == "null" or ISBN == "" ):
        print("Error: Book ISBN name can't be null.")
        return
    if (title.lower() == "null" or title == ""):
        title = None
    if (year.lower()  == "null" or year == ""):
        year = None
    if (published_by.lower() == "null" or published_by == ""):
        published_by = None
    if (previous_edition.lower() == "null" or previous_edition == ""):
        previous_edition = None
    if (price.lower() == "null" or price == ""):
        price = None

    collection_book.insert_one({"ISBN": ISBN, "title": title, "year": year, "published_by": published_by, "previous_edition": previous_edition, "price": float(price)})

    # Display results
    print("Book was successfully added to the database")

# 3. ------------------- Edit a Book -------------------

# 3. 1. Change ISBN of a Book
def editBookISBN(oldISBN, newISBN):
    # Checking if the new ISBN already exists:
    if collection_book.count_documents({ "ISBN": newISBN }) > 0:
        print("Error: Book already exists with that ISBN! Returning back to the main menu.")
        return

    # Fixing the null case
    if (newISBN.lower() == "null" or newISBN == ""):
        newISBN = None

    collection_book.update_one(
        { "ISBN" : oldISBN },
        {
            "$set": { "ISBN": newISBN },
            # "$currentDate": {"lastModified": True}
        }
    )

    # Return results
    return newISBN

# 3. 2. Change Title of a Book
def editBookTitle(ISBN, title):

    # Fixing the null case
    if (title.lower() == "null" or title == ""):
        title = None

    collection_book.update_one(
        { "ISBN" : ISBN },
        {
            "$set": { "title": title },
            # "$currentDate": {"lastModified": True}
        }
    )

# 3. 3. Change Year of a Book
def editBookYear(ISBN, year):

    # Fixing the null case
    if (year.lower() == "null" or year == ""):
        year = None

    collection_book.update_one(
        { "ISBN" : ISBN },
        {
            "$set": { "year": year },
            # "$currentDate": {"lastModified": True}
        }
    )

# 3. 4. Change Publisher of a Book
def editBookPublisher(ISBN, publisher):

    # Fixing the null case
    if (publisher.lower() == "null" or publisher == ""):
        publisher = None


    collection_book.update_one(
        { "ISBN" : ISBN },
        {
            "$set": { "published_by": publisher },
            # "$currentDate": {"lastModified": True}
        }
    )

# 3. 5. Change Previous Edition of a Book
def editBookPreviousEdition(ISBN, previous_edition):

    # Fixing the null case
    if (previous_edition.lower() == "null" or previous_edition == ""):
        previous_edition = None
    
    collection_book.update_one(
        { "ISBN" : ISBN },
        {
            "$set": { "previous_edition": previous_edition },
            # "$currentDate": {"lastModified": True}
        }
    )

# 3. 6. Change Price of a Book
def editBookPrice(ISBN, price):

    # Fixing the null case
    if (price == "null" or price == ""):
        price = None    

    collection_book.update_one(
        { "ISBN" : ISBN },
        {
            "$set": { "price": float(price) },
            # "$currentDate": {"lastModified": True}
        }
    )

# 4. ---------------- Delete a Book ------------------

# 4. 1. Delete book by its ISBN
def deleteBookByISBN(ISBN):
    collection_book.delete_one({"ISBN": ISBN})

# 4. 2. Delete book by its Title
def deleteBookByTitle(title):
    collection_book.delete_one({"title": title})

# 5. -------------- Search Menu Options --------------

# 5. 1. Search all books
def findAll():
    results = collection_book.find()
    return results

# 5. 2. Search books based on title
def findByTitle(book_title):
    results = collection_book.find({'title': book_title})
    return results

# 5. 3. Search book by its publisher name
def findByPublisher(publisher_name):
    results = collection_book.find({'published_by': publisher_name})
    return results

# 5. 4. Search books based on a price range
def findByPriceRange(min, max):
    results = collection_book.find({'price' : {'$gte' : min, '$lte' : max}})
    return list(results)

# 5. 5. Search books based on title and publisher
def findByTitlePublisher(book_title, publisher_name):
    results = collection_book.find({"$and": [{"title": book_title}, {"published_by": publisher_name}]})
    return results