from datetime import datetime
from itertools import count
import time
now = datetime.now()
Time = (int(datetime.now().strftime('%H')),int(datetime.now().strftime('%M')),int(datetime.now().strftime('%S')))

    
def test_alarm(Currentetime,Alarm):
    if Alarm == False:
        return None
    elif Currentetime[0] == Alarm[0] and Currentetime[1] == Alarm[1] and Currentetime[2] == Alarm[2]:
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

def calculatetime(Currentetime):
    Currentetime[2] += 1
    if Currentetime[2] >= 60:
        Currentetime[2] -= 60
        Currentetime[1] += 1
        if Currentetime[1] >= 60:
            Currentetime[1] -= 60
            Currentetime[0] += 1
            if Currentetime[0] >= 24:
                Currentetime[0] -= 24
    return Currentetime

def time_display(Displaytime,AMPM):
    end = ""
    if AMPM == True:
        if Displaytime[0] < 1:
            Displaytime[0] += 12
            end = "pm"
        elif Displaytime[0] >= 12:
            Displaytime[0] -= 12
            end = "am"
        else:
            end = "am"
    Displaytime = list(map(str, Displaytime))
    for i in range(len(Displaytime)):
        if len(Displaytime[i]) < 2 :
            Displaytime[i] = '0' + Displaytime[i]
    clock = Displaytime[0]+':'+Displaytime[1]+':'+Displaytime[2]+end
    return clock

def afficher_heure(Time,Alarm,AMPM):
    Currentime = [Time[0], Time[1], Time[2]]
    for loop in count(0):
        print(time_display(Currentime,AMPM))
        test_alarm(Currentime,Alarm)
        Currentime == calculatetime(Currentime)
        time.sleep(1)


print("Heure actuelle = "+time_display(Time,False))



def menu():
    Alarm = False
    AMPM = False
    while True:
        print("Horloge")
        print("Afficher l'heure: 1")
        print("Régler une alarme: 2")
        print("Régler l'horloge (24h par défaut): 3")
        choice = input("Saissez votre action ; 1/2/3 : ")
        if choice == "1":
            Time = (int(datetime.now().strftime('%H')),int(datetime.now().strftime('%M')),int(datetime.now().strftime('%S')))
            afficher_heure(Time,Alarm,AMPM)
        elif choice == "2":
            Alarm = (test_validint("l'heure de l'alarme",23)),test_validint("les minutes de l'alarme",59),test_validint("les secondes de l'alarme",59)
        elif choice == "3":
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
