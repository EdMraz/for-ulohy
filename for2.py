print(" Vypočítaj súčet  všetkých  párnych čísiel od 1 do N")

n = int(input("zadaj N= "))
x = 0
for i in range(1,n+1):
    if i%2==0:
        x+=i
print("Súčet párnych čísel je",x)

