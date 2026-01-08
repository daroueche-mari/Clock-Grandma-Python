from datetime import datetime
from itertools import count
import time
import threading
now = datetime.now()
Time = (int(datetime.now().strftime('%H')),int(datetime.now().strftime('%M')),int(datetime.now().strftime('%S')))

  

#Vérifie si l'heure de l'alarme correspond à l'heure actuelle
def test_alarm(Currentime,Alarm):
    if Alarm == False:
        return None
    elif Currentime[0] == Alarm[0] and Currentime[1] == Alarm[1] and Currentime[2] == Alarm[2]:
        print("Alarme")

#Vérifie si l'input est bien un integer valide
def test_validint(timespan,max):
    
    while True:
        value = input("Choisie "+timespan+" : ")
        try:
            truevalue = int(value)
            if 0 <= truevalue <= max:
                return truevalue
            else:
                print('Valeur non valide')
                test_validint(timespan,max)
        except:
            print("Veuillez entrer un nombre")

#Ajoute une seconde et recalcule l'heure
def calculatetime(Currentime):
    Currentime[2] += 1
    if Currentime[2] >= 60:
        Currentime[2] -= 60
        Currentime[1] += 1
        if Currentime[1] >= 60:
            Currentime[1] -= 60
            Currentime[0] += 1
            if Currentime[0] >= 24:
                Currentime[0] -= 24
    return Currentime

#Permet d'arrêter l'horloge
def attendre_retour(stop):
    input("\nAppuyez sur Entrée pour revenir au menu\n")
    stop.append(True)

#Permet de régler l'alarme
def set_alarm(Time):
    Alarm = Time
    return Alarm

#Permet de régler l'heure
def set_time(hours,minutes,seconds):
    Time = (hours,minutes,seconds)
    return Time

#Met l'heure en forme selon le format (24h/12h) pour l'affichage
def time_formating(Displaytime,AMPM):
    end = ""
    if AMPM == True:
        if Displaytime[0] < 1:
            Displaytime[0] += 12
            end = "am"
        elif Displaytime[0] == 12:
            end = "pm"
        elif Displaytime[0] > 12:
            Displaytime[0] -= 12
            end = "pm"
        else:
            end = "am"
    Displaytime = list(map(str, Displaytime))
    for i in range(len(Displaytime)):
        if len(Displaytime[i]) < 2 :
            Displaytime[i] = '0' + Displaytime[i]
    clock = Displaytime[0]+':'+Displaytime[1]+':'+Displaytime[2]+end
    return clock

#Boucle principale
def display_time(Time, Alarm, AMPM):
    stop = []
    thread = threading.Thread(target=attendre_retour, args=(stop,))
    thread.daemon = True
    thread.start()
    Currentime = [Time[0], Time[1], Time[2]]
    while not stop:
        print(time_formating(Currentime.copy(), AMPM))
        test_alarm(Currentime, Alarm)
        Currentime = calculatetime(Currentime)
        time.sleep(1)
    print("Retour au menu...")

#Affiche le menu et les réglages
def menu():
    Alarm = False
    AMPM = False
    Timeset = False
    while True:
        print("Horloge")
        print("Afficher l'heure: 1")
        print("Régler une alarme: 2")
        print("Régler l'heure: 3")
        print("Régler le format de l'horloge (24h par défaut): 4")
        choice = input("Saisissez votre action ; 1/2/3/4 : ")
        if choice == "1":
            if Timeset != True:
                Time = (int(datetime.now().strftime('%H')),int(datetime.now().strftime('%M')),int(datetime.now().strftime('%S')))
            display_time(Time,Alarm,AMPM)
        elif choice == "2":
            Setalarm = (test_validint("l'heure de l'alarme",23),test_validint("les minutes de l'alarme",59),test_validint("les secondes de l'alarme",59))
            Alarm = set_alarm(Setalarm)
        elif choice == "3":
            Time = set_time(test_validint("l'heure",23),test_validint("les minutes",59),test_validint("les secondes",59))
            Timeset = True
        elif choice == "4":
            while True:
                print("24 heures: 1")
                print("12 heures: 2")
                choice = input("Choisissez votre format d'horloge : ")
                if choice == "1":
                    AMPM = False
                    break
                elif choice == "2":
                    AMPM = True
                    break
                else:
                    print("Chiffre non valide")
        else:
            print("Chiffre non valide")

menu() 
