a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
print("tamanho de a: ", len(a))
print("tamanho de b: ", len(b))
print("Repetidos em a: ", len(a) - len(b))
print("valores de b: ", b)

print("-------------------")

a = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
b = set(a)
b.add(5)
print("valores de b depois add(5): ", b)
b.pop()
print("depois do pop(): ", b)