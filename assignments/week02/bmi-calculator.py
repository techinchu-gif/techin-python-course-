"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""
weight = float(input("Enter weight: (kg) "))
height = float(input("Enter height: (m) "))

BMI = weight / height ** 2

print("bmi_User = ", BMI)

if BMI < 18.5:
    print("Underweight")
elif 18.5 <= BMI <= 24.9:
    print("Normal weight")
elif 25.0 <= BMI <= 29.9:
    print("Overweight")
else:
    print("Obese")