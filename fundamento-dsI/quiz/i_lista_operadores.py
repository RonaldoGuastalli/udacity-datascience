month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# Use a indexação de lista para definir a variável num_days com quantos dias existem em um mês específico
tamanho_lista = len(days_in_month)
num_days = days_in_month[tamanho_lista - 1]
print('tamanho da lista days_in_month: ',tamanho_lista)
print(num_days)