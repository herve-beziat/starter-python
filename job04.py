#Créez un script job04.py
#L’utilisateur devra entrer une valeur en input.
#A l’aide d’une boucle while et d’une fonction system, affichez nombres se trouvant de 0
#(inclus) à l’input (inlus).

valeur=input("Entrer une valeur: ")
valeur=int(valeur)
x=0
while x<valeur+1 :
    print(x)
    x=x+1