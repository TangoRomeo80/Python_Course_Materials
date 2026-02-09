import copy

a = [1, 2, 3]
b = a.copy() # Shallow copy of the list
b.append(4)
print(id(a))
print(id(b))
print(a)
print(b)

c = [[1, 2], [3, 4]]
d = copy.deepcopy(c) # Deep copy of the nested list
d[0].append(5)
print(id(c[0]))
print(id(d[0]))
print(c)
print(d)
