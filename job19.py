#Créer un programme job19.py. Le programme devra contenir une seule fonction qui
#prend en paramètres un nombre de paramètres indéfini (uniquement des nombres).
#La fonction devra :
# - Remplir une liste myList contenant tous ces paramètres.
# - Trier par ordre croissant la liste à l’aide de la fonction sort (Donc sans la fonction
#sort)
# - Afficher la liste dans un terminal





def test(*args):
    mylist = list(args)
    r=[]
    while mylist:
        mini=min(mylist)
        mylist.remove(mini)
        r.append(mini)

    print(r)

test(1,5,9,6,15,64,25,3,41,8,65,4,9,25,6,45)

#def trier(liste):
#    r=[]
#    while liste:
#        mini=min(liste)
#        liste.remove(mini)
#        r.append(mini)
#    return r
 
     
#print (trier([41,17,3,4,17,51]))