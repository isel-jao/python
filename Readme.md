# Python Basics

## Python Built-in Data Types

1. Numeric Types

   - int: `1`, `0`, `-1`, `100`
   - float: `1.0`, `0.0`, `-1.0`, `100.0`
   - complex: `1+2j`, `1-2j`, `1.0+2.0j`, `1.0-2.0j`

2. Boolean Type

   - `True`, `False`

3. Text Type

   - str: `"hello world"`, `'hello world'`

4. Sequence Types

   - list: `[1, 2, 3, 4, 5]` (ordered and mutable)
   - tuple: `(1, 2, 3, 4, 5)` (ordered and immutable)

5. Mapping Type

   - dict: `{"name": "John", "age": 36}`

6. Set Types
   - set: `{"apple", "banana", "cherry"}` (unordered and mutable)
   - frozenset: `frozenset({"apple", "banana", "cherry"})` (unordered and immutable)

## range() Function

- `range(stop)` eg. `range(5)` -> `0, 1, 2, 3, 4`
- `range(start, stop)` eg. `range(1, 5)` -> `1, 2, 3, 4`
- `range(start, stop, step)` eg. `range(1, 10, 2)` -> `1, 3, 5, 7, 9`

## Loops

### For Loop

```python
for i in range(5):
    print(i)
```

Output: 0, 1, 2, 3, 4

### While Loop

```python
i = 0
while i < 5:
		print(i)
		i += 1
```

Output: 0, 1, 2, 3, 4

## Conditional Statements

### If Statement

```python
if 1 < 2:
    print("1 is less than 2")
elif 1 == 2:
    print("1 is equal to 2")
else:
    print("1 is greater than 2")
```

Output: 1 is less than 2

### Ternary Operator

```python
print("1 is less than 2") if 1 < 2 else print("1 is greater than 2")
```

Output: 1 is less than 2

## Functions

```python
def add(a, b):
		return a + b
print(add(1, 2))
```

Output: 3

## Python Operators

### Arithmetic Operators

- `+` Addition (eg. `5 + 3` -> `8`)
- `-` Subtraction (eg. `5 - 3` -> `2`)
- `*` Multiplication (eg. `5 * 3` -> `15`)
- `/` Division (eg. `5 / 3` -> `1.6666666666666667`)
- `%` Modulus (eg. `5 % 3` -> `2`)
- `**` Exponentiation (eg. `5 ** 3` -> `125`)
- `//` Floor Division (eg. `5 // 3` -> `1`)

### Unary Operators:

- `+` Positive (eg. `+5` -> `5`)
- `-` Negative (eg. `-5` -> `-5`)

### Bitwise Operators

- `&` Bitwise And (eg. `5 & 3` -> `1`)
- `|` Bitwise Or (eg. `5 | 3` -> `7`)
- `^` Bitwise Xor (eg. `5 ^ 3` -> `6`)
- `~` Bitwise Not (eg. `~5` -> `-6`)
- `<<` Bitwise Left Shift (eg. `5 << 3` -> `40`)
- `>>` Bitwise Right Shift (eg. `5 >> 3` -> `0`)

### Assignment Operators

- `=` Assignment (eg. `x = 5`)
- `+=` Addition Assignment (eg. `x += 3` -> `x = x + 3`)
- `-=` Subtraction Assignment (eg. `x -= 3` -> `x = x - 3`)
- `*=` Multiplication Assignment (eg. `x *= 3` -> `x = x * 3`)
- `/=` Division Assignment (eg. `x /= 3` -> `x = x / 3`)
- `%=` Modulus Assignment (eg. `x %= 3` -> `x = x % 3`)
- `**=` Exponentiation Assignment (eg. `x **= 3` -> `x = x ** 3`)
- `//=` Floor Division Assignment (eg. `x //= 3` -> `x = x // 3`)

### Comparison Operators

- `==` Equal (eg. `5 == 3` -> `False`)
- `!=` Not Equal (eg. `5 != 3` -> `True`)
- `>` Greater Than (eg. `5 > 3` -> `True`)
- `<` Less Than (eg. `5 < 3` -> `False`)
- `>=` Greater Than or Equal To (eg. `5 >= 3` -> `True`)
- `<=` Less Than or Equal To (eg. `5 <= 3` -> `False`)

### Logical Operators

- `and` Logical And (eg. `True and False` -> `False`)
- `or` Logical Or (eg. `True or False` -> `True`)
- `not` Logical Not (eg. `not True` -> `False`)

### Membership Operators

- `in` Membership (eg. `1 in [1, 2, 3]` -> `True`)
- `not in` Membership (eg. `1 not in [1, 2, 3]` -> `False`)

### Identity Operators

- `is` Identity (eg. `1 is 1` -> `True`)
- `is not` Identity (eg. `1 is not 1` -> `False`)

```python
x = 5
y = 5
print(x == y) # True
print(x is y) # True

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y) # True
print(x is y) # False
```
