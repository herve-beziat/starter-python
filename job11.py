#Créer un programme job11.py qui parcourt le contenu du fichier “domains.xml” et qui
#compte le nombre de noms de domaine.



# ouverture et lecture du fichier
with open ("c:/Users/Rvbez/Desktop/La plateforme/Python/domains.xml", "r") as file :
    text = file.read()
    f = len(text.split('"domain'))
print (f)
