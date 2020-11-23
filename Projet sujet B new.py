
import pandas as pd
from datetime import datetime
import calendar
import matplotlib.pyplot as plt
import numpy as np
import sys


    


    
    

    


tab = pd.read_csv('EIVP_KM.csv', sep=';')
tab
print (tab)

date= tab.sent_at
print (date)

L=[]
for j in range (1,7):
    compteur=0
    for i in range (7880):
        if tab.id[i]==j:
            compteur += 1
    L.append(compteur)
print (L)
print (sum(L))

def convtime(strtime):
    """Converts a string date "YYYY-MM-DD HH;MM;SS" as a time in sec"""
    moment = datetime.strptime(strtime, '%Y-%m-%d %H:%M:%S+02:00')
    return calendar.timegm(moment.timetuple())

def convtime2(strtime):
    """Converts a string date "YYYY-MM-DD" as a time in sec"""
    moment = datetime.strptime(strtime, '%Y-%m-%d')
    return calendar.timegm(moment.timetuple())

# temps=[]
# for i in date:
#     temps.append(convtime(i))
# print (temps)

def identite(numero):
    noise=[]
    temperature=[]
    humidity=[]
    lum=[]
    co2=[]
    duree=[]
    for i in range (7880):
        if tab.id[i] == numero:
            noise.append(tab.noise[i])
            temperature.append(tab.temperature[i])
            humidity.append(tab.humidity[i])
            lum.append(tab.lum[i])
            co2.append(tab.co2[i])
            duree.append(convtime(tab.sent_at[i]))
    return noise,temperature,humidity,lum,co2,duree

def noise(id):
    L=[]
    for i in range (7880):
        if tab.id[i] == id:
            L.append(tab.noise[i])
    return L

def temperature(id):
    L=[]
    for i in range (7880):
        if tab.id[i] == id:
            L.append(tab.temperature[i])
    return L

def humidity(id):
    L=[]
    for i in range (7880):
        if tab.id[i] == id:
            L.append(tab.humidity[i])
    return L

def lum(id):
    L=[]
    for i in range (7880):
        if tab.id[i] == id:
            L.append(tab.lum[i])
    return L

def co2(id):
    L=[]
    for i in range (7880):
        if tab.id[i] == id:
            L.append(tab.co2[i])
    return L

def reçu(id):
    L=[]
    for i in range (7880):
        if tab.id[i] == id:
            L.append(convtime(tab.sent_at[i]))
    return L

# print (reçu(6))
# print (len(reçu(6)))
# def duree(id):
#     temps = date(id)[-1] - date(id)[0]
#     return(temps)
    
###afficher les données du capteur lié au bruit sur un graphe####
for i in range (2,7):
    plt.plot(reçu(1),noise(1))
    plt.legend('capteur 1')
    plt.plot(reçu(i), noise(i))
plt.title("Capteur bruit")
plt.show()

###afficher les données du capteur lié à la température sur un graphe####
for i in range (2,7):
    plt.plot(reçu(1), temperature(1))
    plt.plot(reçu(i), temperature(i)) 
plt.title("Capteur temperature")
plt.show()

###afficher les données du capteur lié à l'humidité sur un graphe####
for i in range (2,7):
    plt.plot(reçu(1), humidity(1))
    plt.plot(reçu(i), humidity(i)) 
plt.title("Capteur humidité")
plt.show()

###afficher les données du capteur lié à la lumière sur un graphe####
for i in range (2,7):
    plt.plot(reçu(1), lum(1))
    plt.plot(reçu(i), lum(i)) 
plt.title("Capteur éclairage")
plt.show()

###afficher les données du capteur lié au co2 sur un graphe####
for i in range (2,7):
    plt.plot(reçu(1), co2(1))
    plt.plot(reçu(i), co2(i)) 
plt.title("Capteur qté de O2")
plt.show()

# plt.plot(reçu(1), co2(1))
# plt.plot(reçu(6), co2(6)) 
# plt.title("Capteur qté de O2")
# plt.show()


def minimum(Liste):
    mini=Liste[0]
    for i in Liste:
        if mini >= i:
            mini = i
    return mini

def maximum(Liste):
    maxi=Liste[0]
    for i in Liste:
        if maxi <= i:
            maxi = i
    return maxi

def moyenne(Liste):
    S=0
    compteur=0
    for i in Liste:
        S+= i
        compteur+=1
    return (S/compteur)

def variance(Liste):
    m=moyenne(Liste)
    v=0
    for i in Liste:
        v += (i-m)**2
    return(v/len(Liste))

def ecarttype(Liste):
    return (sqrt(variance(liste)))


  
a= 17.27
b=237.7

def alpha(T,phi):
    return (((a*T)/(b+T))+ np.ln(phi))


def temprose(T,phi):
    return ((b*alpha(T,phi))/(a-alpha(T,phi)))
    

def humidex(T,phi):
    return (T+0.5555(6.11*np.exp(5417.7530*((1/273.16)-(1/(273.15+temprose(T,phi)))))-10))     


nom_du_script=sys.argv[0]
action=sys.argv[1]
if len(sys.argv)==5:
    variable=sys.argv[2]
    numero=int(sys.argv[3])
    start_date=convtime2(sys.argv[4])
    end_date=convtime2(sys.argv[5])
elif len(sys.argv)==6:
    variable1=sys.argv[2]
    variable2=sys.arg[3]
    numero=int(sys.argv[4])
    start_date=convtime2(sys.argv[5])
    end_date=convtime2(sys.argv[6])
    
    
if action=='display' and variable=='humidex':
    print('''L'indice humidex du capteur''', numero, 'est', humidex(numero))
    for i in range (2,6):
        plt.plot(reçu(1), humidex(1))
        plt.plot(reçu(i), humidex(i))
    plt.title("indice humidex")
    plt.show()

    
if action=='displayStat':
    print('Pour', variable)
    print('Le minimum est', minimum(tab[variable]))
    print('Le maximum est', maximum(tab[variable]))
    print('La moyenne est', moyenne(tab[variable]))
    print('La variance est', variance(tab[variable]))
    print('''L'ecarttype est''', ecarttype(tab[variable]))
    
# if action=='corrélation':

# calcul de l'indice humidex (formule avec température de rosée)
# humidity=humidé relative ????

def alpha(T,H):
    a=17.27
    b=237.7
    return (((a*T)/(b+T))+np.log(H))

def humidex(id):
    Tair=temperature(id)
    hum=humidity(id)
    L=[]
    for i in range (7880):
        Trosée=(237.7*alpha(Tair[i],hum[i]))/(17.27-alpha(Tair[i],hum[i]))
        hmdx=Tair[i]+0.5555*(6.11*np.exp(5417.7530*((1/273.16)-(1/(273.15+Trosée))))-10)
        L.append(hmdx)
    return L


###afficher l'indice humidex####
for i in range (2,6):
    plt.plot(reçu(1), humidex(1))
    plt.plot(reçu(i), humidex(i)) 
plt.title("indice humidex")
plt.show()
