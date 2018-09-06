tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for token in tokens:
    if (token.find("<") != -1) and (token.find(">") != -1):
        count = count + 1
print(count)

# outra forma
count2 = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count2 += 1
print(count2)

# imprimir palavras
for token in tokens:
    tamanhos = range(len(token))
    print('tamanho de {} = {}'.format(token, tamanhos))
    for tamanho in tamanhos:
        print(token[tamanho])



