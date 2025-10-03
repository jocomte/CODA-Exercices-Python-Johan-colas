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

def exercice18():
    temps=int(input("Entrez le temps en minutes à convertir: "))
    secondes=temps*60
    print(f'Le temps en secondes est de {secondes} s')

def exercice19():
    prix_ht=float(input("Entrez le prix hors taxe: "))
    tva=prix_ht+prix_ht*0.2
    print(f'Le prix ttc est de {tva} €')

def exercice20():
    nom=input("Entrez votre nom: ")
    age=int(input("Entrez votre âge: "))
    print(f'Bonjour mon cher {nom}, vous avez actuellement {age} ans si je ne me trompes pas.')

def exercice21():
    nombre=int(input('Entrez votre nombre: '))
    if nombre==0:
        print('Le nombre est nul')
    elif nombre>0:
        print('Le nombre est positif')
    else:
        print('Le nombre est négatif')    

def exercice22():
    age=int(input("Entrez votre âge: "))
    if age<18:
        print('Vous êtes mineur')
    else:
        print('Vous êtes majeur')

def exercice23():
    note=int(input("Entrez votre note: "))
    if note<10:
        print('Non validé')
    else:
        print('Validé')

def exercice24():
    print (22)
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le deuxième nombre : "))

    print(f"{a if a > b else b} est plus grand")

def exercice25():
    a = int(input("Entrez le premier nombre : "))
    b = int(input("Entrez le deuxième nombre : "))

    if a < b:
        print("Ordre croissant : OUI")
    else:
        print("Ordre croissant : NON")

def exercice26():
    nombre=int(input("Entrez un nombre :"))
    if nombre % 5 == 0:
        print (f"{nombre} est un multiple de 5")
    else:
        print(f"{nombre} n'est pas un multiple de 5")

def exercice27():
    nombre =int(input("Entrez votre âge: "))
    if nombre<12:
        print('Vous êtes un enfant')
    elif 12<=nombre<18:
        print('Vous êtes un adolescent')
    else:
        print('Vous êtes un adulte')

def exercice28():
    temperature=int(input("Entrez la température de l'eau: "))
    if temperature<0:
        print ("L'eau est de la glace")
    elif 0<=temperature<100:
        print("L'eau est liquide")
    else:
        print("L'eau est de la vapeur")
    
def exercice29():
    note_bac=int(input("Entrez votre note au bac: "))
    if 0<=note_bac<10:
        print('Recalé')
    elif 10<=note_bac<12:
        print('Passable')
    elif 12<=note_bac<16:
        print('Bien')
    else:
        print('Très bien')

def main():
    # Demande à l'utilisateur quel exercice exécuter
    choix = input("Entrez le numéro de l'exercice à exécuter : ")
    nom_fonction = f"exercice{choix}"
    if nom_fonction in globals():
        globals()[nom_fonction]()

    else:
        print("Exercice non reconnu.")
if __name__ == "__main__":
    main()