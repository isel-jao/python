print("workin with sets")

fruits = {'apple', 'banana', 'cherry'}
print(fruits)  # Output: {'cherry', 'banana', 'apple'}

fruits = set(['apple', 'banana', 'cherry'])
print(fruits)  # Output: {'cherry', 'banana', 'apple'}

for x in fruits:
    print(x)

# check if "banana" is present in the set
print("banana" in fruits)  # Output: True

fruits.add('dates')
print(fruits)  # Output: {'dates', 'cherry', 'banana', 'apple'}

fruits.update(['elderberry', 'fig'])
# Output: {'elderberry', 'fig', 'dates', 'cherry', 'banana', 'apple'}
print(fruits)


fruits.remove('banana')
print(fruits)  # Output: {'elderberry', 'fig', 'dates', 'cherry', 'apple'}

fruits.discard('blueberry')  # does not raise an error
print(fruits)  # Output: {'elderberry', 'fig', 'dates', 'cherry', 'apple'}

fruits.pop()  # Output: 'elderberry'
print(fruits)  # Output: {'fig', 'dates', 'cherry', 'apple'}

fruits.clear()
print(fruits)  # Output: set()

del fruits  # delete the set completely
# print(fruits)  # Output: NameError: name 'fruits' is not defined

fruits1 = {'apple', 'banana', 'cherry'}
fruits2 = {'banana', 'dates', 'elderberry'}

# Output: {'dates', 'cherry', 'apple', 'elderberry', 'banana'}
print(fruits1.union(fruits2))
# Output: {'dates', 'cherry', 'apple', 'elderberry', 'banana'}
print(fruits1 | fruits2)
print(fruits1.intersection(fruits2))  # Output: {'banana'}
print(fruits1 & fruits2)  # Output: {'banana'}
print(fruits1 - fruits2)  # Output: {'cherry', 'apple'}
print(fruits1.difference(fruits2))  # Output: {'cherry', 'apple'}
print(fruits1 ^ fruits2)  # Output: {'dates', 'cherry', 'apple', 'elderberry'}
print(fruits1.symmetric_difference(fruits2))
