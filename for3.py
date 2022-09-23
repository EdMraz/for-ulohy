print(" Naprogramuj funkciu, ktorá zistí počet všetkých čísel od , ktoré sú deliteľné siedmymi a štyrmi.")

n = int(input("zadaj N= "))
x = 0
for i in range(1,n+1):
    if i%4==0 and i%7==0:
        x+=1

print("Počet čísel deliteľných siedmymi a štyrmi je",x)
