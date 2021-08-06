alphabet = [lettre for lettre in "abcdefghijklmnopqrstuvwxyz"]
transformations = {
    alphabet[i]: alphabet[(i+cle)%len(alphabet)] for i in range(len(alphabet))
}
transformations_inverses = {valeur: cle for cle, valeur in transformations.items()}
chiffre = "".join(transformations.get(lettre, lettre) for lettre in texte.lower())
chiffre_decode = "".join(transformations_inverses.get(lettre, lettre) for lettre in chiffre.lower())
