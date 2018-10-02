'''
Quiz: Chunker
Se você tem um iterável que é grande demais para caber na memória por completo (ex. ao lidar com arquivos grandes),
ser capaz de pegar e utilizar apenas pedaços a cada vez pode ser muito valioso. Implemente uma função de gerador,
chunker, que recebe um iterável e retorna um pedaço de tamanho específico por vez.
'''

def chunker(iterable, size):
    """sucessivos chunker pelo iterável de tamanho size"""
    for index in range(0, len(iterable), size):
        valor = iterable[index: index + size]
        yield valor

for chunk in chunker(range(25), 4):
    """iteravel"""
    print(list(chunk))

"""outro exemplo"""
# lista de quadrados
sq_list = [x**2 for x in range(10)]
print('quadrado: {}'.format(sq_list)) # a lista e apresentada quando sq_list estiver pronta

# iterador de quadrados
sq_iterator = (y**2 for y in range(10))
print(list(sq_iterator)) # chama o iterador varias vezes
