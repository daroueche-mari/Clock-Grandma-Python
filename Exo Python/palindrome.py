# pour [::-1]
# - start est vide → on commence au début
# - stop est vide → on va jusqu’à la fin
# - step = -1 → on parcourt la séquence à l’envers
# si string est egale a string à l'envers affiche a(True) sinon b(false)

a = True
b = False

def palindrome(string):
      if string == string[::-1]:
            print(a)
      else:
            print(b)

palindrome("ana")
palindrome("victor")            
            

