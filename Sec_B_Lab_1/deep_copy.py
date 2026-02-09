import copy

a = [[1, 2], [3, 4]]
# b = a.copy() # Shallow copy of the list a
b = copy.deepcopy(a) # Deep copy of the list a
b[0].append(5)

print(a) # output: [[1, 2], [3, 4]]
print(b) # output: [[1, 2, 5], [3, 4]]