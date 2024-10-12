# Problem 0: Write a program that takes an integer input from the user and checks if it's odd or even.
#   Use an if-else statement to print the result.
while True:
    number = int(input("Enter a number: "))
    if (number % 2) == 0:
        print("The number is: even")
    else:
        print("The number is: odd")
    if input("Do you want to continue? (y/n): ").lower() != 'y':
        break
        
# Problem 1: Write a Python program to find the sum of all even numbers from 1 to 100 using a loop.
# Make use of control flow constructs like the for loop and conditional statements.
sum_of_evens = 0
for number in range(1, 101):
    if number % 2 == 0:
        sum_of_evens += number

print("The sum of all even numbers from 1 to 100 is:", sum_of_evens)

# Problem 2: Write a Python script that prompts the user in the console a simple problem
# ( how much does 5 + 17 equal to ) until the user provides a correct answer.
        