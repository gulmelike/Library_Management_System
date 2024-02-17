class Library:
    def __init__(self, file_path="books.txt"):
        self.file_path = file_path
        self.file = open(self.file_path, "a+")

    def __del__(self):
        if self.file:
            self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()

        if not lines:
            print("No books found in the library.")
            return

        print("List of books:")
        for line in lines:
            book_details = line.split(',')
            if len(book_details) == 4:
                book_title, book_author, release_date, num_pages = book_details
                print(f"Title: {book_title}, Author: {book_author}")

    def add_book(self):
        book_title = input("Enter book title: ")
        book_author = input("Enter book author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{book_title},{book_author},{release_date},{num_pages}\n"

        self.file.write(book_info)
        print("Book added successfully!")

    def remove_book(self):
        book_title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0)
        lines = self.file.read().splitlines()
        books_list = [line for line in lines if line.startswith(book_title_to_remove)]

        if not books_list:
            print(f"Book with title '{book_title_to_remove}' not found.")
            return

        index_to_remove = lines.index(books_list[0])
        lines.pop(index_to_remove)

        self.file.truncate(0)
        self.file.seek(0)
        self.file.write('\n'.join(lines))
        print(f"Book '{book_title_to_remove}' removed successfully!")


lib = Library()

while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")

    choice = input("Enter your choice (1-3, or q to Quit): ")


    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice.lower() == 'q':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3, or q to Quit.")
