from ebook import EBook


def main():
    my_book = EBook("Thinking fast and slow", "Daniel Kahneman", 480)

    print("Initial Book Status:")
    my_book.display_status()
    print()

    print("Book Status After Opening:")
    my_book.open_book()
    my_book.display_status()
    print()

    [my_book.next_page() for _ in range(15)]
    my_book.display_status()
    print()

    my_book.close_book()
    print()

    my_book.next_page()
    my_book.previous_page()


# Run the main program
if __name__ == "__main__":
    main()