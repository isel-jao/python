print("class in python")


class ClassName:
    def __init__(self, name="Initial Value", age=None):
        self.name = name
        self.__age = 0

    def display_name(self):
        print(self.name)


class ChildClass (ClassName):
    def __init__(self, name="Initial Value", age=None):
        super().__init__(name, age)
        self.name = name
        self.__age = 0

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


print(ClassName)  # Output: <class '__main__.ClassName'>
print(type(ClassName))  # Output: <class 'type'>

# Creating an object of the class
obj = ClassName()

print(obj)  # Output: <__main__.ClassName object at <memory location>>
print(type(obj))  # Output: <class '__main__.ClassName'>
print(obj.name)  # Output: Initial Value
obj.name = "New Value"
obj.display_name()  # Output: New Value

child = ChildClass()

print(child)  # Output: <__main__.ChildClass object at <memory location>>
print(type(child))  # Output: <class '__main__.ChildClass'>

child.set_age(10)
print(child.get_age())  # Output: 10
