import random

NOMBRE_MIN = 1
NOMBRE_MAX = 10
NB_QUESTIONS = 4


def poser_qeustion():
    a = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    b = random.randint(NOMBRE_MIN, NOMBRE_MAX)
    reponse_str = input(f"Calculez {a} + {b} = ")
    reponse_int = int(reponse_str)
    if reponse_int == a+b:
        print("Réponse correcte")
    else:
        print("Réponse incorrecte")


for i in range(0, NB_QUESTIONS):
    print(f"Question n°{i+1} sur {NB_QUESTIONS}")
    poser_qeustion()
    print()
