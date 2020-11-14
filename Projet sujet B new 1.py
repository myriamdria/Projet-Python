# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 09:34:18 2020

@author: myriam.andriamananjaona
"""

import pandas as pd
# from datetime import datetime
# import calendar
import numpy as np
import matplotlib.pyplot as plt


tab = pd.read_csv('EIVP_KM.csv', sep=';')
tab
print (tab)

L=[]
for j in range (1,7):
    compteur=0
    for i in range (7880):
        if tab.id[i]==j:
            compteur += 1
    L.append(compteur)
print (L)
print (sum(L))


date = tab.loc['2019-01-01':'2019-01-02']

# def convtime(strtime):
#     """Converts a string date "YYYY-MM-DD HH;MM;SS" as a time in sec"""
#     moment = datetime.strptime(strtime, '%Y-%m-%d %H:%M:%S+02:00')
#     return calendar.timegm(moment.timetuple())

# # temps=[]
# # for i in date:
# #     temps.append(convtime(i))
# # print (temps)

# def identite(numero):
#     noise=[]
#     temp=[]
#     humidity=[]
#     lum=[]
#     co2=[]
#     duree=[]
#     for i in range (7880):
#         if tab.id[i] == numero:
#             noise.append(tab.noise[i])
#             temp.append(tab.temp[i])
#             humidity.append(tab.humidity[i])
#             lum.append(tab.lum[i])
#             co2.append(tab.co2[i])
#             duree.append(convtime(tab.sent_at[i]))
#     return noise,temp,humidity,lum,co2,duree

def noise(id):
    L=[]
    for i in range (len(date)):
        if tab.id[i] == id:
            L.append(tab.noise[i])
    return L

def temp(id):
    L=[]
    for i in range (len(date)):
        if tab.id[i] == id:
            L.append(tab.temp[i])
    return L

def humidity(id):
    L=[]
    for i in range (len(date)):
        if tab.id[i] == id:
            L.append(tab.humidity[i])
    return L

def lum(id):
    L=[]
    for i in range (len(date)):
        if tab.id[i] == id:
            L.append(tab.lum[i])
    return L

def co2(id):
    L=[]
    for i in range (len(date)):
        if tab.id[i] == id:
            L.append(tab.co2[i])
    return L

# def reçu(id):
#     L=[]
#     for i in range (len(date)):
#         if tab.id[i] == id:
#             L.append(convtime(tab.sent_at[i]))
    return L

# print (reçu(6))
# print (len(reçu(6)))
# def duree(id):
#     temps = date(id)[-1] - date(id)[0]
#     return(temps)
    
###afficher les données du capteur lié au bruit sur un graphe####
for i in range (2,6):
    plt.plot(date,noise(1))
    plt.plot(date, noise(i))
plt.title("Capteur bruit")
plt.show()

###afficher les données du capteur lié à la température sur un graphe####
for i in range (2,6):
    plt.plot(date, temp(1))
    plt.plot(date, temp(i))
    plt.tight_layout()
plt.title("Capteur temperature")
plt.show()

###afficher les données du capteur lié à l'humidité sur un graphe####
for i in range (2,6):
    plt.plot(date, humidity(1))
    plt.plot(date, humidity(i)) 
    plt.tight_layout()
plt.title("Capteur humidité")
plt.show()

###afficher les données du capteur lié à la lumière sur un graphe####
for i in range (2,6):
    plt.plot(date, lum(1))
    plt.plot(date, lum(i)) 
plt.title("Capteur éclairage")
plt.show()

###afficher les données du capteur lié au co2 sur un graphe####
for i in range (2,6):
    plt.plot(date, co2(1))
    plt.plot(date, co2(i)) 
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

        
print (minimum(tab.co2))

a= 17.27
b=237.7

def alpha(T,phi):
    return (((a*T)/(b+T))+ np.ln(phi))


def temprose(T,phi):
    return ((b*alpha(T,phi))/(a-alpha(T,phi)))
    

def humidex(T,phi):
    Ta = 25
    return (Ta+0.5555(6.11*np.exp(5417.7530*((1/273.16)-(1/(273.15+temprose(T,phi)))))-10))

    