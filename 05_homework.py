# 1. Create a list with the numbers from 1 to 10 and print it.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

# # 1.1. Create a list with the numbers from 1 to 1000 and print it.
#numbers2 = list(range(1, 1001))
#print(numbers2)

# 2. Reverse the order of the elements in the list from problem 1 and print the result.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
print(numbers)

# 3. Given a list of words, create a new list containing the lengths of each word.
words = ["apple", "banana", "cherry", "dolphin", "elephant", "falcon", "guitar", "horizon", "island", "jungle"]
len_words = [len(word) for word in words]
print(len_words)

# 3.1. Given a list of words, create a new dictionary mapping every word to it's length.
len_word = {word: len(word) for word in words}
print(len_word)

# 4. Write a function that takes a list and returns the sum of all even numbers in the list.
def even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(even_numbers(numbers))

# 5. Given a tuple of integers, find the maximum and minimum values without using built-in functions.
integers = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
max_int = integers[0]
min_int = integers[0]

for num in integers:
    if num > max_int:
        max_int = num
    if num < min_int:
        min_int = num

print(max_int)
print(min_int)

# 6. Implement a basic queue structure ( as a global var ) by defining two functions `enqueue` and `dequeue.
# Initialize an empty list to act as the queue
queue = []

# Function to add an element to the end of the queue
def enqueue(item):
    queue.append(item)
    print(f"Enqueued: {item}")

# Function to remove an element from the front of the queue
def dequeue():
    if len(queue) == 0:
        print("Queue is empty!")
        return None
    item = queue.pop(0)
    print(f"Dequeued: {item}")
    return item

# Example:
enqueue(1)
enqueue(2)
enqueue(3)
dequeue()  # Should remove 1
dequeue()  # Should remove 2
dequeue()  # Should remove 3
dequeue()  # Queue is empty!

# 7. Create a dictionary that maps students to their bank account number. Some students may have multiple bank accounts.
student_accounts = {
    "Alice": ["123456789", "987654321"],
    "Bob": ["234567890"],
    "Joro": ["345678901", "456789012", "567890123"],
    "Diana": ["678901234"],
    "Evа": ["789012345", "890123456"]
}
print(student_accounts)

# 8. Think of a function that can hash lists. Implement it and test it.
def hash_list(input_list):
    return hash(tuple(input_list))
test_list = [1, 2, 3, 4, 5]
hashed_value = hash_list(test_list)

print(f"List: {test_list}")
print(f"Hashed Value: {hashed_value}")

# 9. Write a function that counts the frequency of each word in a given string
# (copy the first paragraph of an online article,for example) and returns a dict with the result.
import string

def word_frequency(text):
    # Convert text to lowercase and remove punctuation
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    
    # Split text into words
    words = text.split()
    
    # Create a dictionary to count each word's frequency
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

# Example usage with a sample paragraph
sample_text = """
Artificial intelligence (AI) is rapidly advancing in various sectors, transforming industries and 
enhancing our daily lives. From healthcare to finance, AI-driven solutions provide unprecedented 
efficiencies and capabilities, helping to automate routine tasks and analyze large datasets with 
remarkable speed and accuracy. As AI technology evolves, it continues to push the boundaries of 
what is possible, leading to new innovations and opportunities.
"""
# Calculate word frequency
result = word_frequency(sample_text)

print(result)

# 10. Create two sets with some common elements and find their intersection.
# Define two sets with some common elements
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
# Find the intersection of the two sets
intersection = set_a.intersection(set_b)

print("Set A:", set_a)
print("Set B:", set_b)
print("Intersection:", intersection)

# 11. Given two sets, write a function that determines if one set is a subset of the other. Do not use `<` or `>`
def is_subset(set1, set2):
    # Check if all elements in set1 are in set2
    for element in set1:
        if element not in set2:
            return False
    return True

# Example usage
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

print(is_subset(set_a, set_b))  # Should return True as set_a is a subset of set_b
print(is_subset(set_b, set_a))  # Should return False as set_b is not a subset of set_a

# 12. Write a function to remove duplicates from a list using a set.
def remove_duplicates(input_list):
    # Convert the list to a set to remove duplicates, then back to a list
    return list(set(input_list))

sample_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(sample_list)

print("Original List:", sample_list)
print("List without duplicates:", unique_list)

# 13. Use list comprehension to create a list of the squares of even numbers from 1 to 30.
squares_of_even_numbers = [x**2 for x in range(1, 31) if x % 2 == 0]
print(squares_of_even_numbers)

# 14. Given a list of words, create a dictionary where the keys are the
# words and the values are their lengths, using dictionary comprehension.
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)

# 15. Write a program that generates a set of prime numbers less than 100 using list comprehensions and sets.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate a set of prime numbers less than 100
prime_numbers = {x for x in range(2, 100) if is_prime(x)}

print("Prime numbers less than 100:", prime_numbers)