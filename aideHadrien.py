mot = "bonjour"

motVide = []

for lettre in mot:
    motVide.append("_")

for lettre in mot:
    print("_ ", end='')

for i in range(5):
    i = 0
    lt = input("\n")
    for lettre in mot:
        if(lettre == lt):
            motVide[i] = lettre
        i += 1

for lettre in motVide:
    print(end=lettre)
