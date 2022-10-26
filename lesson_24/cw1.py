class Dog:
    def __init__(self, name, age, type, color):
        self.dog_name = name
        self.dog_age = age
        self.dog_type = type
        self.color = color

    def get_age(self):
        print(f"{self.dog_name}'s age is {self.dog_age}")


dog_1 = Dog("Jack", 4, "labrador", "black")

dog_1.get_age()
