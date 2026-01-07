from datetime import datetime
from itertools import count
import time
import threading
now = datetime.now()
Time = (int(datetime.now().strftime('%H')),int(datetime.now().strftime('%M')),int(datetime.now().strftime('%S')))

  


def test_alarm(Currentime,Alarm):
    if Alarm == False:
        return None
    elif Currentime[0] == Alarm[0] and Currentime[1] == Alarm[1] and Currentime[2] == Alarm[2]:
        print("Alarme")


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

def attendre_retour(stop):
    input("\nAppuyez sur Entrée pour revenir au menu\n")
    stop.append(True)

def time_display(Displaytime,AMPM):
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


def afficher_heure(Time, Alarm, AMPM):
    stop = []
    thread = threading.Thread(target=attendre_retour, args=(stop,))
    thread.daemon = True
    thread.start()
    Currentime = [Time[0], Time[1], Time[2]]
  

    while not stop:
        print(time_display(Currentime.copy(), AMPM))
        test_alarm(Currentime, Alarm)
        Currentime = calculatetime(Currentime)
        time.sleep(1)

    print("Retour au menu...")



def menu():
    Alarm = False
    AMPM = False
    Timeset = False
    while True:
        print("Horloge")
        print("Afficher l'heure: 1")
        print("Régler une alarme: 2")
        print("Régler l'heure: 3")
        print("Régler l'horloge (24h par défaut): 4")
        choice = input("Saisissez votre action ; 1/2/3/4 : ")
        if choice == "1":
            if Timeset != True:
                Time = (int(datetime.now().strftime('%H')),int(datetime.now().strftime('%M')),int(datetime.now().strftime('%S')))
            afficher_heure(Time,Alarm,AMPM)
        elif choice == "2":
            Alarm = (test_validint("l'heure de l'alarme",23)),test_validint("les minutes de l'alarme",59),test_validint("les secondes de l'alarme",59)
        elif choice == "3":
            Time = (test_validint("l'heure",23)),test_validint("les minutes",59),test_validint("les secondes",59)
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



