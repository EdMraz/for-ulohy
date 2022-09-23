print("naprogramuj funkciu, ktorá vráti počet všetkych párnych čísel od 1-N")

n = int(input("zadaj N= "))
x = 0

for i in range(1,n+1):
    if i%2==0:
        x+=1

print("Počet párnych čísel je",x)
