# BMI Calculator with Enhanced Features by Shawn Litt
# I worked on this project as a way to practice what I learned while studying python on my own.
# As a collegiate student-athlete, my body composition was always overweight in normal BMI calculators.
# Therefore, I wanted to create a BMI calculator that would take into account body fat percentage.
# This could estimate whether the higher BMI was due to muscle mass or excess fat.
# I also incorporated both imperial and metric units since I am originally from a country that uses metric units.


import csv
import datetime

print("Welcome to the Enhanced BMI Calculator!")
while True:
    print("\n--- New BMI Calculation ---") 
    # Input loop for unit selection
    selected_units = "" 
    print("Please choose your preferred units for the calculation:")
    print("1. Imperial (pounds and inches)")
    print("2. Metric (kilograms and meters)")
    while True:
        unit_choice_str = input("Choose units (Imperial/Metric): ").strip().lower()
        if unit_choice_str in ['imperial', 'metric']:
            selected_units = unit_choice_str
            break
        else:
            print("Invalid choice. Please enter 'Imperial' or 'Metric'.")

    # Input loop for selected unit
    if selected_units == 'imperial':
        while True:
            try:
                weight_str = input("Enter your weight (in pounds): ")
                weight_lbs = float(weight_str)
                if weight_lbs <= 0:
                    print("Weight must be a positive value. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numerical value for weight.")

        while True:
            try:
                height_str = input("Enter your height (in inches): ")
                height_inches = float(height_str)
                if height_inches <= 0:
                    print("Height cannot be zero or negative. Please enter a valid height.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numerical value for height.")

        # These inputs are shared between both unit systems
        while True:
            gender = input("Enter your gender (M/F/Other): ").strip().lower()
            if gender in ['m', 'f', 'male', 'female', 'other']:
                if gender == 'm':
                    gender = 'male'
                elif gender == 'f':
                    gender = 'female'
                break
            else:
                print("Invalid gender. Please enter 'M', 'F', or 'Other'.")

        while True:
            try:
                age_str = input("Enter your age (in years): ")
                age = int(age_str)
                if age <= 0:
                    print("Age must be a positive value. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a whole number for age.")

        while True:
            try:
                body_fat_str = input("Enter your estimated body fat percentage (e.g., 12.0): ")
                body_fat_percentage = float(body_fat_str)
                if body_fat_percentage < 0 or body_fat_percentage > 100:
                    print("Body fat percentage must be between 0 and 100. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numerical value for body fat percentage.")

        # Imperial BMI Calculation
        bmi = (weight_lbs / (height_inches ** 2)) * 703
        print(f"\nYour BMI is: {bmi:.2f}")

        # Imperial Summary String
        weight_display = f"{weight_lbs} lbs"
        height_display = f"{height_inches} inches"


    elif selected_units == 'metric':
        # Loop for Metric Inputs
        while True:
            try:
                weight_str = input("Enter your weight (in kilograms): ")
                weight_kg = float(weight_str)
                if weight_kg <= 0:
                    print("Weight must be a positive value. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numerical value for weight.")

        while True:
            try:
                height_str = input("Enter your height (in centimeters): ")
                height_cm = float(height_str)
                if height_cm <= 0:
                    print("Height cannot be zero or negative. Please enter a valid height.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numerical value for height.")

        # These inputs are shared between both unit systems as said prior
        while True:
            gender = input("Enter your gender (M/F/Other): ").strip().lower()
            if gender in ['m', 'f', 'male', 'female', 'other']:
                if gender == 'm':
                    gender = 'male'
                elif gender == 'f':
                    gender = 'female'
                break
            else:
                print("Invalid gender. Please enter 'M', 'F', or 'Other'.")

        while True:
            try:
                age_str = input("Enter your age (in years): ")
                age = int(age_str)
                if age <= 0:
                    print("Age must be a positive value. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a whole number for age.")

        while True:
            try:
                body_fat_str = input("Enter your estimated body fat percentage (e.g., 12.0): ")
                body_fat_percentage = float(body_fat_str)
                if body_fat_percentage < 0 or body_fat_percentage > 100:
                    print("Body fat percentage must be between 0 and 100. Please try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a numerical value for body fat percentage.")

        # Metric BMI Calculation
        height_m = height_cm / 100 # Convert cm to meters for calculation
        bmi = weight_kg / (height_m ** 2)
        print(f"\nYour BMI is: {bmi:.2f}")

        # Metric Summary String
        weight_display = f"{weight_kg} kg"
        height_display = f"{height_cm} cm"


    # General BMI Categories
    print("BMI Category: ")
    category = ""

    if bmi < 18.5:
        print("Underweight")
        category = "Underweight"
    elif 18.5 <= bmi <= 24.9:
        print("Normal weight")
        category = "Normal weight"
    elif 25 <= bmi <= 29.9:
        print("Overweight")
        category = "Overweight"
    else:
        print("Obese")
        category = "Obese"

    # Body Compostion Insight
    print("\n--- Body Composition Insight ---")

    if gender == 'male':
        lean_bf_max = 18.0
        avg_bf_max = 24.0
        high_bf_min = 25.0
    elif gender == "female":
        lean_bf_max = 25.0
        avg_bf_max = 31.0
        high_bf_min = 32.0
    else:
        lean_bf_max = 20.0
        avg_bf_max = 28.0
        high_bf_min = 29.0
        print("Note: Gender-specific body fat interpretation may not be as accurate for 'Other' or unrecognized gender.")

    if (category == "Overweight" or category == "Obese") and body_fat_percentage <= lean_bf_max:
        print("Given your BMI and body fat percentage, your higher BMI is "
              "likely due to more muscle mass than fat. "
              "If that is the case, great job! "
              "This is common for atheletes or those with a muscular build."
              "Keep in mind BMI may not accurately reflect your body composition.")
    elif category == "Normal weight" and body_fat_percentage >= high_bf_min:
        print(" Your BMI is in the normal range, however your body fat percentage is high. " 
              "This suggests a higher fat-to-muscle ratio, putting you in the skinny fat category."
              "Strength training and a balanced diet can help even things out."
              " Keep in mind BMI may not accurately reflect your body composition.")
    elif category == "Normal weight" and body_fat_percentage <= avg_bf_max:
        print("Great job maintaining a balanced physique. Keep in mind BMI may not accurately reflect body composition.")
    else:
        print("Your body composition is generally aligned with your BMI category"
              " or requires more specific interpretation based on other factors.")

    # CSV Storage of results
    csv_filename = "bmi_records.csv"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Using CSV to show stored data
    data_row = [
        timestamp,
        weight_display, 
        height_display, 
        gender,
        age,
        body_fat_percentage,
        bmi,
        category,
        selected_units 
    ]

    header_row = [
        "Timestamp", "Weight", "Height", "Gender", "Age", "Body_Fat_Percentage",
        "BMI_Value", "BMI_Category", "Units_Used"
    ]

    with open(csv_filename, 'a', newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(header_row)
        writer.writerow(data_row)
    print(f"\nYour BMI record has been saved to '{csv_filename}'.")


    # Final Summary for both units
    print(f"\n--- Summary ---")
    print(f"You entered: {weight_display} and {height_display}.")
    print(f"Additional info: Gender - {gender}, Age - {age}, Body Fat - {body_fat_percentage:.1f}%.")
    print(f"Your BMI is {bmi:.2f}, which is categorized as {category}.")
    print(f"Units used for this calculation: {selected_units.capitalize()}.") # Capitalize for nice display

    # Ask for another calculation
    while True:
        try_again = input("\nDo you want to perform another BMI calculation? (yes/no): ").strip().lower()
        if try_again in ['yes', 'no', 'y', 'n']:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if try_again in ['no', 'n']:
        print("\nThank you for using the Enhanced BMI Calculator!")
        print("If you would like more info on BMI, check the CDC website.")
        print("https://www.cdc.gov/healthyweight/assessing/bmi/index.html")
        print("Goodbye!")
        break