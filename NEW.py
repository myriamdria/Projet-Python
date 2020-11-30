import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

df = pd.read_csv('EIVP_KM.csv', sep=';')
tab = pd.read_csv('EIVP_KM.csv', sep=';', index_col = 'sent_at',parse_dates = True)
tab

a=17.27
b=237.7

def alpha(T,humid):
    return (((a*T)/(b+T))+ np.log(humid))

def temprose(T,humid):
    return ((b*alpha(T,humid))/(a-alpha(T,humid)))

#on ajoute une colonne pour notre indice humidex
tab['humidex']= tab['temp']+0.5555*(6.11*np.exp(5417.7530*((1/273.16)-(1/(273.15 + temprose(tab['temp'],tab['humidity'])))))-10)





print ("Nombre d'arguments:", len(sys.argv), "arguments")
print ("Liste des arguments:", str(sys.argv))

#Pour notre légende#
capteur=['capteur 1','capteur 2','capteur 3','capteur 4','capteur 5','capteur 6']

if len(sys.argv)==3:
    variable=sys.argv[2]
    if str(sys.argv)[1]=='display':
        for i in range(1,7):
            idn = tab[tab['id'] == i] #on sélectionne que les données d'un capteur 1,2,3,4,5 ou 6"
            plt.plot(idn[variable]) #On trace le graphe de la donnée qui nous intéresse"
        plt.legend(capteur) #légende par numéro de capteur"
        plt.title("Graphe de la variable choisie en fonction du temps")
        plt.show()

##Les valeurs statistiques###
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

def mediane(Liste):
    n = len(Liste)
    if n%2 == 0:
        return ((Liste[(n//2)-1] + Liste[n//2]) / 2 )
    else:
        return (Liste[(n//2)])

def ecarttype(Liste):
    return (variance(Liste)**(1/2))

def covariance(Liste1,Liste2):
    if len(Liste1) == len(Liste2):
        m1= moyenne(Liste1)
        m2= moyenne(Liste2)
        S=0
        for i in range(len(Liste1)):
            S += (Liste1[i]-m1)*(Liste2[i]-m2)
        return (S/len(Liste1))

def correlation(Liste1,Liste2):
    return (covariance(Liste1,Liste2)/(ecarttype(Liste1)*ecarttype(Liste2)))

def moyenne1(dimension):  ##déterminer les moyennes d'une variable pour chaque capteur
    moy1=[]
    for i in range(1,7):
        idn = tab[tab['id'] == i]
        periode = idn[start_date : end_date]
        moy1.append(moyenne(periode[dimension]))
    return (moy1)
# print (moyenne1(variable))

def median1(dimension):
    med=[]
    for i in range(1,7):
        idn = tab[tab['id'] == i]
        periode = idn[start_date : end_date]
        med.append(mediane(periode[dimension]))
    return (med)
# print (median1(variable))

def ecarttype1(dimension):
    e=[]
    for i in range(1,7):
        idn = tab[tab['id'] == i]
        periode = idn[start_date : end_date]
        e.append(ecarttype(periode[dimension]))
    return (e)
# print (ecarttype1(variable))

def maximum1(dimension):
    maxi=[]
    for i in range (1,7):
        idn = tab[tab['id'] == i]
        periode = idn[start_date : end_date]
        maxi.append(maximum(periode[dimension]))
    return (maxi)
# print (maximum1(variable))

def minimum1(dimension):
    mini=[]
    for i in range (1,7):
        idn = tab[tab['id'] == i]
        periode = idn[start_date : end_date]
        mini.append(minimum(periode[dimension]))
    return (mini)
    
if len(sys.argv)==5:
    variable=sys.argv[2]
    start_date=sys.argv[3]
    end_date=sys.argv[4]
    if str(sys.argv)[1]=='display':
        for i in range(1,7):
            idn = tab[tab['id'] == i] #on sélectionne que les données d'un capteur 1,2,3,4,5 ou 6"
            periode = idn[ start_date : end_date ] #on choisit notre intervalle de temps qui nous intéresse"
            plt.plot(periode[variable]) #On trace le graphe de la donnée qui nous intéresse"
        plt.legend(capteur) #légende par numéro de capteur"
        plt.title("Graphe de la variable choisie en fonction du temps")
        plt.show() #Afficher le graphe d'une variable pour nos différents capteurs
    if str(sys.argv)[1]=='displayStat':
        id1=tab[tab['id']==1]
        id2=tab[tab['id']==2]
        id3=tab[tab['id']==3]
        id4=tab[tab['id']==4]
        id5=tab[tab['id']==5]
        id6=tab[tab['id']==6]
        fig, (cx1,cx2,cx3)= plt.subplots(3,1, sharex='col')
        fig.suptitle('Courbe capteur 1,2 et 3 avec la moyenne')
        cx1.plot(id1[variable])
        cx1.axhline(moyenne(id1[variable]))
        cx1.legend([moyenne(id1[variable])], loc='best')
        cx2.plot(id2[variable])
        cx2.axhline(moyenne(id1[variable]))
        cx2.legend([moyenne(id2[variable])], loc='best')
        cx2.set_ylabel(variable)
        cx3.plot(id3[variable])
        cx3.axhline(moyenne(id3[variable]))
        cx3.legend([moyenne(id3[variable])], loc='best')
        cx3.set_xlabel('temps')
        plt.show()
        fig ,(cx4,cx5,cx6)=plt.subplots(3,1,sharex='col')
        fig.suptitle('Courbe capteur 4,5 et 6 avec la moyenne')
        cx4.plot(id4[variable])
        cx4.axhline(moyenne(id4[variable]))
        cx4.legend([moyenne(id4[variable])], loc='best')
        cx5.plot(id5[variable])
        cx5.axhline(moyenne(id5[variable]))
        cx5.legend([moyenne(id5[variable])], loc='best')
        cx5.set_ylabel(variable)
        cx6.plot(id6[variable])
        cx6.axhline(moyenne(id6[variable]))
        cx6.legend([moyenne(id6[variable])], loc='best')
        cx6.set_xlabel('temps')
        plt.show()
        print('Pour', variable)
        print('Le minimum est(dans lordre des numéros des capteurs)', minimum1(tab[variable]))
        print('Le maximum est', maximum1(tab[variable]))
        print('La moyenne est:', moyenne1[tab[variable]])
        print('La variance est', variance(tab[variable]))
        print('''L'ecarttype est''', ecarttype1(tab[variable]))
        
if len(sys.argv)==6:
    variable1=sys.argv[2]
    variable2=sys.arg[3]
    start_date=sys.argv[4]
    end_date=sys.argv[5]
    if str(sys.argv)[1] == 'corrélation':
        id1=tab[tab['id']==1]
        donnee = id1[start_date:end_date] 
        print ("l'indice de corrélation entre",variable1, "et", variable2, "est:", correlation(donnee[variable1],donnee[variable2]))


#

