# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 08:48:24 2020

@author: myriam.andriamananjaona
"""



monfichier=open('EIVP_KM.csv','r')
L =[]
for ligne in monfichier.readlines() :       #traitement du fichier ligne par ligne
    L += ligne.split(';')
L = L[7:]                     #suppression des 1ers caractère de L (issu de la ligne Date Heure id...)           
L = [i for i in L]  
print(L)


id=[]
noise=[]
temp=[]
humidity=[]
lum=[]
co2=[]
date=[]
n= len(L)
compteur=0
sousliste=[]
sousliste=L[0:7]
print (sousliste)
 
import pandas as pd       
tab = pd.read_csv('EIVP_KM.csv', sep=';')
tab
print (tab)
        
#####capteur1#####
noise1=[tab.noise[i] for i in range(1336)]
temp1=[tab.temp[i] for i in range(1336)]
humidity1=[tab.humidity[i] for i in range (1336)]
lum1=[tab.lum[i] for i in range (1336)]
co21=[tab.co2[i] for i in range(1336)]
duree1=[convtime(tab.sent_at[i]) for i in range(1336)]

#####capteur2#####
n2= 1336+1345 
noise2=[tab.noise[i] for i in range(1336, n2)]
temp2=[tab.temp[i] for i in range(1336, n2)]
humidity2=[tab.humidity[i] for i in range (1336, n2)]
lum2=[tab.lum[i] for i in range (1336, n2)]
co22=[tab.co2[i] for i in range(1336, n2)]
duree2=[convtime(tab.sent_at[i]) for i in range(1336, n2)]

#####capteur3#####
n3 = n2 + 1345
noise3=[tab.noise[i] for i in range(n2, n3)]
temp3=[tab.temp[i] for i in range(n2, n3)]
humidity3=[tab.humidity[i] for i in range (n2, n3)]
lum3=[tab.lum[i] for i in range (n2, n3)]
co23=[tab.co2[i] for i in range(n2, n3)]
duree3=[convtime(tab.sent_at[i]) for i in range(n2, n3)]

#####capteur4#####
n4 = n3 + 1344
noise4=[tab.noise[i] for i in range(n3, n4)]
temp4=[tab.temp[i] for i in range(n3, n4)]
humidity4=[tab.humidity[i] for i in range (n3, n4)]
lum4=[tab.lum[i] for i in range (n3, n4)]
co24=[tab.co2[i] for i in range(n3, n4)]
duree4=[convtime(tab.sent_at[i]) for i in range(n3, n4)]

#####capteur5#####
n5 = n4 + 1165
noise5=[tab.noise[i] for i in range(n4, n5)]
temp5=[tab.temp[i] for i in range(n4, n5)]
humidity5=[tab.humidity[i] for i in range (n4, n5)]
lum5=[tab.lum[i] for i in range (n4, n5)]
co25=[tab.co2[i] for i in range(n4, n5)]
duree5=[convtime(tab.sent_at[i]) for i in range(n4, n5)]

#####capteur6#####

plt.plot(duree1,noise1)
plt.plot(duree2,noise2)
plt.show()
    
plt.plot(duree1,co21)
plt.plot(duree2,co22)
plt.show()
  



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


    
        
    