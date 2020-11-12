# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 08:48:24 2020

@author: myriam.andriamananja
"""


import os

os.getcwd()
monfichier=open('EIKM.csv','r')
L =[]
for ligne in monfichier.readlines() :       #traitement du fichier ligne par ligne
    L += ligne.split('\t')
L = L[6:]                                    #suppression des 1ers caractère de L (issu de la ligne Date Heure id...)
L = [i for i in L]
print(L)

def listes(L):
    id=[]
    noise=[]
    temp=[]
    humidity=[]
    lum=[]
    co2=[]
    date=[]
    n=len(L)
    id.append L[0]

    noise.append L[2:6]
    temp.append L [7:11]
    humidity



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




import pandas as pd

df = pd.read_csv('EIVP_KM.csv', sep=';')
df



from datetime import datetime
import calendar

def convtime(strtime):
    """Converts a string date "YYYY-MM-DD" as a time in sec"""
    moment = datetime.strptime(strtime, '%Y-%m-%d %H;%M;%S')
    return calendar.timegm(moment.timetuple())

print(convtime('2016-04-17 17;48;06'))






