# 1 : pierre 
# 2 : ciseaux
# 3 : feuille

choix_joueur1 = random.randint(1, 3)
choix_joueur2 = random.randint(1, 3)

if choix_joueur1 == 1:
    choix_joueur1 = "pierre"
elif choix_joueur1 == 2:
    choix_joueur1 = "ciseaux"
else:
    choix_joueur1 = "feuille"
    
if choix_joueur2 == 1:
    choix_joueur2 = "pierre"
elif choix_joueur2 == 2:
    choix_joueur2 = "ciseaux"
else:
    choix_joueur2 = "feuille"

print(f"Le joueur 1 a choisi {choix_joueur1}")
print(f"Le joueur 2 a choisi {choix_joueur2}")

if choix_joueur1 == "pierre":
    if choix_joueur2 == "pierre":
        gagnant = None
    elif choix_joueur2 == "ciseaux":
        gagnant = "joueur1"
    else:
        gagnant = "joueur2"
        
elif choix_joueur1 == "ciseaux":
    if choix_joueur2 == "pierre":
        gagnant = "joueur2"
    elif choix_joueur2 == "ciseaux":
        gagnant = None
    else:
        gagnant = "joueur1"

else:
    if choix_joueur2 == "pierre":
        gagnant = "joueur1"
    elif choix_joueur2 == "ciseaux":
        gagnant = "joueur2"
    else:
        gagnant = None

if gagnant:
    print(f"Le {gagnant} a gagné!")
else:
    print("Egalité")
