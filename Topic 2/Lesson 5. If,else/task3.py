mininv = int(input("Минимальная сумма инвестиций: $")) 
mike = int(input("Денег у Майкла: $"))
ivan  = int(input("Денег у Ивана: $"))
total = mike + ivan
if mike >= mininv and ivan >= mininv:
    print (2)
elif mike >= mininv and ivan < mininv:
    print ("Майкл")
elif mike < mininv and ivan >= mininv:
    print ("Иван")
elif total >= mininv:
    print(1)
else:
    print(0)