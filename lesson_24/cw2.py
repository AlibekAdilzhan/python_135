class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def get_name(self):
        print(f"Person's name is {self.name}")

    def get_age(self):
        print(f"{self.name}'s age is {self.age}")


class Student(Person):
    def __init__(self, name, age, weight, height, university):
        super().__init__(name, age, weight, height)
        self.university = university

    def get_university(self):
        print(f"{self.name}'s university is {self.university}")


person_1 = Person("Asan", 29, 65, 190)
student_1 = Student("Temir", 19, 62, 185, "AITU")

student_1.get_university()

print(issubclass(int, Person))