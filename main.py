def exercice1():
    print("Exercice 1 : Bonjour le monde !")
    print("Hello World !")

def exercice2():
    prenom = input ('Entrez votre prénom ')
    print(f'Bonjour {prenom}')

def exercice3():
    print('Bienvenue\n à \nvous!')

def exercice4():
    annee = int(input("Entrez votre année de naissance: "))
    annee_mtn=2025
    age = annee_mtn- annee
    print(f'Vous avez approximativement {age} ans')

def exercice5():
    nombre1= int(input("Entrez le premier nombre à calculer: "))
    nombre2 =int(input("Entrez le second nombre à calculer: "))
    resultat= nombre1+nombre2 
    print(resultat)

def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    if choix == "1":
        exercice1()
    if choix == "2":
        exercice2()
    if choix == "3":
        exercice3()
    if choix == "4":
        exercice4()
    if choix == "5":
        exercice5()
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()