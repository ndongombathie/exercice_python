distance={('Dakar','Bakel'):663,('Bakel','Kedougou'):483,('Kedougou','Kolda'):448,('Kolda','Ziguinchor'):185}

def convert_dict_to_list(distances,CalculDistance=False,Trie=False):
    #question numero 3
    if(Trie is True):
        NewDic = [(Distance, ville) for ville,Distance in distances.items()]
        NewDic.sort(reverse=True)
        NewDic =[(ville,Distance) for Distance,ville in NewDic]
        return dict(NewDic)
    
    #question numero 2
    if(CalculDistance is True):
       # return sum(distances.values())
        distanceTotal=0
        for distance in distances.values():
            distanceTotal+=distance
        return distanceTotal
    
    #question numero 1
    return list(distances.items())

print(convert_dict_to_list(distances=distance))
print("calcul de la distance total ")
print(convert_dict_to_list(distances=distance,CalculDistance=True))
print("la liste triée par valeur(distance) ")
print(convert_dict_to_list(distances=distance,Trie=True))