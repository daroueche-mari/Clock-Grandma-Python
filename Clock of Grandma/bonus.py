# Ajoutez une fonction qui permet de choisir entre différents modes d'affichage
# de l'heure: 12 heures ou 24 heures. Si le mode 12 heures est sélectionné, l'heure
# devra être affichée sous la forme hh:mm:ss AM/PM. Par exemple, si l'heure
# est (16, 30, 0), elle devra être affichée comme 04:30:00 PM.
print('-----------------------------------------')
print('First Exercice Bonus :')

from datetime import datetime
import time

now = datetime.now()

def selector(mode):
     if mode == 12:
          print(now.strftime("%I:%M:%S %p"))
     else:
          if mode == 24:
               print(now.strftime("%H:%M:%S"))
selector(12)
time.sleep(1)
selector(24)


# Ajoutez une fonction qui permet de mettre en pause l'horloge. Cette fonction
# devra suspendre l'actualisation de l'heure jusqu'à ce qu'elle soit de nouveau
# relancée. Cette fonctionnalité ne sera pas spécialement utile à mamie mais
# vous voulez vous en servir pour lui faire de petites farces.
print('-----------------------------------------')
print('Second Exercice Bonus :')

from datetime import datetime
import time


now = datetime.now()

def stop(trigger):
     if trigger == 1:
          exit()
     else:
          print(now.strftime("%H:%M:%S"))

stop(0)
time.sleep(1)
stop(0)
time.sleep(1)
# le programme s'arrete là
stop(1)
time.sleep(1)
stop(0)
