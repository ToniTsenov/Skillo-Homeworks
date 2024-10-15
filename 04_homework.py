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
'''
# Problem 2: Area of Shapes
# Create a module named `geometry` with functions to calculate the area of common shapes
# like a square, rectangle, triangle, and circle. Import this module and use it to calculate the areas of
# different shapes. You should be able to use the function for calculating the area of a rectangle to calculate
# the area of a square by passing in only one argument.