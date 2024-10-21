
# Problem 0:
# Complete the following function so that it returns the sum of the elements in the list passed as an argument.
# Call your function several times in order to test it
def sum_elements(arr):
    result = 0
    for element in arr:
        result += element
    return result
print(sum_elements([1, 2, 3, 4, 5]))
print(sum_elements([10, 20, 30]))
print(sum_elements([100]))


# Problem 1:
# Simple Calculator Function
# Define a function called `simple_calculator` that takes two numbers and an operator ('+', '-', '*', or '/')
# as arguments and returns the result of the operation.

def simple_calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
result = simple_calculator(2, 3, "*")
print(result)


# Problem 2: Area of Shapes
# Create a module named `geometry` with functions to calculate the area of common shapes
# like a square, rectangle, triangle, and circle. Import this module and use it to calculate the areas of
# different shapes. You should be able to use the function for calculating the area of a rectangle to calculate
# the area of a square by passing in only one argument.
import geometry
print(geometry.area_square(3))
print(geometry.area_rectangle(4, 4))
print(geometry.area_triangle(4, 5))
print(geometry.area_circle(2))


# Problem 3: Temperature Conversion
# Write a program that converts temperatures between Celsius and Fahrenheit. Create two functions,
# one for each conversion, and use them in a program to convert temperatures provided by the user.
# Write another script which tests these functions.
def celsius():
    user_input = float(input("Enter temperature in Fahrenheit: "))
    return (user_input - 32) / 1.8
temperature_in_celsius = celsius()
print(f"temperature in Celsius is {temperature_in_celsius:.2f}C")

def fahrenheit():
    user_input = float(input("Enter temperature in Celsius: "))
    return (user_input * 1.8) + 32
temperature_in_fahrenheit = fahrenheit()
print(f"Temperature in Fahrenheit is {temperature_in_fahrenheit:.2f}F")

    # Testing functions:
def test_both():
    def test_celsius(fahrenheit):
        return (fahrenheit - 32) / 1.8
    assert test_celsius(32) == 0, "Test case 1 failed: 32°F should be 0°C"

    def test_fahrenheit(celsius):
        return (celsius * 1.8) + 32
    assert test_fahrenheit(0) == 32, "Test case 2 failed: 0°C should be 32°F"
    print("All test cases passed!")
test_both()


# Problem 4: Factorial(again):
# Write a recursive function which computes the Factorial of a given integer.
def factorial(x):
    result = 1
    for y in range(1, x + 1):
        result *= y
    return result
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")


# Problem 5: Online Shopping Cart
# Create a Python program that simulates an online shopping cart using a global dictionary variable.
# Every customer has unique id as a key. Define functions to add items to the cart, remove items, calculate the
# total price, and display the contents of the cart. Allow the user to interact with the cart by adding and removing items.