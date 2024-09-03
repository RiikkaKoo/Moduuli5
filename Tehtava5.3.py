luku = int(input("Anna kokonaisluku: "))

for jakaja in range(2, (luku + 1)):
    #print(f"Toisto: {jakaja}")
    jakojaannos = luku % jakaja
    #print(f"Jakojäännös: {jakojaannos}")
    if jakojaannos == 0 and jakaja < luku:
        print("Tämä luku ei ole alkuluku.")
        break
    elif jakojaannos == 0 and jakaja == luku:
        print("Tämä luku on alkuluku.")