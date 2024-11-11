from flask import Flask


luku = int(input("Syötä tähän luku tarkistaaksesti, onko se alkuluku: "))

def alkuluku():


#luvut 0 ja 1 eivät ole alkulukuja
if luku > 1:

    for i in range(2, luku//2+1):

        if luku % i == 0:
            print(f"Luku {luku} ei ole alkuluku.")
            break
    else:
        print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")

