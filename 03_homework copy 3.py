import random
'''
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

# Problem 2 and 5: Write a Python script that prompts the user in the console a simple problem
# ( how much does 5 + 17 equal to ) until the user provides a correct answer.
def random_sum_game():
    while True:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        total = num1 + num2

        user_answer = int(input(f"What is the result of {num1} + {num2}: "))
        
        if user_answer == total:
            print("You guessed correctly!")
        else:
            print(f"You are wrong! The correct answer is {total}. Try again!")

        continue_game = input("Do you want to continue? (y/n): ").lower()

        if continue_game != 'y':
            print("Thanks for playing!")
            break

random_sum_game()
'''
# Problem 3: Write a Python script that iterates over the first 1000 numbers and prints "Fizz" if the number is divisible by 3,
# "Buzz" if it's divisible by 5, and "FizzBuzz" if it's divisible by both 3 and 5.

for number in range(1, 1001):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number} FizzBuzz")
    elif number % 3 == 0:
        print(f"{number} Fizz")
    elif number % 5 == 0:
        print(f"{number} Buzz")
    else:
        print(number)