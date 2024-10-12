#   Write a program that takes an integer input from the user and checks if it's odd or even.
#   Use an if-else statement to print the result.
while True:
    number = int(input("Enter a number: "))
    if (number % 2) == 0:
        print("The number is: even")
    else:
        print("The number is: odd")
