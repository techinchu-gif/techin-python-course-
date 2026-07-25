"""
Question 2: Currency Converter (20 points)

Write a program that converts between Thai Baht (THB) and US Dollars (USD).
Requirements:

Ask user to choose conversion direction (THB to USD or USD to THB)
Ask for the amount to convert
Use exchange rate: 1 USD = 35.5 THB
Display result with 2 decimal places
Show the calculation formula used
"""
rate = 35.5

print("1. THAI BAHT (THB) to US DOLLARS (USD)")
print("2. US DOLLARS (USD) to THAI BAHT (THB)")

choice = input("Choose option: ")

if choice == "1":
    Amount = float(input("Enter amount in THB:"))
    USD = Amount / rate
    print(f"USD = {USD:.2f} USD") 

elif choice == "2":
    Amount = float(input("Enter amount in USD:"))
    THB = Amount * rate
    print(f"THB = {THB:.2f} THB")