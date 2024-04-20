print("working with lists")

### Creating Lists: ###

# Basic list
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4]
mixed_list = [True, 3.14, "hello"]

# List comprehension
squares = [x**2 for x in range(5)]
# squares = []
# for x in range(5):
#    squares.append(x**2)


### Accessing Elements: ###
print(fruits[0])  # Output: apple (first element)
print(numbers[2])  # Output: 3 (third element)
print(fruits[-1])  # Output: orange (last element)


### Iterating over Lists: ###
for fruit in fruits:
  print(fruit)


### Adding and Removing Elements: ###
fruits.append("mango")
print(fruits)  # Output: ["apple", "banana", "orange", "mango"]

fruits.insert(1, "kiwi")
print(fruits)  # Output: ["apple", "kiwi", "banana", "orange", "mango"]

fruits.remove("banana")
print(fruits)  # Output: ["apple", "kiwi", "orange", "mango"]

del fruits[2]  # Remove element at index 2
print(fruits)  # Output: ["apple", "kiwi", "mango"]

removed_fruit = fruits.pop(0)  # Remove and return element at index 0
print(fruits)  # Output: ["kiwi", "mango"]


### List Slicing: ###
sliced_fruits = fruits[1:]  # From index 1 to the end
print(sliced_fruits)  # Output: ["kiwi", "mango"]

another_slice = fruits[::-1]  # Reverse the list
print(another_slice)  # Output: ["mango", "kiwi"]


### List methods: ###
# len(list): Returns the length of the list.
# list.sort(): Sorts the list elements in place.
# list.reverse(): Reverses the order of elements in place.
# list.index(element): Returns the index of the first occurrence of the element.
# list.count(element): Counts the number of occurrences of the element.

del fruits
del numbers
del mixed_list
del squares

################################### Advanced Concepts: ###################################

### List Comprehensions with Conditionals: ###
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num % 2 == 0]  # List of even numbers
print(even_numbers)  # Output: [2, 4, 6]


### Nested Lists: ###
inventory = [
    ["apple", 5],
    ["banana", 3],
    ["orange", 10]
]

# Accessing elements within nested lists
first_fruit = inventory[0][0]  # first_fruit will be "apple"


### List Membership and Comparison: ###
fruits = ["apple", "banana", "orange"]
print("apple" in fruits)  # Output: True

another_list = fruits.copy()  # Create a copy to avoid reference issues
print(fruits == another_list)  # Output: True

### Zip Function: ###
fruits = ["apple", "banana", "orange"]
colors = ["red", "yellow", "orange"]
fruit_color_pairs = list(zip(fruits, colors))
print(fruit_color_pairs)  # Output: [("apple", "red"), ("banana", "yellow"), ("orange", "orange")]

### Enumerate Function: ###
movies = ["edge of tomorrow", "source code","interstellar"]
indexedMovies = [f'0{str(i + 1).zfill(1)}-{"_".join(movie.split(" "))}' for i, movie in enumerate(movies)]
print(indexedMovies)  # Output: ['01-edge_of_tomorrow', '02-source_code', '03-interstellar']

### Lambda Functions with Lists: ###
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

###
fruits = ["apple","cherry", "Banana"]

def sort_by_length(fruit):
  return len(fruit.lower())  # Sort by lowercase length

fruits.sort(key=sort_by_length)
print(fruits)  # Output: ["cherry", "Banana", "apple"]


### Finding minimum and maximum elements: ###
numbers = [10, 5, 2, 8, 1]
minimum = min(numbers)
maximum = max(numbers)

print("Minimum:", minimum)  # Output: Minimum: 1
print("Maximum:", maximum)  # Output: Maximum: 10


### Working with Strings in Lists: ###

# Joining list elements:
fruits = ["apple", "banana", "orange"]
fruit_string = ", ".join(fruits)
print(fruit_string)  # Output: apple, banana, orange
