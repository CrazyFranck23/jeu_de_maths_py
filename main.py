import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 4


def poser_qeustion():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    o = random.randint(0,1)   # Let 0 -> + and 1 -> *

    operateur_str = "+"
    if o == 1:
        operateur_str = "*"

    reponse_int = 0
    while reponse_int == 0:
        reponse_str = input(f"Calculez {a} {operateur_str} {b} = ")

        try:
            reponse_int = int(reponse_str)
        except ValueError:
            print("ERREUR: Entrer uniquement des nombres comme réponse.")
            print()
        else:
            calcul = a + b
            if o == 1:
                calcul = a * b

            if reponse_int == calcul:
                return True
            else:
                return False


nb_points = 0
for i in range(0, NB_QUESTIONS):
    print(f"Question n°{i+1} sur {NB_QUESTIONS}")
    if poser_qeustion():
        print("Réponse correcte")
        nb_points += 1
    else:
        print("Réponse incorrecte")
    print()

print(f"Votre note est : {nb_points} / {NB_QUESTIONS}")

moyenne = int(NB_QUESTIONS/2)

if nb_points == NB_QUESTIONS:
    print("Excellent !")
elif nb_points == 0:
    print("Révisez vos maths")
elif nb_points > moyenne:
    print("Pas mal")
else:
    print("Peut mieux faire")


