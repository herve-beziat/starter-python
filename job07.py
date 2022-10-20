#Écrire un programme qui parcourt les nombres entiers de 1 à 100. Pour les multiples de
#trois, afficher "Fizz" au lieu du nombre et pour les multiples de cinq afficher "Buzz". Pour
#les nombres qui sont des multiples de trois et cinq, afficher "FizzBuzz".

for value in range (1, 101) :
    if value%3==0 and value%5==0:
        print ("FizzBuzz")
    elif value%5==0:
        print ("Buzz")
    elif value%3==0:
        print ("Fizz")
    else:
        print(value)

        