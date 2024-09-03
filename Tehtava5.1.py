import random

kuutioiden_maara = int(input("Anna arpakuutioiden määrä: "))
heitot = 1
listatut_heitot =[]
while heitot <= kuutioiden_maara:
    listaan = int(random.randint(1,6))
    listatut_heitot.append(listaan)
    heitot = heitot + 1

print(f"Heitetään arpakuutiot! Saatiin silmäluvut: \n {listatut_heitot}")
summa = 0
for heitto in listatut_heitot:
    summa = summa + heitto

print()
print(f"Näiden arpakuutioiden summa on {summa}!")