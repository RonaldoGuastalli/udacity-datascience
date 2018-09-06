"""Quiz: Gerador de senha
Escreva uma função chamada generate_password que seleciona três palavras aleatórias de um arquivo de palavras fornecido
e as concatena em uma única string. O código para ler os dados do arquivo já está no código inicial, você precisará
construir uma senha a partir destas peças."""

# Use an import statement at the top
import random

word_file = "../docs/words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

print(len(word_list))

# Add your function generate_password here
def generate_password():
    word_1 = word_list[random.randint(0, len(word_list)-1)]
    word_2 = word_list[random.randint(0, len(word_list)-1)]
    word_3 = word_list[random.randint(0, len(word_list)-1)]
    return ''.join(random.sample(word_list, 3))
    # return random.choice(word_list)+random.choice(word_list)+random.choice(word_list)
    # return str(word_1 + word_2 + word_3)

# test your function
print(generate_password())