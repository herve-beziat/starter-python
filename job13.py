#Créer un programme job13.py qui demande à l’utilisateur de renseigner un nombre entier. 
#Le programme devra alors parcourir le contenu du fichier “data.txt” compter le nombre de mots de la taille renseignée qui s’y trouvent.

lettres = int(input("Nombre de lettres : "))

with open ("data.txt", "r") as file :
    data = file.read()
    data = data.replace(","," ")
    data = data.replace(";"," ")
    data = data.replace("'"," ")
    data = data.replace(":"," ")
    data = data.replace("?"," ")
    data = data.replace("!"," ")
    data = data.replace("."," ")
    words = data.split()
    #print (words)

compte = 0

for i in words :
    if len(i)==lettres:
        compte=compte+1

print(compte)
