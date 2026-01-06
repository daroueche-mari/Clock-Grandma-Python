# Vous créez un programme python qui affiche l’heure sous la forme
# suivante : hh:mm:ss. Par exemple, si l'heure est (16, 30, 0), le programme
# devra afficher 16:30:00. Votre programme doit actualiser l’heure toutes
# les secondes jusqu'à l’arrêt de ce dernier.
print('-----------------------------------------')
print('First Exercice :')

from datetime import datetime 
import time
show = datetime.today()
print("Dates and Hours of Today:", show)
time.sleep(1)
show = datetime.today()
print("Dates and Hours of Today:", show)
time.sleep(1)
show = datetime.today()
print("Dates and Hours of Today:", show)

# Vous ajoutez une fonction nommée “afficher_heure” qui permet de
# régler l'heure. Cette fonction devra prendre en paramètre une heure
# sous la forme d'un tuple (heures, minutes, secondes) et devra mettre à
# jour l'heure affichée grâce à la fonction “afficher_heure”.
print('-----------------------------------------')
print('Second Exercice :')
import time
def show_info(hours, minutes, seconds):
    print("The Hour", hours,":", minutes,":", seconds)
show_info(15, 10, 55)
time.sleep(1)
show_info(15, 10, 56)
time.sleep(1)
show_info(15, 10, 57)
time.sleep(1)
show_info(15, 10, 58)
time.sleep(1)
show_info(15, 10, 59)


# Mamie Jeannine a besoin d’une alarme ! Ajoutez une fonction qui
# permet de régler l'alarme. Cette fonction devra prendre en paramètre
# une heure sous la forme d'un tuple (heures, minutes, secondes) et
# devra afficher un message lorsque l'heure actuelle correspond à l'heure
# de l'alarme.
print('-----------------------------------------')
print('Third Exercice :')
import time
def setting_alarm(hours, minutes, seconds):
    print("The Hour is", hours,':', minutes,':', seconds)
    if hours == 17 and minutes == 15 and seconds == 50:
        print("Alarm")
setting_alarm(15, 10, 55)
time.sleep(1)
setting_alarm(18, 25, 30)
time.sleep(1)
setting_alarm(17, 15, 50)