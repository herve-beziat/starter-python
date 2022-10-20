#Écrire un programme triangle.py qui affiche dans le terminal un triangle avec des ‘_’, des
#‘\’ et des ‘/’
#en fonction de l’input entré, qui représentera la hauteur.
#Exemple si l’input entré est 5

left = "/"
right = "\\"
base = "__"

hauteur = int(input("Hauteur : "))


for i in range (hauteur) :
    print((hauteur - i) * " " + left + ((i*2) * " ") + right)
    if i == hauteur -1 :
        print(left + base * hauteur + right)