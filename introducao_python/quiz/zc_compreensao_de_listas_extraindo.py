'''
Quiz: Extraindo os primeiros nomes
Use uma compreensão de listas para criar uma nova lista first_names, que contém apenas os primeiros nomes em names em
letras minúsculas.
'''
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.lower().split()[0] for name in names]
print(first_names)


print('---outra solução----')
result = []
for name in names:
    name = name.lower().split()[0]
    result.append(name)
print(result)