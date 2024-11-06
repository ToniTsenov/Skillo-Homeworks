
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

# global variables to store the information
shopping_carts = {}
items = []
prices = []
quantities = []
total = 0

# function to add items to card
def add_to_card():
    customer_id = int(input("Enter custumer ID: "))
    if customer_id not in shopping_carts:
        shopping_carts[customer_id] = {"items": [], "prices": [], "quantities": []}

    item = input("Enter item to add in card: ").strip().lower()
    price = float(input("Enter price of item: "))
    quantity = int(input("Enter quantity of item: "))
    
    # Access the customer's specific cart
    cart = shopping_carts[customer_id]
    cart["items"].append(item)
    cart["prices"].append(price)
    cart["quantities"].append(quantity)

    total_price = price * quantity

    print(f"Added {quantity}x {item}'s at total price of {total_price:.2f} BGN for customer {customer_id} ")

# function to remove items from card
def remove_from_card():
    customer_id = int(input("Enter custumer ID: "))
    if customer_id not in shopping_carts or not shopping_carts[customer_id]["items"]:
            print("No items found in the cart for this customer.")
            return

    item = input("Enter item to remove from card: ").strip().lower()
    quantity = int(input("Enter quantity: "))

    cart = shopping_carts[customer_id]

# Check if the item exists in the customer cart
    if item in cart["items"]:
        index = cart["items"].index(item)
        
        # Remove specified quantity or entire item if quantity matches or exceeds
        if cart["quantities"][index] > quantity:
            cart["quantities"][index] -= quantity
            print(f"Removed {quantity} of {item} from customer {customer_id}'s cart.")
        elif cart["quantities"][index] == quantity:
            # Remove the item completely from cart if quantity matches
            del cart["items"][index]
            del cart["prices"][index]
            del cart["quantities"][index]
            print(f"Removed all of {item} from customer {customer_id}'s cart.")
        else:
            print("Quantity to remove exceeds quantity in the cart.")
    else:
        print(f"{item} not found in customer {customer_id}'s cart.")

# Function to display the cart contents for a specific customer
def display_cart(customer_id):
#Display the contents of the customer cart.
    if customer_id not in shopping_carts or not shopping_carts[customer_id]["items"]:
        print("Cart is empty.")
        return
    
    cart = shopping_carts[customer_id]
    print(f"\nCart contents for customer {customer_id}:")
    total = 0
    for i in range(len(cart["items"])):
        item_total = cart["prices"][i] * cart["quantities"][i]
        total += item_total
        print(f"{cart['quantities'][i]} x {cart['items'][i]} at ${cart['prices'][i]:.2f} each - Total: ${item_total:.2f}")
    
    print(f"\nTotal cart value: ${total:.2f}")


# shopping card interface function
def shopping_card_interface():
    while True:
        print("\nOptions: \n1. Add\n2. Remove\n3. Display\n4. Exit")
        action = input("Enter action:(1-5): ").strip()

        if action == "1":
            add_to_card()

        elif action == "2":
            remove_from_card()

        elif action == "3":
            customer_id = int(input("Enter customer ID to display cart: "))
            display_cart(customer_id)
            
        elif action == "4":
            print("Exiting from shopping card. ")
            break
        else:
            print("Invalid option!Please enter a valid option between 1 and 5. ")
            continue
shopping_card_interface()