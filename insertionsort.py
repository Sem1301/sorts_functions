def insertionsort(lista):
    control = order(lista) #our control value will be used to see if the list is sorted yet
    place = 0 #place will be our current location in the list
    maxplace = len(lista) -1
    while control == 1: #control is determined by order() if order() is 1 that means the list is not ordered and therefore we should keep sorting
        place2 = place +1 #place2 will be the location of the value we will be comparing place to.
        left = lista[place] #value at place
        right = lista[place2] #value at place2
        if left > right: #if the left value has a bigger value then the right value they switch places
            lista[place] = right
            lista[place2] = left
        place = place + 1 #after switching me move up in the list
        if place == maxplace: #if we reach the right side of the list we go back to the start
            place = 0
        control = order(lista)
    return lista
def order(test_list):
    temp = 0
    i = 1
    while i < len(test_list):
        if(test_list[i] < test_list[i - 1]):
            temp = 1
        i += 1
    if (temp == 0) :
        return temp
    else :
        return temp
