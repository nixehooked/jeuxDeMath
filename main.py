import random

NOMBRE_MIN = 1
NOMBRE_MAX = 20
NOMBRE_TOURS = 4
NOMBRE_POINTS = 0
check = False


def demanderCalcul():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(1, 4)

    if o == 1:
        o = "+"
        calcul = a + b
    elif o == 2:
        o = "-"
        calcul = a - b
    elif o == 3:
        o = "x"
        calcul = a * b
    else:
        o = "/"
        calcul = a / b

    print(f"Combien font : {a} {o} {b}")
    return calcul


for i in range(0, NOMBRE_TOURS):
    print()
    print(f"Question n°{i + 1} sur {NOMBRE_TOURS}")
    print()
    reponse_calcul = demanderCalcul()
    reponse_user = input("Votre réponse: ")

    try:
        user_num = int(reponse_user)
    except ValueError:
        print("Vous devez saisir un nombre")

    if user_num == reponse_calcul:
        NOMBRE_POINTS += 1

if NOMBRE_POINTS <= 2:
    print(f"Peu mieu faire, voici ton résultat: {NOMBRE_POINTS} / {NOMBRE_TOURS}")
elif NOMBRE_POINTS > 2:
    print(f"C'est un beau score, voici ton résultat: {NOMBRE_POINTS} / {NOMBRE_TOURS}")
elif NOMBRE_POINTS == 0:
    print(f"Révise tes maths, voici ton résultat: {NOMBRE_POINTS} / {NOMBRE_TOURS}")
else:
    print(f"C'est un parfait, voici ton résultat: {NOMBRE_POINTS} / {NOMBRE_TOURS}")
