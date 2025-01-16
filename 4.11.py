class C:
    def __init__(self, sectors):
        self.sectors = sectors.copy()

    def m1(self, s: str, n: int):
        """Change the number of fans in a sector or add a new sector.

        :param s: Sector letter
        :param n: Number of fans
        """
        self.sectors[s] = n

    def m2(self, s: str):
        """
        Calculate the sum of fans in the specified sectors.

        :param s: String of sector letters
        :return: Total number of fans in the specified sectors
        """
        return sum(self.sectors.get(sector, 0) for sector in s)


# Test cases
def main():
    stadium = C({"A": 120, "D": 150, "G": 90, "K": 110})

    stadium.m1("G", 130)

    print("Fans in sectors GD:", stadium.m2("GD"))  # 280
    print("Fans in sectors KEJ:", stadium.m2("KEJ"))  # 110


if __name__ == "__main__":
    main()