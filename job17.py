#Créer un programme job17.py. Le programme devra contenir une fonction qui prend en
#paramètres un nombre de paramètres indéfini (uniquement des nombres).
#La fonction devra :
# - Remplir une liste myList contenant tous ces paramètres.
# - Parcourir et afficher dans le terminal uniquement les nombres pairs de la liste.

def test(*args):
    mylist = args

    
    for r in mylist:
        if r%2==0:
            print(r)



test(1,3,5,8,12,6,8,9,7,3,7,17,14,19)

