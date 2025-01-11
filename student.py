# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.major = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Wukong"
    student1.age = 20
    student1.major = "Art"
    student2.name = "Macaque"
    student2.age = 21
    student2.major = "Theater"
    student3.name = "Mei"
    student3.age = 19
    student3.major = "Sports"


    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, major: {student1.major}')
    print(f'{student2.name}, {student2.age} years old, major: {student2.major}')
    print(f'{student3.name}, {student3.age} years old, major: {student3.major}')


if __name__ == "__main__":
    main()