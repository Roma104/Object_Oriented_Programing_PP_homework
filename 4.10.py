class C:
    def __init__(self, coordinates: list):
        self.coordinates = coordinates

    def m(self, n):
        """
        Check if at least n points are in the first quadrant.
        First quadrant is defined as points where both x and y are > 0.
        """
        first_quadrant_points = sum(1 for x, y in self.coordinates if x > 0 and y > 0)

        return first_quadrant_points >= n


def main():
    points = C([[2, 3], [1, 8], [-6, 4], [3, -7]])

    print(points.m(2))  # True
    print(points.m(3))  # False


if __name__ == "__main__":
    main()