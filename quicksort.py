import random

def quicksort(lista):
    if order(lista) == 0: #order() returns 0 if the list is sorted so if order() returns 0 then you just return the list
        return lista
    else:
        length = len(lista)
        randomplace = random.randrange(0,length) #here we take a random place in the list which will give use the variable at that place. We will use this variable to sort the list around.
        rotationpoint = lista[randomplace]
        left = []
        right = []
        for i in lista: #here we start using the rotation variable, if something is lower it will go to the left and if its higher it will go to the right.
            if i > rotationpoint:
                right.append(i)
            else:
                left.append(i)
        left = quicksort(left) #we sort the left again until its sorted
        right = quicksort(right) #we sort the right again until its sorted
        for i in right:
            left.append(i) #we add the right to the left 
        return left #and return a sorted list

def order(test_list):
    temp = 0
    i = 1
    while i < len(test_list):
        if(test_list[i] < test_list[i - 1]):
            temp = 1
        i += 1
    if (temp == 0) :
        return temp
    else:
        return temp
