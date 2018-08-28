#First Example - try changing the value of phone_balance
phone_balance = 10
bank_balance = 50

if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10

print(phone_balance)
print(bank_balance)

#Second Example - try changing the value of number

number = 145
if number % 2 == 0:
    print("Number " + str(number) + " is even.")
else:
    print("Number " + str(number) + " is odd.")

#Third Example - try to change the value of age
age = 35

# Here are the age limits for bus fares
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65

# These lines determine the bus fare prices
concession_ticket = 1.25
adult_ticket = 2.50

# Here is the logic for bus fare prices
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket

message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age, ticket_price)
print(message)



print('------------------')
de1_50 = 'wooden rabbit'
de51_150 = 'no prize'
de151_180 =	'wafer-thin mint'
de181_200 =	'penguin'
points = 40
if (points >= 1) and (points <= 50):
    result = "Congratulations! You won a {}!".format(de1_50)
elif (points >= 51) and (points <= 150):
    result = "Congratulations! You won a {}!".format(de51_150)
elif (points >= 151) and (points <= 180):
    result = "Congratulations! You won a {}!".format(de151_180)
elif (points >= 181) and (points <= 200):
    result = "Congratulations! You won a {}!".format(de181_200)
else:
    result = "Oh dear, no prize this time."
print(result)

# outra forma de fazer

print('------------------')
if points <= 50:
    result = "Congratulations! You {}".format(de1_50)
elif points <= 150:
    result = "Congratulations! You {}".format(de51_150)
elif points <= 180:
    result = "Congratulations! You wona {}".format(de151_180)
elif points <= 200:
    result = "Congratulations! You {}".format(de181_200)
else:
    result = "Oh dear, no prize this time."

print(result)