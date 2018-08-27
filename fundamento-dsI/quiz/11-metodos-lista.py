a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

# qual é o maior e o menor vetor?
print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

print('----------------------')

# oredenar e inserir caractre
names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names))) # Albert & Carol & Donna & ben

names.append("Eugenia")
print(sorted(names))
