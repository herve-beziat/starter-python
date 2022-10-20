#Créez un script job05.py
#L’utilisateur devra entrer deux valeurs en input.
#A l’aide d’une boucle for et d’une fonction system, affichez uniquement les nombres se
#trouvant entre l’input 1 et l’input 2. Le programme doit toujours partir de l’input 1 et
#aller jusqu’à l’input 2.
#Si les deux sont égaux, le programme devra écrire “Valeurs égales”.

valeur1=input("Valeur 1 : ")
valeur1=int(valeur1)


valeur2=input("Valeur 2 : ")
valeur2=int(valeur2)


for x in range(valeur1+1,valeur2) or range(valeur1-1,valeur2, -1):
    print(x)

if valeur1==valeur2:
    print("Valeurs égales")