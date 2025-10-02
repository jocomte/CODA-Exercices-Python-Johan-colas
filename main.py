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

def Add(a,b):
    return a+b
def exercice5():
    nombre1= int(input("Entrez le premier nombre à calculer: "))
    nombre2 =int(input("Entrez le second nombre à calculer: "))
    resultat= Add(nombre1,nombre2) 
    print(resultat)

def Sous(a,b):
    return a-b

def exercice6():
    nombre1= int(input("Entrez le premier nombre à calculer: "))
    nombre2 =int(input("Entrez le second nombre à calculer: "))
    resultat= Sous(nombre1,nombre2) 
    print(resultat)

def mult(a,b):
    return a*b
def exercice7():
    nombre1= int(input("Entrez le premier nombre à calculer: "))
    nombre2 =int(input("Entrez le second nombre à calculer: "))
    resultat= mult(nombre1,nombre2) 
    print(resultat)

def div(a,b):
    return a/b
def exercice8():
    nombre1= int(input("Entrez le premier nombre à calculer: "))
    nombre2 =int(input("Entrez le second nombre à calculer: "))
    resultat= div(nombre1,nombre2) 
    print(resultat)

def carré(a):
    return a**2
def exercice9():
    nombre=int(input("Entrez votre nombre à mettre au carré: " ))
    resultat=carré(nombre)
    print(resultat)

def double(a):
    return a*2
def exercice10():
    nombre=int(input("Entrez votre nombre à doubler: " ))
    resultat=double(nombre)
    print(resultat)

def moitié(a):
    return a/2
def exercice11():
    nombre=int(input("Entrez votre nombre à diviser par 2: " ))
    resultat=moitié(nombre)
    print(resultat)

def exercice12():
    message = input ('Entrez un message: ')
    print(f'{message}\n{message}\n{message}\n{message}\n{message}')

def exercice13():
    n=0
    for i in range(n+1,6):
        print (i)

def exercice14():
    for i in range(1, 6):  
        print(f"2 × {i} = {2 * i}")

def exercice15():
    cote=int(input("Entrez la longueur du côté du carré: "))
    perimetre=cote*4
    print(f'Le périmètre du carré est de {perimetre} ')

def exercice16():
    cote=int(input("Entrez la longueur du côté du carré: "))
    aire=cote*cote
    print(f'L\'aire du carré est de {aire} ')

def exercice17():
    euro=int(input("Entrez le montant en euros à convertir: "))
    dollar=euro*1.1
    print(f'Le montant en dollars est de {dollar} $')

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
    if choix == "6":
        exercice6()
    if choix == "7":
        exercice7()
    if choix == "8":
        exercice8()
    if choix == "9":
        exercice9()
    if choix == "10":
        exercice10()
    if choix == "11":
        exercice11()
    if choix == "12":
        exercice12()
    if choix == "13":
        exercice13()
    if choix == "14":
        exercice14()
    if choix == "15":
        exercice15()
    if choix == "16":   
        exercice16()
    if choix == "17":   
        exercice17()

    
    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()