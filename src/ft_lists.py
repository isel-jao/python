print("working with lists")

fruits = ['apple', 'banana', 'cherry', 'dates']

print(fruits)  # Output: ['apple', 'banana', 'cherry', 'dates']
print(len(fruits))  # Output: 4

# Iterating over a list
for (x in fruits)
    print(x)

fruits.append('elderberry')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'dates', 'elderberry']

print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: elderberry
print(fruits[1:3])  # Output: ['banana', 'cherry']
print(fruits[:3])  # Output: ['apple', 'banana', 'cherry']
print(fruits[2:])  # Output: ['cherry', 'dates', 'elderberry']
print(fruits[-4:-1])  # Output: ['banana', 'cherry', 'dates']

fruits.pop()
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'dates']
fruits.pop(1)
print(fruits)  # Output: ['apple', 'cherry', 'dates']

fruits.insert(1, 'banana')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'dates']

fruits.remove('banana')
print(fruits)  # Output: ['apple', 'cherry', 'dates']

# fruits.remove('banana')  # Output: ValueError: list.remove(x): x not in list

fruits.reverse()
print(fruits)  # Output: ['dates', 'cherry', 'apple']

fruits.sort()
print(fruits)  # Output: ['apple', 'cherry', 'dates']

# A new list with each item in fruits titlecased
fruits_in_caps = [fruit.title() for fruit in fruits]
print(fruits_in_caps)  # Output: ['Apple', 'Cherry', 'Dates']

fruits.clear()
print(fruits)  # Output: []

del fruits
# print(fruits)  # Output: NameError: name 'fruits' is not defined
