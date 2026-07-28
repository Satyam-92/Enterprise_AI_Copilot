from database.analytics import (
    get_total_books,
    get_average_price,
    get_highest_priced_book,
    get_lowest_priced_book,
    get_books_by_rating,
    search_books,
)

print("=" * 50)
print("DATABASE ANALYTICS")
print("=" * 50)

print(f"Total Books: {get_total_books()}")
print(f"Average Price: {get_average_price()}")

print(f"Most Expensive Book: {get_highest_priced_book()}")
print(f"Cheapest Book: {get_lowest_priced_book()}")

print("\n" + "=" * 50)
print("FIVE STAR BOOKS")
print("=" * 50)

books = get_books_by_rating(5)

if books:
    for book in books:
        print(book)
else:
    print("No five-star books found.")

print("\n" + "=" * 50)
print("SEARCH RESULT: Travel")
print("=" * 50)

results = search_books("Travel")

if results:
    for book in results:
        print(book)
else:
    print("No books found.")