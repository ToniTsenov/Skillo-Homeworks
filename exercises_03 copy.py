# Exercise 1: Online Shopping Discount

# Given a variable `total_amount` representing the total amount in the shopping cart,
# write a program that prints a discount message if the total amount is over $100,
# and always prints a thank you message.

total_amount = 120  # Fill in the total amount here

if total_amount >= 100:
    print("you have discount!")
print("thank you!")

# Exercise 2: Temperature Checker

# Given a variable `temperature` representing the current temperature in Celsius,
# write a program that prints "Warm" if the temperature is greater than or equal to 25 degrees Celsius,
# otherwise print "Cool".

temperature = 26  # Fill in the temperature here

if temperature >= 25:
    print("warm")
else:
    print("cool")

# Exercise 3: Time of the Day

# Given a variable `hour` representing the current hour (in 24-hour format),
# write a program that prints "Good Morning" if the hour is before 12 (12 inclusive),
# "Good Afternoon" if the hour is between 12 and 17 (17 inclusive),
# and "Good Evening" if the hour is after 17.

hour = 12  # Fill in the hour here

if hour > 6 and hour <= 12:
    print("good morning!")
elif hour > 12 and hour <= 17:
    print("good afternoon!")
elif hour > 17 and hour <= 24:
    print("good evening!")


# Exercise 4: Secret Message

# Given a variable `message` representing a secret message,
# write a program that prints "Message found" if the message is not empty,
# otherwise print "No message".

message = ""  # Fill in the message here

if message:
    print("message found")
else:
    print("message not fount")

# Exercise 5: List Iteration

# You have a list of fruits. Write a program that iterates over each fruit in the list and prints each fruit's name.

fruits = ["Apple", "Banana", "Orange", "Grape", "Watermelon"]

for fruit in fruits:
    print(fruit)

# Exercise 6: Range Iteration

# Write a program that prints all the even numbers from 1 to 20 using a for loop and the range() function.

for num in range (1, 21):
    if num % 2 == 0:
        print(num)

# Exercise 7: While Loop

# Write a program using a while loop to find the sum of all numbers from 1 to 100.

total = 0
number = 1
while num <= 100:
    total += num
    num += 1
    print(num)

# Exercise 8: Number of Friends

# Write a program that asks how many friends you have and then asks for each of their names.

num_friends = int(input("How many friends you have?: "))
friends = []

for x in range(num_friends):
    name = input(f"Enter the name of friend {x + 1}: ")
    friends.append(name)

print("\nYour friends are: ")
for friend in friends:
    print(friend)

# Exercise 9: Guess the Number
# Write a program that has a number and keeps asking the user to input a number until the user guesses it.

secret_number = 42
user_input = float(input("Guess the secret number?: "))
while True:
    if user_input != secret_number:
        print("Wrong!Try again!")
        user_input = float(input("Guess the secret number?: "))
    else:
        print(f"You won!The secret number was {secret_number}")
        break  
        
# Exercise 10: Multiplication Table

# Generate the multiplication table for the numbers 1 to 9.

for x in range (1, 10):
    for y in range (1, 10):
        print(f"{x} x {y} = {x * y}", end="\t")
    print()

# Exercise 11: continue

# Do the same as in Exercise 6 but do not print the number 10. Use `continue` do achieve this

for num in range (1, 21):
    if num % 2 == 0:
        if num == 10:
            continue
        print(num)

# Exercise 12: Password Checker

# Write a program that asks the user to enter a password. If the password is correct, print a message saying
# "Access granted" and end the program. If the user enters the wrong password three times, print "Access denied" and
# end the program..

correct_password = "learnpythonwithskillo"
user_ask = input("Enter a password: ")
counts = 3

while counts > 0:
    if user_ask != correct_password:
        counts -= 1
        if counts == 0:
            print("Access denied!")
            break
        else:
            print(f"Wrong password!Try again!Remaining counts: {counts}")
            user_ask = input("Enter a password: ")
    else:
        print("Access grandet!")
        break