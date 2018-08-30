'''
Quiz: Enumerate
Use enumerate para modificar a lista cast para que cada elemento contenha o nome seguido da altura correspondente do
personagem. Por exemplo, o primeiro elemento de cast deve mudar de "Barney Stinson" para "Barney Stinson 72".
'''
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# o enumerate()
for c in enumerate(cast):
    print(c)

print("---------")
# write your for loop here
for i, caracter in enumerate(cast):
    print(i, caracter)
    cast[i] = caracter + " "+str(heights[i])
print(cast)


