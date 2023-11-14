def planned_trip():

    currLoc = input("dari mana?")
    destLoc = input("mau kemana?")
    transType = input("what type of transportation?")

    distance = 0
    fuel =  0
    

    if transType == 'motor':
        fuel = 10000
    elif transType == 'mobil':
        fuel = 20000
    

    if destLoc == 'bandung':
        distance = 20
    elif destLoc == 'depok':
        distance = 10
    else:
        distance == 0

    cost = distance*fuel
    
    print (distance)
    print (cost)

planned_trip()
