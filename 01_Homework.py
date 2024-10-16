import math

#   1. Write a Python script that prints "Hello, World!" to the console.
print('Hello, World!')

#   2. Create variables to store your name, age, and favorite color. 
# Then, print out a message using these variables 
# (e.g., "My name is [name], I am [age] years old, and my favorite color is [color].").
name = "Toni"
age = 33
favorite_color = "green"

print(f"My name is {name}, I am {age} years old, and my favorite color is {favorite_color}. ")


#   3. Write a program that calculates the area of a rectangle.
# Prompt the user to enter the length and width, calculate the area, and then print it.
length = float(input("Enter a lenght: "))
width = float(input("Enter a width: "))
area = length * width

print(f"The area of a rectangle is: {area}cm")


#   4. Write a program that converts temperatures from Fahrenheit to Celsius. 
# Prompt the user to enter a temperature in Fahrenheit and then print out the equivalent temperature in Celsius.
fahrenheit = float(input("Enter temperature in fahrenheit: "))
celsius = (fahrenheit - 32) * (5 / 9)

print(f"temperature in celsius is: {celsius:.2f} C")


#   5. Create a program that asks the user to enter two numbers and then prints out the sum, 
# difference, product, and quotient of those numbers.
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
result1 = (first_number + second_number)
result2 = (first_number - second_number)
result3 = (first_number * second_number)
result4 = (first_number / second_number)

print("*******************************")
print(f"The sum of numbers is: {result1}\nThe difference of numbers is: {result2}\nThe product of numbers is: {result3}\nThe quotient of numbers is: {result4:.2f}")
print("*******************************")
                

#   6. Write a program that prompts the user to enter a radius and then calculates 
# and prints the area and circumference of a circle with that radius.
enter_radius = float(input("Enter radius of the circle: "))
area = math.pi*enter_radius**2

print(f"the area of circle is: {area}")


#   7. Create a program that checks whether a given number is even or odd.
# Prompt the user to enter a number and then print out whether it's even or odd.
for num in range(1, 21):
    if num % 2 == 0:
        print(num, "is even")
else:
    print(num, "is odd")
        # if 1-20 is OK,but if is 1-21,it says 20 is both: even and odd
                        

#   8. Write a program that prompts the user to enter their age and then 
# determines and prints out whether they are eligible to vote (i.e., if they are 18 or older)

age = float(input("Enter your age: "))
if age >= 18 and age < 100:
    print("You can vote")
elif age > 0:
    print("You cannot vote")
elif age <= 0:
    print("Enter valid age")


#   9. Create a program that prompts the user to enter a string and then prints out the length of the string.
string = input("Enter some text: ")

print(len(string))


#   10. Write a program that prompts the user to enter two strings and then concatenates them together 
# (i.e., joins them into one string) and prints out the result.
string1 = input("Whats your name? ")
string2 = input("Where are you from? ")
solution = string1 + " " + string2

print(solution)

# test branch pull request