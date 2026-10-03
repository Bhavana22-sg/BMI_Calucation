
print("===================================")
print("          BMI CALCULATOR")
print("===================================")

try:
    # Get user input
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    # Check for invalid values
    if weight <= 0 or height <= 0:
        print("\nError: Weight and height must be greater than zero.")

    else:
        # Calculate BMI
        bmi = weight / (height * height)

        # Display BMI
        print("\nYour BMI is:", round(bmi, 2))

        # Determine BMI category
        if bmi < 20:
            category = "Underweight"
        elif bmi < 60:
            category = "Normal"
        elif bmi < 80:
            category = "Overweight"
        else:
            category = "Obese"

        # Display category
        print("BMI Category:", category)

except ValueError:
    print("\nError: Please enter numbers only.")

print("===================================")
