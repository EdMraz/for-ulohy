print("Naprogramuj funkciu, ktorá v intervale od  <začiatok,  koniec>  zistí počet čísel, ktoré sú deliteľné ôsmimi")

z = int(input("Zadaj začiatočnú hodnotu intervalu: "))
k = int(input("Zadaj konečnú hodnotu intervalu: "))
x = 0

for i in range(z,k+1):
    if i%8==0:
        x+=1

print("Počet čísel v intervale, ktoré sú deliteľné ôsmimi je",x)
