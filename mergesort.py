def sorteer(gesorteerde_lijst):
    if len(gesorteerde_lijst) <= 1:
        return gesorteerde_lijst
    
    m = len(gesorteerde_lijst) // 2
    l = gesorteerde_lijst [:m]
    r = gesorteerde_lijst [m:]

    l = sorteer(l)
    r = sorteer(r)
    return merge(l, r)

def merge(lijst1, lijst2):
    wombocombo_lijst = []
    index1 = 0
    index2 = 0
    lengte1 = len(lijst1)
    lengte2 = len(lijst2)

    while index1 < lengte1 and index2 < lengte2:

        if lijst1[index1] <= lijst2[index2]:
            wombocombo_lijst.append(lijst1[index1])
            index1 = index1 + 1
        else:
            wombocombo_lijst.append(lijst2[index2])
            index2 = index2 + 1

    while index1 < lengte1:
        wombocombo_lijst.append(lijst1[index1])
        index1 = index1 + 1
    while index2 < lengte2:
        wombocombo_lijst.append(lijst2[index2])
        index2 = index2 + 1
    return wombocombo_lijst 


print(sorteer([4, 3, 2, 1]))
    


