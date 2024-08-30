import random as r

exercice = int(input("Quelle exercice voulez-vous voir?"))

def exercice1():
    nom = input("Quelle est votre nom?")
    print("Bonjour", nom, "Comment allez-vous?")
def exercice2():
    nombre1 = int(input("nombre 1?"))
    nombre2 = int(input("nombre 2?"))
    total = nombre1 + nombre2
    print("La somme de", nombre1, "+", nombre2, "est", total)
def exercice3():
    nombre1 = int(input("nombre 1?"))
    nombre2 = int(input("nombre 2?"))
    if nombre1 == 0 or nombre2 == 0:
        print("undifined")
    else:
        total = nombre1 / nombre2
        print("Le quotient de", nombre1, "et", nombre2, "est", total)
def exercice4():
    impair = 0
    pair = 0
    for i in range(1,10):
        x = i % 2
        if x == 0:
            print(i,"est un nombre pair")
            pair += 1
        else:
            print(i,"est un nombre impair")
            impair += 1
    print(pair,"nombre pair et", impair,"nombre impair")

def exercice5():
    impair = 0
    pair = 0
    min = int(input("nombre minimum"))
    max = int(input("nombre maximum"))
    for i in range(min, max):
        x = i % 2
        if x == 0:
            print(i, "est un nombre pair")
            pair += 1
        else:
            print(i, "est un nombre impair")
            impair += 1
    print(pair, "nombre pair et", impair, "nombre impair")

def exercice6():
    x = r.randint(1,6)
    print("Le résultat de votre lancer =", x)

def exercice7():
    score = 0
    x = int(input("combien de fois voulez-vous lancer le dé?"))
    for i in range(x):
        y = r.randint(1, 6)
        score += y
    print("Vous avez lancé", x,"dé(s) à six faces et obtenu le score de", score)

if exercice == 1:
    exercice1()
elif exercice == 2:
    exercice2()
elif exercice == 3:
    exercice3()
elif exercice == 4:
    exercice4()
elif exercice == 5:
    exercice5()
elif exercice == 6:
    exercice6()
elif exercice == 7:
    exercice7()
else:
    print("incorect")
