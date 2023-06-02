print("workin with strings")

# Using single quotes
str1 = 'Hello, World!'
print(str1)  # Output: Hello, World!

# Using double quotes
str2 = "Hello, World!"
print(str2)  # Output: Hello, World!


str1 = 'Hello, World!'

# Accessing first character
print(str1[0])  # Output: H

# Slicing
print(str1[0:5])  # Output: Hello


str1 = 'Hello'
str2 = 'World'

# Concatenation
print(str1 + str2)  # Output: HelloWorld

# Repetition
print(str1 * 3)  # Output: HelloHelloHello

# Checking if a character is in a string
print('H' in str1)  # Output: True

# Checking if a character is not in a string
print('H' not in str1)  # Output: False


str1 = 'Hello, World!'

# Lowercase
print(str1.lower())  # Output: hello, world!

# Uppercase
print(str1.upper())  # Output: HELLO, WORLD!

# Replace
print(str1.replace('H', 'J'))  # Output: Jello, World!

# Split
print(str1.split(','))  # Output: ['Hello', ' World!']

# Strip
str2 = ' Hello, World! '
print(str2.strip())  # Output: 'Hello, World!'

# Check alphanumeric
str3 = "Hello123"
print(str3.isalnum())  # Output: True

# Check if all characters are alphabetic
str4 = "Hello"
print(str4.isalpha())  # Output: True

# Check string starts with a certain character
str5 = "Hello"
print(str5.startswith('H'))  # Output: True

# Check string ends with a certain character
str6 = "Hello"
print(str6.endswith('o'))  # Output: True

# Find position of a character in string
str7 = "Hello"
print(str7.find('e'))  # Output: 1


############### String Formatting ###############
# Using .format() method
# Output: Hello, John. You are 23.
print("Hello, {}. You are {}.".format("John", 23))
print("The novel '{1}' was published by {0}".format(
    "Author Name", "Book Name"))


# Using f-strings (Python 3.6+)
name = "John"
age = 23
print(f"Hello, {name}. You are {age}.")  # Output: Hello, John. You are 23.

# Using % operator
# Output: Hello, John. You are 23.
print("Hello, %s. You are %d." % ("John", 23))
