from random import randint

cont = True

while cont == True:
    number = randint(1,6)
    print(number)
    userAns = input("Do you want to continue? ")
    if userAns == "yes" or "Yes":
        cont = True
    else:
        cont = False



