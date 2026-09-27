# Example 1: Function with one parameter
def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Nice to meet you.")

print("Calling greet_person with different names:")
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")
print()

# Example 2: Function with multiple parameters
def introduce_person(name, age, city):
    """Introduces a person with their details"""
    print(f"Hi! My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I live in {city}.")
    print()

print("Calling introduce_person:")
introduce_person("Diana", 25, "New York")
introduce_person("Eve", 30, "Los Angeles")

# Example 3: Mathematical function
def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()
    print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)

calculate_rectangle_area(10, 7)
# Example 1: Function that returns a value
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result

print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()

# Example 2: Function returning multiple values
def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()

# =============================================================================
# PART 4: DEFAULT PARAMETERS
# =============================================================================
print("\n=== PART 4: DEFAULT PARAMETERS ===")
# Example 1: Function with default parameter
def greet_with_title(name, title="Mr./Ms."):
    """Greets person with optional title"""
    print(f"Hello, {title} {name}!")

print("Using default parameters:")
greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Custom title
greet_with_title("Brown", "Prof.")  # Custom title
print()

# Example 2: Multiple default parameters
def create_profile(name, age=18, country="Unknown"):
    """Creates a user profile with default values"""
    print(f"Profile: {name}, Age: {age}, Country: {country}")

print("Multiple default parameters:")
create_profile("Alice")  # All defaults
create_profile("Bob", 25)  # Age specified
create_profile("Charlie", 30, "USA")  # All specified
print()

# Example 3: Power function with default exponent
def power(base, exponent=2):
    """Calculates base raised to exponent (default: square)"""
    return base ** exponent

print("Power function with defaults:")
print(f"power(5) = {power(5)}")  # Square
print(f"power(5, 3) = {power(5, 3)}")  # Cube
print(f"power(2, 4) = {power(2, 4)}")  # Fourth power
print()

"""
เขียน FUNCTION แปลงหน่วยสกุลเงิน ที่สามารถแปลงเงินจาก
THB <-> USD .. 1USD = 32 THB
โดยใช้ชื่อและการใช้งาน
function convert_currency(100,"USD")

แสดงผลออกทางหน้าจอ
100 THB = 3.3 USD
และทดสอบการใช้งาน function ที่ตัวเองเขียนด้วย

"""

def convert_currency(a,b):
    if b == "USD":
        print(f"{a}THB = {a / 32.0}USD")
    else:
        print(a,"USD = ",a * 32.0,"THB")

convert_currency(100,"USD")
convert_currency(100,"THB")