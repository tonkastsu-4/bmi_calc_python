import csv
import datetime

# --- Functions for getting user input ---

def get_units():
    """Asks the user to select a unit system and validates the input."""
    while True:
        unit_choice = input("Choose units (Imperial/Metric): ").strip().lower()
        if unit_choice in ['imperial', 'metric']:
            return unit_choice
        else:
            print("Invalid choice. Please enter 'Imperial' or 'Metric'.")

def get_weight(units):
    """Prompts for and validates weight input based on the unit system."""
    while True:
        unit_text = "pounds" if units == 'imperial' else "kilograms"
        try:
            weight_str = input(f"Enter your weight (in {unit_text}): ")
            weight = float(weight_str)
            if weight <= 0:
                print("Weight must be a positive value. Please try again.")
            else:
                return weight
        except ValueError:
            print(f"Invalid input. Please enter a numerical value for weight.")

def get_height(units):
    """Prompts for and validates height input based on the unit system."""
    while True:
        unit_text = "inches" if units == 'imperial' else "centimeters"
        try:
            height_str = input(f"Enter your height (in {unit_text}): ")
            height = float(height_str)
            if height <= 0:
                print("Height cannot be zero or negative. Please enter a valid height.")
            else:
                return height
        except ValueError:
            print(f"Invalid input. Please enter a numerical value for height.")

def get_gender():
    """Prompts for and validates gender input."""
    while True:
        gender = input("Enter your gender (M/F/Other): ").strip().lower()
        if gender in ['m', 'f', 'male', 'female', 'other']:
            if gender == 'm':
                return 'male'
            elif gender == 'f':
                return 'female'
            else:
                return gender
        else:
            print("Invalid gender. Please enter 'M', 'F', or 'Other'.")

def get_age():
    """Prompts for and validates age input."""
    while True:
        try:
            age_str = input("Enter your age (in years): ")
            age = int(age_str)
            if age <= 0:
                print("Age must be a positive value. Please try again.")
            else:
                return age
        except ValueError:
            print("Invalid input. Please enter a whole number for age.")

def get_body_fat():
    """Prompts for and validates body fat percentage input."""
    while True:
        try:
            body_fat_str = input("Enter your estimated body fat percentage (e.g., 12.0): ")
            body_fat_percentage = float(body_fat_str)
            if body_fat_percentage < 0 or body_fat_percentage > 100:
                print("Body fat percentage must be between 0 and 100. Please try again.")
            else:
                return body_fat_percentage
        except ValueError:
            print("Invalid input. Please enter a numerical value for body fat percentage.")

# --- Functions for calculation and logic ---

def calculate_bmi(weight, height, units):
    """Calculates BMI based on units and returns the value."""
    if units == 'imperial':
        return (weight / (height ** 2)) * 703
    else: # Metric
        height_m = height / 100 # Convert cm to meters
        return weight / (height_m ** 2)

def categorize_bmi(bmi):
    """Returns the standard BMI category for a given BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Normal weight"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_enhanced_insight(gender, category, body_fat_percentage):
    """Generates a detailed body composition insight based on inputs."""
    if gender == 'male':
        lean_bf_max, avg_bf_max, high_bf_min = 18.0, 24.0, 25.0
    elif gender == "female":
        lean_bf_max, avg_bf_max, high_bf_min = 25.0, 31.0, 32.0
    else:
        lean_bf_max, avg_bf_max, high_bf_min = 20.0, 28.0, 29.0
        print("Note: Gender-specific body fat interpretation may not be as accurate for 'Other' or unrecognized gender.")

    if (category == "Overweight" or category == "Obese") and body_fat_percentage <= lean_bf_max:
        return ("Given your BMI and body fat percentage, your higher BMI is "
                "likely due to a higher amount of muscle mass than excess fat. "
                "Keep in mind BMI may not accurately reflect your body composition.")
    elif category == "Normal weight" and body_fat_percentage >= high_bf_min:
        return ("While your BMI is in the normal range, your body fat percentage suggests a higher fat-to-muscle ratio. "
                "You may be in the skinny fat category. Focusing on strength training and diet could help."
                " Keep in mind BMI may not accurately reflect your body composition.")
    elif category == "Normal weight" and body_fat_percentage <= avg_bf_max:
        return "Great job maintaining a balanced physique. Keep in mind BMI may not accurately reflect body composition."
    else:
        return ("Your body composition is generally aligned with your BMI category"
                " or requires more specific interpretation based on other factors.")

def save_record(record_data):
    """Appends a new record to the CSV file, creating a header if necessary."""
    csv_filename = "bmi_records.csv"
    header_row = [
        "Timestamp", "Weight", "Height", "Gender", "Age", "Body_Fat_Percentage",
        "BMI_Value", "BMI_Category", "Units_Used"
    ]
    try:
        with open(csv_filename, 'a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(header_row)
            writer.writerow(record_data)
        print(f"\nYour BMI record has been saved to '{csv_filename}'.")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

# --- Main program loop ---

def run_calculator():
    """This is the main function that orchestrates the entire BMI calculation process."""
    print("\n--- New BMI Calculation ---")
    
    # 1. Get all inputs from the user
    units = get_units()
    weight = get_weight(units)
    height = get_height(units)
    gender = get_gender()
    age = get_age()
    body_fat_percentage = get_body_fat()

    # 2. Perform calculations and get results
    bmi = calculate_bmi(weight, height, units)
    category = categorize_bmi(bmi)
    insight = get_enhanced_insight(gender, category, body_fat_percentage)

    # 3. Prepare display and CSV data
    weight_display = f"{weight} {'lbs' if units == 'imperial' else 'kg'}"
    height_display = f"{height} {'inches' if units == 'imperial' else 'cm'}"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data_row = [
        timestamp,
        weight_display,
        height_display,
        gender,
        age,
        body_fat_percentage,
        bmi,
        category,
        units
    ]

    # 4. Display results and save to CSV
    print(f"\nYour BMI is: {bmi:.2f}")
    print("BMI Category: ")
    print(f"  {category}")
    print("\n--- Body Composition Insight ---")
    print(insight)

    save_record(data_row)

    print(f"\n--- Summary ---")
    print(f"You entered: {weight_display} and {height_display}.")
    print(f"Additional info: Gender - {gender}, Age - {age}, Body Fat - {body_fat_percentage:.1f}%.")
    print(f"Your BMI is {bmi:.2f}, which is categorized as {category}.")
    print(f"Units used for this calculation: {units.capitalize()}.")

# --- Program entry point ---
if __name__ == "__main__":
    print("Welcome to the Enhanced BMI Calculator!")
    while True:
        run_calculator()
        while True:
            try_again = input("\nDo you want to perform another BMI calculation? (yes/no): ").strip().lower()
            if try_again in ['yes', 'no', 'y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        if try_again in ['no', 'n']:
            print("\nThank you for using the Enhanced BMI Calculator!")
            print("Please consult a healthcare professional for personalized advice.")
            print("Goodbye!")
            break


