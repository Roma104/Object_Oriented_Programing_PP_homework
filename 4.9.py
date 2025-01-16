class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        name_initial = self.name[0]

        if self.age >= 18:
            return f"{self.surname.upper()}{name_initial.upper()}{self.seniority}"
        else:
            return f"{self.surname.lower()}{name_initial.lower()}{self.seniority}"


# Test cases
def main():
    # test case 1: kid
    emp1 = C("Anna", "May", 17, 7)
    print(str(emp1))

    # test case 2: adult
    emp2 = C("George", "Brown", 21, 4)
    print(str(emp2))


if __name__ == "__main__":
    main()