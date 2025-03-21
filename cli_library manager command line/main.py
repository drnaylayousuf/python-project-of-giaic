import os
import json
import pyfiglet
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Library class to manage the book collection
class PersonalLibrary:
    def __init__(self):
        self.library = []
        self.load_library()

    def load_library(self):
        """Load library data from a file."""
        if os.path.exists("library.json"):
            with open("library.json", "r") as file:
                self.library = json.load(file)

    def save_library(self):
        """Save library data to a file."""
        with open("library.json", "w") as file:
            json.dump(self.library, file)

    def add_book(self):
        """Add a new book to the library."""
        title = input(Fore.YELLOW + "📚 Enter the book title: ")
        author = input(Fore.CYAN + "✍️ Enter the author: ")
        year = int(input(Fore.GREEN + "📅 Enter the publication year: "))
        genre = input(Fore.MAGENTA + "🎭 Enter the genre: ")
        read_status = input(Fore.BLUE + "📖 Have you read this book? (yes/no): ").strip().lower()
        read_status = True if read_status == "yes" else False

        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read_status": read_status
        }

        self.library.append(book)
        print(Fore.GREEN + "✅ Book added successfully!")

    def remove_book(self):
        """Remove a book from the library."""
        title = input(Fore.RED + "❌ Enter the title of the book to remove: ")
        for book in self.library:
            if book["title"].lower() == title.lower():
                self.library.remove(book)
                print(Fore.GREEN + "✅ Book removed successfully!")
                return
        print(Fore.YELLOW + "❗ Book not found!")

    def search_book(self):
        """Search for a book by title or author."""
        print("🔍 Search by: ")
        print(Fore.CYAN + "1. Title 📖")
        print(Fore.MAGENTA + "2. Author ✍️")
        choice = input(Fore.YELLOW + "Enter your choice: ")

        if choice == "1":
            title = input(Fore.GREEN + "📖 Enter the title: ")
            results = [book for book in self.library if title.lower() in book["title"].lower()]
        elif choice == "2":
            author = input(Fore.GREEN + "✍️ Enter the author: ")
            results = [book for book in self.library if author.lower() in book["author"].lower()]
        else:
            print(Fore.RED + "❗ Invalid choice!")
            return

        if results:
            print("🔎 Matching Books:")
            for idx, book in enumerate(results, 1):
                status = "✅ Read" if book["read_status"] else "❌ Unread"
                print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        else:
            print(Fore.YELLOW + "❗ No matching books found.")

    def display_books(self):
        """Display all books in the library."""
        if not self.library:
            print(Fore.YELLOW + "❗ Your library is empty.")
            return
        print("📚 Your Library:")
        for idx, book in enumerate(self.library, 1):
            status = "✅ Read" if book["read_status"] else "❌ Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

    def display_statistics(self):
        """Display library statistics."""
        total_books = len(self.library)
        read_books = sum(1 for book in self.library if book["read_status"])
        percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
        print(Fore.CYAN + f"📊 Total books: {total_books}")
        print(Fore.MAGENTA + f"📈 Percentage read: {percentage_read:.2f}%")

# Main function to handle menu and user interaction
def main():
    library = PersonalLibrary()

    # Artistic starting design using pyfiglet for the welcome message
    welcome_message = pyfiglet.figlet_format("Welcome to the Library!")
    print(Fore.CYAN + Style.BRIGHT + welcome_message)

    while True:
        print("\n📚 Menu")
        
        # Colorized welcome message
        print(Fore.CYAN + Style.BRIGHT + "Personal Library Manager 😊")

        # Menu options with different colors for each option
        print( "1. Add a book 📖")
        print( "2. Remove a book ❌")
        print( "3. Search for a book 🔍")
        print( "4. Display all books 📚")
        print( "5. Display statistics 📊")
        print( "6. Exit 🚪")
        choice = input(Fore.YELLOW + "Enter your choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.remove_book()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            library.display_books()
        elif choice == "5":
            library.display_statistics()
        elif choice == "6":
            library.save_library()

            # Artistic ending design using pyfiglet for the exit message
            goodbye_message = pyfiglet.figlet_format("Goodbye!")
            print(Fore.CYAN + Style.BRIGHT + goodbye_message)
            print(Fore.CYAN + "💾 Library saved to file. See you next time! 👋")
            break
        else:
            print(Fore.RED + "❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
