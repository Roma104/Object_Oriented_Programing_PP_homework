from stats import Statistics


def main():
    stats = Statistics(init_numbers=[12, 37, 6])

    while True:
        new_number = input('Add number to the set ("exit" to exit): ')
        if new_number != 'exit':
            stats.add_number(int(new_number))
        else:
            break

    stats.display_numbers()
    stats.print_statistics()
    

if __name__ == '__main__':
    main()