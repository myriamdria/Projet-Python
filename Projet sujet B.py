# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:34:18 2020

@author: myriam.andriamananjaona
"""

import pandas as pd
from datetime import datetime
import calendar
import matplotlib.pyplot as plt


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
    moment = datetime.strptime(strtime, '%Y-%m-%d %H:%M:%S +0200')
    return calendar.timegm(moment.timetuple())

# temps=[]
# for i in date:
#     temps.append(convtime(i))
# print (temps)

def identite(numero):
    noise=[]
    temp=[]
    humidity=[]
    lum=[]
    co2=[]
    duree=[]
    for i in range (7880):
        if tab.id[i] == numero:
            noise.append(tab.noise[i])
            temp.append(tab.temp[i])
            humidity.append(tab.humidity[i])
            lum.append(tab.lum[i])
            co2.append(tab.co2[i])
            duree.append(convtime(tab.sent_at[i]))
    return noise,temp,humidity,lum,co2,duree

def noise(id):
    L=[]
    for i in range (7880):
        if tab.id[i] == id:
            L.append(tab.noise[i])
    return L

def temp(id):
    L=[]
    for i in range (7880):
        if tab.id[i] == id:
            L.append(tab.temp[i])
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
    if id == 6:
        for i in range (7880):
            if tab.id[i] == id:
                L.append(convtime(tab.sent_at[i])+ 31540007 + 2628000) #on ajoute une année et un mois pour avoir une même plage horaire que les autres capteurs
        return L
    else:
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
for i in range (2,6):
    plt.plot(reçu(1),noise(1))
    plt.legend('capteur 1')
    plt.plot(reçu(i), noise(i))
plt.title("Capteur bruit")
plt.show()

for i in range (2,6):
    plt.plot(reçu(1), temp(1))
    plt.plot(reçu(i), temp(i)) 
plt.title("Capteur temperature")
plt.show()

for i in range (2,6):
    plt.plot(reçu(1), humidity(1))
    plt.plot(reçu(i), humidity(i)) 
plt.title("Capteur humidité")
plt.show()

for i in range (2,6):
    plt.plot(reçu(1), lum(1))
    plt.plot(reçu(i), lum(i)) 
plt.title("Capteur éclairage")
plt.show()

for i in range (2,6):
    plt.plot(reçu(1), co2(1))
    plt.plot(reçu(i), co2(i)) 
plt.title("Capteur qté de O2")
plt.show()

# plt.plot(reçu(2), co2(2))
# plt.plot(reçu(4), co2(4)) 
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
