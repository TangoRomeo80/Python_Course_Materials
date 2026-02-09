# Every variable in python is an object.
a = 10
# We can check the type of variable using the type() function.
print(type(a))  # Output: <class 'int'>

# Variables only store references (memory location) to objects, not the actual data.
b = [1, 2, 3]
c = b
c.append(4)
# id() function returns the memory address of the object.
print(id(b))
print(id(c))
print(b)
print(c)

# Mutability defines if a data type can be changed in place.
# Mutable types: list, dict, set
# Immutable types: int, float, str, tuple





