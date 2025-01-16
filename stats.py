import statistics


class Statistics:
    def __init__(self, init_numbers=None):
        self.numbers = init_numbers

    def add_number(self, num):
        try:
            self.numbers.append(num)
            print(f"Number {num} added successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def display_numbers(self):
        print("Numbers:", " ".join(map(str, self.numbers)))

    def get_maximum(self):
        return max(self.numbers)

    def get_minimum(self):
        return min(self.numbers)

    def calculate_mean(self):
        return statistics.mean(self.numbers)

    def calculate_median(self):
        return statistics.median(self.numbers)

    def print_statistics(self):
        if not self.numbers:
            print("No numbers in the set.")
            return

        print("\nStatistical Quantities:")
        print(f"Minimum: {self.get_minimum()}")
        print(f"Maximum: {self.get_maximum()}")
        print(f"Arithmetic Mean: {self.calculate_mean()}")
        print(f"Median: {self.calculate_median()}")