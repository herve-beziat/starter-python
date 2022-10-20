#Créer un programme job15.py. Le programme devra contenir une fonction 
#qui prend en paramètres une variable prenom et une variable nom.
#La fonction écrira “Bonjour prenom nom” dans le terminal.

nom = input("Quel est votre nom: ")
prenom = input("Quel est votre prenom: ")

def myname(prenom, nom):
    print("Bonjour" + " " + prenom + " "+ nom)

myname(prenom,nom)