óra1 = int(input("Kérlek adj meg egy órát!"))
perc1 = int(input("Kérlek adj meg egy percet!"))
másodperc1 = int(input("Kérlek adj meg egy másodpercet!"))

óra2 = int(input("Kérlek adj meg egy órát!"))
perc2 = int(input("Kérlek adj meg egy percet!"))
másodperc2 = int(input("Kérlek adj meg egy másodpercet!"))


idő1 = (óra1*3600)+(perc1*60)+másodperc1

idő2 = (óra2*3600)+(perc2*60)+másodperc2


if idő1>idő2:
    elteltidő = idő1 - idő2
else:
    elteltidő = idő2 - idő1


óra = elteltidő//3600
óramásodperc = óra*3600

perc = (elteltidő-óramásodperc)//60
percmásodperc = perc*60

másodperc=elteltidő-óramásodperc-percmásodperc

print("A két idő közötti idő "+str(óra)+":"+str(perc)+":"+str(másodperc)+".")







#if óra1>óra2:
#    összóra = óra1 - óra2   
#else:
#    összóra = óra2 - óra1
#if perc1>perc2:
#    összperc = perc1 - perc2
#else:
#    összperc = perc2 - perc1
#if másodperc1>másodperc2:
#    összmásodperc = másodperc1 - másodperc2
#else:
#    összmásodperc = másodperc2 - másodperc1
#print(str(összóra)+":"+str(összperc)+":"+str(összmásodperc))

