x = [2,8,1,4,6,3,7]
print ("Sorted List returned: "),
print (sorted(x))

print ("\nReverse sort: "),
print (sorted(x,reverse = True))

print("\nOriginal list not modified: "),
print (x)

print("\nSorting different data types: "),

x = ['q','w','r','e','t','y']
print (sorted(x))

x = ('q','w','e','r','t','y')
print (sorted(x))

x = "python"
print (sorted(x))

x = {'q':1,'w':2,'e':3,'r':4,'t':5,'y':6}
print (sorted(x))

x = frozenset(('q','w','e','r','t','y'))
print(sorted(x))

