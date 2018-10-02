# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.
print("Cabeçalho dos dados.")
print(data_list[0])


# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for index in range(1, 21):
    print("amostra {} - {}".format(index, data_list[index]))

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
samples = []
for linha in range(len(data_list)):
    valor_linha = data_list[linha]
    samples.append(valor_linha[6])

for index in range(0, 20):
    print("gênero amostras {} - {}".format(index, samples[index]))

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
# Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
def column_to_list(data, index):
    """Função adiciona as colunas de uma lista em outra lista.
      Argumentos:
          data: uma lista com várias colunas.
          index: index da coluna que será inserido na nova lista.
      Retorna:
          Uma lista da coluna de index x, na mesma oredem."""
    column_list = []
    for valor in data:
        column_list.append(valor[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = column_to_list(data_list, -2).count("Male")
female = column_to_list(data_list, -2).count("Female")


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """Função contador de gêneros.
          Argumentos:
              data_list: lista que contem os gêneros a serem contados.
          Retorna:
              Retorna uma lista com os quantidade dos gêneros encontrado."""
    male = column_to_list(data_list, -2).count("Male")
    female = column_to_list(data_list, -2).count("Female")
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """Função classifica qual o gênero mais popular em um lista.
              Argumentos:
                  data_list: lista que contem os gêneros analisados.
              Retorna:
                  Retorna uma string informando o gênero mais popular da lista."""
    total_gender = count_gender(data_list)
    if total_gender[0] > total_gender[1]:
        answer = "Masculino"
    elif total_gender[0] < total_gender[1]:
        answer = "Feminino"
    else:
        answer = "Igual"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

def count_itens(data_list, index, string):
    """Função contador de itens.
              Argumentos:
                  data_list: lista que contem os itens a serem contados.
                  index: o index do item que deseja contar.
                  string: a string que será contada na lista especificada
              Retorna:
                  Retorna a quantidade que o item de index x foi encontrado na lista."""
    valor = column_to_list(data_list, index).count(string)
    return valor

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
user_types_subscriber = count_itens(data_list, -3, "Subscriber")
user_types_customer = count_itens(data_list, -3, "Customer")
types_user_types = ["Subscriber", "Customer"]
quantity_user_types = [user_types_subscriber, user_types_customer]
y_pos_user_types = list(range(len(types_user_types)))
plt.bar(y_pos_user_types, quantity_user_types)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuários')
plt.xticks(y_pos_user_types, types_user_types)
plt.title('Quantidade por Tipo de Usuários')
plt.show(block=True)

print("\nTAREFA 7: Verifique o gráfico!")


input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Por que male + female != len(data_list), ou seja, ({} + {}) != {}".format(count_gender(data_list)[0], count_gender(data_list)[1], len(data_list))
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.
trip_duration_list = [float(i) for i in trip_duration_list]
trip_duration_list.sort()
for inicial in trip_duration_list:
    if inicial != " " and inicial != 0.0:
        min_trip = inicial
        break
trip_duration_list.sort(reverse=True)
for inicial in trip_duration_list:
    if inicial != " " and inicial != 0.0:
        max_trip = inicial
        break

def calcula_media(data):
    """Função calculo da média de uma lista.
              Argumentos:
                  data: lista de float que contem os valores.
              Retorna:
                  Retorna um float como a média calculada."""
    soma = 0.0
    for item in data:
        soma += item
    media = soma / len(data)
    return media

trip_duration_list.sort()
mean_trip = calcula_media(trip_duration_list)

def calcula_mediana(data):
    """Função calcula a mediana em uma lista.
              Argumentos:
                  data: lista de float que contem os valores..
              Retorna:
                  Retorna um float que é mediana da lista."""
    posicao_valor_mediano = (len(data) + 1) / 2
    if posicao_valor_mediano % 2 == 0:
        median_trip = data[posicao_valor_mediano]
    else:
        median_trip = ((data[int(posicao_valor_mediano)]) + (data[int(posicao_valor_mediano) + 1]))/2
    return float(median_trip)

trip_duration_list.sort()
median_trip = calcula_mediana(trip_duration_list)


print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:"
"""Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x."""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """Função que conta o número de tipos de parêmtros em um lista.
              Argumentos:
                  data: lista a ser analisada.
              Retorna:
                  item_types: coleção dos tipos de itens encontrados na lista.
                  count_items: quantidade de tipos de itens encontrados na lista"""
    count_items = []
    item_types = []
    item_set = set(column_list)
    item_types = list(item_set)

    for j in range(len(item_types)):
        count_items.append(0)

    for i in column_list:
        if i in item_types:
            count_items[item_types.index(i)] += 1

    return item_types, count_items

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
# -----------------------------------------------------