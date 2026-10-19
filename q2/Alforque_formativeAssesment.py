class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)


class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_of_pages = None
        self.set_number_of_pages(number_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_pages):
        if isinstance(number_pages, int) and number_pages > 0:
            self.__number_of_pages = number_pages
        else:
            print("The number of pages must be positive")

    def display_info(self):
        super().display_info()
        print("Number of Pages:", self.__number_of_pages)


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = None
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if isinstance(issue_number, int) and issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive")

    def display_info(self):
        super().display_info()
        print("Issue Number:", self.__issue_number)

pub1 = Publication(
    "Journal of Experimental Psychology",
    "Ratchiff, R. & Van Dongen, H."
)

pub2 = Publication(
    "Introduction to Programming",
    "John Smith"
)

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("Noli Me Tangere", "Jose Rizal", 480)

mag1 = Magazine("National Geographic", "Various Authors", 202)
mag2 = Magazine("Science Today", "Various Authors", 15)

print("Publication Information:")
pub1.display_info()

print("\nPublication Information:")
pub2.display_info()

print("\nBook Information:")
book1.display_info()

print("\nBook Information:")
book2.display_info()

print("\nMagazine Information:")
mag1.display_info()

print("\nMagazine Information:")
mag2.display_info()

print("\nTesting Validation:")
book1.set_number_of_pages(-310)
mag1.set_issue_number(0)

book2.set_number_of_pages(500)
mag2.set_issue_number(16)

print("\nUpdated Book Pages:", book2.get_number_of_pages())
print("Updated Magazine Issue:", mag2.get_issue_number())
