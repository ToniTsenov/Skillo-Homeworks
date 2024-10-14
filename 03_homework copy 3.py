import random

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
        
# Problem 4: Design a Python program that simulates a simple guessing game.
# The program should generate a random number between 1 and 100 and ask the user to guess it.
# Provide hints like "Too high" or "Too low" until the user 
# guesses the correct number. Use a while loop for this game.
low_num = 1
hight_num = 100
answer = random.randint(low_num, hight_num)
guesses = 0
is_running = True

print("Welcome to guess game!")
print(f"Select number between {low_num} and {hight_num} ")

while is_running:
    guess = input("Enter the guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < low_num or guess > hight_num:
            print("The number is out of range!")
            print(f"Please select number between {lowest_num} and {highest_num} ")
        elif guess < answer:
            print("Too low!Try again!")
        elif guess > answer:
            print("Too hight!Try again!")
        else:
            print(f"You won!The answer was: {answer} ")
            print(f"The number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess!")
        print(f"Please select number between {low_num} and {hight_num} ")
        

# Problem 6: Write a Python program that takes an integer input from the user
# and prints the multiplication table for that number from 1 to 10 using a for loop
user_number = int(input("Enter a number: "))
for number in range (1, 11):
        print(f"{user_number} * {number} = {user_number * number}")
        

# Problem 7: Create a Python program that checks if a given integer is a prime number.
# Use a for loop to iterate through possible divisors and use an if-else statement to determine if it's prime.
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

while True:
    num = int(input("Enter an integer to check if it's a prime number: "))

    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
    
    try_again = input("Try again (y/n)? ").lower()
    if try_again != "y":
        print("Bye!")
        break
        

# Problem 8: Write a program that takes an integer 'n' as input
# and prints the following pattern using nested for loops:
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
# tazi zada4a ne q razbrah