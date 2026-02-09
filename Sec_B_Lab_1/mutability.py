a = 10
a + 2 # This does not change the value of a, it creates a new value 12 and does not assign it to a
print(a) # This will print 10, not 12
a = a + 2
print(a) # This will print 12, because we have assigned the new value back to a

b = [1, 2, 3] # This creates a list object and assigns it to b
b.append(4) # This modifies the list object that b is referencing, it does not create a new list, it changes the existing one
print(b)

c = 'aiub' # This creates a string object and assigns it to c
c.upper() # This does not change the value of c, it creates a new string 'AIUB' and does not assign it to c
print(c) # This will print 'aiub', not 'AIUB'
# c[1] = 'A' # This will raise an error because strings are immutable, you cannot change a character in a string
c.replace('i', 'A') # This does not change the value of c, it creates a new string 'AAUB' and does not assign it to c
print(c) # This will print 'aiub', not 'AAUB'
c = c.replace('i', 'A') # This will create a new string 'AAUB' and assign it back to c
print(c) # This will print 'AAUB'