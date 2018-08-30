'''
Quiz: Tuplas descompactadas
Descompacte a tupla cast em duas tuplas, names e heights.
'''

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = zip(*cast)


print(names)
print(heights)