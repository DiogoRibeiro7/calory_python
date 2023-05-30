# 
class Human:
    def __init__(self, name, age, weight, height, gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender

    def calculate_bmr(self):
        if self.gender.lower() == "male":
            bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        elif self.gender.lower() == "female":
            bmr = 655 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)
        else:
            raise ValueError("Invalid gender. Please specify 'male' or 'female'.")
        return bmr

    def calculate_calories(self, activity_level):
        bmr = self.calculate_bmr()
        if activity_level == "sedentary":
            calories = bmr * 1.2
        elif activity_level == "lightly active":
            calories = bmr * 1.375
        elif activity_level == "moderately active":
            calories = bmr * 1.55
        elif activity_level == "very active":
            calories = bmr * 1.725
        elif activity_level == "super active":
            calories = bmr * 1.9
        else:
            raise ValueError("Invalid activity level. Please choose from 'sedentary', 'lightly active', 'moderately active', 'very active', or 'super active'.")
        return calories


# Example usage
name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
gender = input("Enter your gender (male/female): ")
activity_level = input("Enter your activity level: ")

person = Human(name, age, weight, height, gender)
calories = person.calculate_calories(activity_level)
print(f"{person.name}, you need to consume {calories} calories per day.")
