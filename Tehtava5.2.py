luvut = []

luku = input("Anna luku: ")
while luku != "":
    luku = int(luku)
    luvut.append(luku)
    luku = input("Anna luku tai paina 'Enter' lopettaaksesi: ")

luvut.sort(reverse=True)
print()
print(f"Viisi suurinta lukua ovat:\n {luvut[0:5]}.")