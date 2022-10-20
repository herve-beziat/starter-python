#Créer un programme job18.py. Le programme devra contenir une fonction qui prend en
#paramètres un nombre de paramètres indéfini (uniquement des nombres).
#La fonction devra :
# - Remplir une liste myList contenant tous ces paramètres.
# - Trier par ordre croissant la liste à l’aide de la fonction sort
# - Afficher la liste dans un terminal


def test(*args):
    mylist = args
    print(sorted(mylist))



test(1,2,5,9,48,56,32,5,6,48,20,21,23)


