class EBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.total_pages = pages
        self.current_page = 0  # Book is not opened yet
        self.is_open = False

    def open_book(self):
        self.is_open = True
        self.current_page = 1
        print(f"Book '{self.title}' is now open.")

    def close_book(self):
        self.is_open = False
        self.current_page = 0
        print(f"Book '{self.title}' is now closed.")

    def next_page(self):
        if not self.is_open:
            print("Cannot turn page. Book is closed.")
            return

        if self.current_page < self.total_pages:
            self.current_page += 1
            print(f"Turned to page {self.current_page}")
        else:
            print("You've reached the last page of the book.")

    def previous_page(self):
        if not self.is_open:
            print("Cannot turn page. Book is closed.")
            return

        if self.current_page > 1:
            self.current_page -= 1
            print(f"Turned to page {self.current_page}")
        else:
            print("You're already on the first page.")

    def display_status(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Total Pages: {self.total_pages}")

        if self.is_open:
            print(f"Current Page: {self.current_page}")
            print("Book Status: Open")
        else:
            print("Book Status: Closed")