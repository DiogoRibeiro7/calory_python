# 
class Human:
    def __init__(self, name, age, weight, height, gender, body_fat_percentage, muscle_mass_percentage):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.body_fat_percentage = body_fat_percentage
        self.muscle_mass_percentage = muscle_mass_percentage
        self.calories_consumed = 0
        self.calories_burned = 0

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

        # Adjust calories based on body composition and muscle mass
        lean_mass_percentage = 100 - self.body_fat_percentage
        lean_mass_calories = calories * (lean_mass_percentage / 100)
        muscle_mass_calories = lean_mass_calories + (self.muscle_mass_percentage / 100) * self.weight * 13
        adjusted_calories = muscle_mass_calories

        return adjusted_calories

    def intake_calories(self, calories_intake):
        self.calories_consumed += calories_intake

    def burn_calories(self, calories_burned):
        self.calories_burned += calories_burned

    def calculate_fat_gain_loss(self):
        net_calories = self.calories_consumed - self.calories_burned
        fat_gain_loss = net_calories / 7700  # 7700 calories per kg of fat
        return fat_gain_loss


# Example usage
name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
gender = input("Enter your gender (male/female): ")
body_fat_percentage = float(input("Enter your body fat percentage: "))
muscle_mass_percentage = float(input("Enter your muscle mass percentage: "))
activity_level = input("Enter your activity level: ")

person = Human(name, age, weight, height, gender, body_fat_percentage, muscle_mass_percentage)
calories = person.calculate_calories(activity_level)
print(f"{person.name}, you need to consume {calories} calories per day.")

# Calorie intake simulation
