''' Quiz: Quebrando uma string Escreva um loop com uma declaração break para criar uma string, news_ticker,
que tenha exatamente 140 caracteres de tamanho. Você deve criar o ticker de notícias adicionando manchetes da lista
headlines, inserindo um espaço entre cada uma. Se necessário, você pode truncar a última manchete no meio,
para que news_ticker tenha exatamente 140 caracteres de tamanho. Lembre-se de que a break funciona tanto para loops
while como para for. Use o loop que parecer mais apropriado. Considere adicionar declarações print a seu código para
ajudá-lo a resolver bugs. '''

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic", 'eu', 'm']


news_ticker = ""
# write your loop here
for headline in headlines:
    news_ticker += headline + " "
    if len(news_ticker) >= 140:
        news_ticker = news_ticker[:140]
        break

print(news_ticker)

# TODO: outra forma
'''
tamanho_headlines = len(headlines)
contadorCaracteres = 0
i = 0
while (i < (tamanho_headlines -1)):
    string_atual = headlines[i].replace(' ', '')
    tamanho_string_atual = len(string_atual)
    print('headline atual: {} ({})'.format(string_atual, tamanho_string_atual))
    if contadorCaracteres >= 140:
        news_ticker = news_ticker[:140] # retira o ultimo espaço
        contadorCaracteres = len(news_ticker)
        print('breaking loop!')
        break
    elif tamanho_string_atual + contadorCaracteres > 140:
        print('valor pulado: {} ({})'.format(string_atual, tamanho_string_atual))
        i += 1
        continue
    else:
        news_ticker += string_atual[:140] + " "
        print('adicionado: {} ({})'.format(string_atual, tamanho_string_atual))
        i += 1
        contadorCaracteres = len(news_ticker)

print('news_ticker: {} ({} caracteres)'.format(news_ticker, contadorCaracteres))
'''

