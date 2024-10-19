'''
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
'''

#Problem 3: Temperature Conversion
# Write a program that converts temperatures between Celsius and Fahrenheit. Create two functions,
# one for each conversion, and use them in a program to convert temperatures provided by the user.
# Write another script which tests these functions.
def celsius():
    user_input = float(input("Enter temperature in Fahrenheit: "))
    return (user_input - 32) / 1.8
temperature_in_celsius = celsius()
print(f"temperature in Celsius is {temperature_in_celsius:.2f}")


def fahrenheit():
    user_input = float(input("Enter temperature in Celsius: "))
    return (user_input * 1.8) + 32
temperature_in_fahrenheit = fahrenheit()
print(f"Temperature in Fahrenheit is {temperature_in_fahrenheit:.2f}")