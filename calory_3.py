# 
import datetime

class Human:
    # ... (previous code remains the same) ...

    def calculate_calories_interval(self, activity_level, start_hour, end_hour):
        calories = self.calculate_calories(activity_level)
        total_hours = end_hour - start_hour
        interval_calories = calories * (total_hours / 24)
        return interval_calories

    def simulate_calorie_intake(self, activity_level):
        now = datetime.datetime.now()
        current_hour = now.hour
        total_calories_intake = 0

        # Calorie intake before 6pm
        if current_hour < 18:
            calories_intake = self.calculate_calories_interval(activity_level, 0, 18)
            total_calories_intake += calories_intake

        # Progressive decay after 6pm
        for hour in range(18, current_hour):
            calories_intake = self.calculate_calories_interval(activity_level, hour, hour + 1)
            decay_factor = 1 - ((hour - 18) / 6)  # Adjust decay factor based on the hour
            calories_intake *= decay_factor
            total_calories_intake += calories_intake

        return total_calories_intake


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

total_calories_intake = person.simulate_calorie_intake(activity_level)
print(f"{person.name}, your estimated calorie intake for today is {total_calories_intake} calories.")
