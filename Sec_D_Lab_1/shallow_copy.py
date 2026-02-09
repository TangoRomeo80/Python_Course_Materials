a = [1, 2, 3]
# b = a # This will not create a new list, it will just create a new reference to the same list
b = a.copy() # Shallow copy of the list a
b.append(4)

print(id(a))
print(id(b))

print(a)
print(b)

# Variables don't store the objects, it only stores the reference(memory location) to the objects.

