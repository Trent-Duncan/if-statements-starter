# Abe Lincoln
# 26 SEP 20XX
# Simple IF Statements in Python

# Example 1
number = 10
if number > 0:
    print("The number is positive.")

# Example 2
number = 10
if number % 2 == 0:
    print("The number is even.")

# Example 3
num1 = 10
num2 = 5
if num1 >= num2:
    print("num1 is greater than or equal to num2.")

# Example 4
string = "hello, world!"
if string.startswith("hello"):
    print("The string starts with 'hello'.")

# Example 5
string = "Hello"
if string.startswith("H"):
    print("The string starts with 'H'.")

# Example 6
filepath = "/home/user/documents/file.txt"
if filepath.startswith("/home/user"):
    print("The file is located in the /home/user directory.")

# Example 7
filename = "cat.jpg"
if filename.endswith(".jpg"):
    print("The file is a JPEG image.")

# Example 8
word = "apple"
if word.startswith("a") or word.startswith("e") or word.startswith("i") or word.startswith("o") or word.startswith("u"):
    print("The word starts with a vowel.")

# Example 9
url = "https://example.com"
if url.endswith(".com"):
    print("The URL is a .com domain.")

# Example 10
string = "Hello, world!"
if string.endswith("!"):
    print("The string ends with an exclamation mark.")

# Example 11
is_raining = True
if is_raining:
    print("I'll bring my umbrella today.")   

# Example 12
# Using the in membership operator to check whether a
# specific item is contained in a Python list
fruits = ['apple', 'banana', 'orange']
if 'banana' in fruits:
    print('Banana is in the list!')
