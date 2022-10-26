class Dog:
    def __init__(self, name, age, type, color):
        self.dog_name = name
        self.dog_age = age
        self.dog_type = type
        self.color = color

    def get_age(self):
        print(f"{self.dog_name}'s age is {self.dog_age}")

    def get_name(self, owner):
        print(f"Dog's name is {self.dog_name}, his owner is {owner}")


dog_1 = Dog("Jack", 4, "labrador", "black")

dog_1.get_age()
dog_1.get_name("John")