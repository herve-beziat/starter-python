#Ecrire un programme rectangle.py qui attend 2 inputs : la largeur puis la hauteur.
#Votre programme devra ensuite dessiner un rectangle avec les éléments suivants :
# des "|" pour dessiner les côtés droite et gauche
# des "-" pour dessiner le haut et le bas
# des espaces pour remplir le rectangle

hauteur = int(input("Hauteur :"))
largeur = int(input("Largeur :"))

side = "|"
separator = "-"

for i in range(hauteur):
    if i==0 or i == hauteur -1:
        separator ="-"
    else :
        separator = " "
    print (side + separator*largeur + side)