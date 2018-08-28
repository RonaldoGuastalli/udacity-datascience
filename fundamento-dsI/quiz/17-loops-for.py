names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
print(list(range((len(names)))))
for index in range((len(names))):
    valor = names[index].replace(" ", "_")
    usernames.append(valor.lower())
print(usernames)