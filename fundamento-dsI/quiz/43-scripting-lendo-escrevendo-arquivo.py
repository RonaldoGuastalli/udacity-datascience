"""Lendo um arquivo"""
# A função open devolve um objeto de arquivo
# r ou somente leitura
# Use o método read para acessar o conteúdo do objeto de arquivo
# método close para liberar quaisquer recursos do sistema ocupados pelo arquivo
f = open('../docs/some_file.txt', 'r')
file_data = f.read()
f.close()
print(file_data)

"""Escrevendo em um arquivo"""
# adicionar algo a um arquivo existente, sem excluir seu conteúdo, deve usar o modo acrescentar ('a')
# modo de escrita ('w')
f = open('../docs/my_file.txt', 'w')
f.write("Hello there")
f.close()

"""Muitos arquivos abertos"""
# erro: FileNotFoundError: [Errno 2] No such file or directory: 'some_file.txt'
'''files = []
for i in range(10000):
    files.append(open('some_file.txt', 'r'))
    print(i)'''

"""fecha automaticamente um arquivo assim que você terminar de usá-lo"""
with open('../docs/some_file.txt', 'r') as f:
    file_data_with = f.read()

print('USANDO WITH: \n\n{}'.format(file_data_with))