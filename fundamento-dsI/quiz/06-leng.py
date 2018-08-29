given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

#nome completo
nome_completo = given_name+ ' ' + middle_names+ ' ' + family_name
print(nome_completo)

#calcular o tamanho desse nome
name_length = len(nome_completo)

# Confirme se o nome tem o número de caracteres permitido na Carteira de Motorista
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)