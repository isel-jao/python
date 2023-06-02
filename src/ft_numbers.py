import math
import random

print("workin with numbers")

my_int = 6
print(my_int, type(my_int))  # Output: 6 <class 'int'>

# Floats
my_float = 6.0
print(my_float, type(my_float))  # Output: 6.0 <class 'float'>

# Complex
my_complex = 6 + 0j
print(my_complex, type(my_complex))  # Output: (6+0j) <class 'complex'>

# Number Type Conversion:
a = 1
print(float(a))  # Output: 1.0

b = 1.99
print(int(b))  # Output: 1

c = 1
print(complex(c))  # Output: (1+0j)


# Mathematical Functions:

print(math.pi)  # Output: 3.141592653589793
print(math.e)  # Output: 2.718281828459045
print(math.inf)  # Output: inf
print(-math.inf)  # Output: -inf
print(math.nan)  # Output: nan
print(abs(-7))  # Output: 7
print(math.ceil(1.2))  # Output: 2
print(math.floor(1.2))  # Output: 1
print(round(1.2))  # Output: 1
print(round(1.5))  # Output: 2
print(math.exp(1))  # Output: 2.718281828459045
print(math.log(2.718281828459045))  # Output: 1.0
print(math.log(2.718281828459045, 10))  # Output: 0.4342944819032518
print(math.log10(2.718281828459045))  # Output: 0.4342944819032518
print(math.pow(2, 3))  # Output: 8.0
print(math.sqrt(4))  # Output: 2.0
print(math.sin(math.pi / 3))  # Output: 0.8660254037844386
print(math.cos(math.pi / 3))  # Output: 0.5000000000000001
print(math.tan(math.pi / 3))  # Output: 1.7320508075688767
print(math.asin(0.8660254037844386))  # Output: 1.0471975511965976
print(math.acos(0.5000000000000001))  # Output: 1.0471975511965979
print(math.atan(1.7320508075688767))  # Output: 1.0471975511965976
print(math.degrees(1.0471975511965976))  # Output: 59.99999999999999
print(math.radians(59.99999999999999))  # Output: 1.0471975511965976

# Random Number Functions:

print(random.random())  # Return a random number between 0 and 1

print(random.randint(10, 20))  # Return a random number between a given range

print(random.choice([1, 2, 3, 4, 5]))  # Choose a random element from a list

# Shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)
