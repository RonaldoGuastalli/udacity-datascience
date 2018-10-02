'''
Quiz: Lambda com mapa
map() é uma função interna de ordem superior que aceita uma função e um iterável como entradas e devolve um iterador
que aplica a função para cada elemento do iterável. O código abaixo usa map() para encontrar a média de cada lista em
numbers e criar a lista averages. Teste para ver o que acontece. Reescreva esse código para ser mais conciso,
substituindo a função mean por uma expressão lambda definida dentro da
chamada de map().
'''
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]
# função
def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

# função lambda
averages2 = list(map(lambda num_list: sum(num_list) / len(num_list), numbers))
print(averages2)