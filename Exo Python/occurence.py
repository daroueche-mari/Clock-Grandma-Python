# # Calculer le nombre d'occurences d'un caractère

# Contraintes :

# La fonction prend deux paramètres de type string :
# - une chaine de caractere
# - un caractere à rechercher

# la fonction retourne un entier(int) correspondant au nombres 
# d'occurences du caractere dans la chaine


def count_occurences(s: str, char: str) -> int:
    count = 0
    for c in s:
        if c == char:
            count += 1
            return count
count_occurences('Bonjour','o') 

