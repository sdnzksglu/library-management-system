class Library:
    def __init__(self):
        self.file_name = "books.txt"
        self.file = open("books.txt", "r")
        self.book_info = {}

    def add_book(self):
        def define_book_title():
            book_title = input("Enter the title of the book you want to add: ")
            print("Saved ✅", book_title)
            self.book_info["book title"] = book_title

        def define_the_author():
            the_author = input("Enter the author of the book you want to add: ")
            print("Author:", the_author, "Saved ✅")
            self.book_info["author"] = the_author

        def define_release_date():
            while True:
                release_date = input("Enter the publication year of the book you want to add: ")
                if len(release_date) == 4:
                    print("Publication year", release_date, "Saved ✅")
                    self.book_info["publication year"] = release_date
                    break
                else:
                    print("Invalid date, couldn't be saved ❎")

        def define_the_page():
            page_num = input("Enter the number of pages of the book you want to add: ")
            print("Number of pages", page_num, "Saved ✅")
            self.book_info["number of pages"] = page_num

        define_book_title()
        define_the_author()
        define_release_date()
        define_the_page()

        with open(self.file_name, "a") as file:
            file.write(f"{self.book_info['book title']}, {self.book_info['author']}, {self.book_info['publication year']}, {self.book_info['number of pages']}\n")

    def close(self):
        self.file.close()

    def list_books(self):
        with open(self.file_name, "r") as file:
            books = file.readlines()
            for book in books:
                book_info = book.strip().split(", ")
                print(f"Book Title: {book_info[0]}, Author: {book_info[1]}")

    def remove_book(self):
        book_to_remove = input("Enter the name of the book you want to remove from the library: ")
        book_found = False

        with open(self.file_name, "r") as file:
            lines = file.readlines()
        with open(self.file_name, "w") as file:
            for line in lines:
                book_info = line.strip().split(", ")
                if book_to_remove == book_info[0]:
                    book_found = True
                else:
                    file.write(line)

        if book_found:
            print(f"'{book_to_remove}' has been successfully removed.")
        else:
            print(f"'{book_to_remove}' not found in the library.")

def menu():
    lib = Library()
    while True:
        print("\n -----MENU-----\n")
        print("1-List books")
        print("2-Add book")
        print("3-Remove book")
        print("q-Log out\n")
        choice = input("Select the appropriate action from the menu: ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice.lower() == "q":
            lib.close()
            print("Logging out")
            break
        else:
            print("Invalid option, please try again")

if __name__ == "__main__":
    menu()
