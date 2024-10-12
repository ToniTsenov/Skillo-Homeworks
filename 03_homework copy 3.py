# Problem 0: Write a program that takes an integer input from the user and checks if it's odd or even.
#   Use an if-else statement to print the result.

number = int(input("Enter a number: "))
if (number % 2) == 0:
    print("The number is: even")
else:
    print("The number is: odd")

# Problem 1: Write a Python program to find the sum of all even numbers from 1 to 100 using a loop.
# Make use of control flow constructs like the for loop and conditional statements.
    sum_of_evens = 0

    for number in range(1, 101):
    # Check if the number is even
        if number % 2 == 0:
        # Add the even number to the sum
            sum_of_evens += number

# Print the result
    print("The sum of all even numbers from 1 to 100 is:", sum_of_evens)