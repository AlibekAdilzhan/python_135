class Human:
    def __init__(self, name, surname, age, weight, height):
        self.h_name = name
        self.h_surname = surname
        self.age = age
        self.weight = weight
        self.height = height

    def get_weight(self):
        print(f"{self.h_name}'s weight is {self.weight} kg")

    def get_age_after_years(self, delta_age):
        x = self.age + delta_age
        print(f"age after {delta_age} years is {x}")


human_1 = Human("AAA", "BBB", 23, 70, 185)
human_2 = Human("CCC", "BBB", 26, 80, 189)

print(human_1.age)
human_1.get_age_after_years(40)