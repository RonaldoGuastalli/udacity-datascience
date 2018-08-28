usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
print('antes: ', usernames)
for index in range((len(usernames))):
    valor = usernames[index].replace(" ", "_")
    usernames[index] = valor.lower() #alterando a lista
print('depois: ', usernames)