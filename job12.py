#Créer un programme job12.py qui parcourt le contenu du fichier “data.txt” et qui compte
#le nombre de mots (sans caractère spéciaux) qui s’y trouvent.

words = 0
with open ("data.txt", "r") as file :
    data = file.read()
    lines = data.split()
    words = len(lines)
    print (words)
