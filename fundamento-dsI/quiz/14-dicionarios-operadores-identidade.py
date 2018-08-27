# Defina um dicionario chamado population,
# que contenha informação sobre as maiores
# cidades do mundo.
# A chave deve ser o nome da cidade (string)
# e seu valor a respectiva população em
# milhões de pessoas, conforme tabela abaixo:
#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {'Shanghai': 17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print(population)
print('resultado da pesquisa: ', population['Mumbai'])
# population['Brazil'] isso retorna erro: KeyError: 'Brazil'
print(population.get('Brazil'))
print(population.get('Brazil'), 'caso None, msg: a chave pesquisada não foi encontrada')

print('-----------------')

a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b)
print(a is b)
print(a == c)
print(a is c)   #aponta para lugar diferentes da memória