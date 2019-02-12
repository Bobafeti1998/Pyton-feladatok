dbszázas = int(input("hány darab 100FT van a kasszában?"))
dbkétszázas = int(input("hány darab 200FT van a kasszában?"))
dbötszázas = int(input("hány darab 500FT van a kasszában?"))

százas = dbszázas*100
kétszázas = dbkétszázas*200
ötszázas = dbötszázas*500

kassza = százas+kétszázas+ötszázas
print("A kasszában: " + str(kassza) + " FT van!")
