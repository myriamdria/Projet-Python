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



capteur=['capteur 1','capteur 2','capteur 3','capteur 4','capteur 5','capteur 6']
#Entrer la variable qui nous intéresse#
# variable = input('entrer une chaîne de caractère soit noise,humidity,lum,temp,co2,humidex:')
# start_date = '2019-08-23'
# end_date= '2019-08-24'

print ("Nombre d'arguments:", len(sys.argv), "arguments")
print ("Liste des arguments:", str(sys.argv))



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
        plt.axhline(y=moyenne(id1[variable]))
        plt.title('Graphe de notre variable en fonction du temps avec ses valeurs stats')
        plt.show()
        print('Pour', variable)
        print('Le minimum est', minimum(tab[variable]))
        print('Le maximum est', maximum(tab[variable]))
        print('La moyenne est', moyenne(tab[variable]))
        print('La variance est', variance(tab[variable]))
        print('''L'ecarttype est''', ecarttype(tab[variable]))
        
if len(sys.argv)==6:
    variable1=sys.argv[2]
    variable2=sys.arg[3]
    start_date=sys.argv[4]
    end_date=sys.argv[5]
    if str(sys.argv)[1] == 'corrélation':
        id1=tab[tab['id']==1]
        donnee = id1[start_date:end_date] 
        print ("l'indice de corrélation entre",variable1, "et", variable2, "est:", correlation(donnee[variable1],donnee[variable2]))


##Trouver les similarités##


# id1=tab[tab['id']==1]
# id2=tab[tab['id']==2]
# id3=tab[tab['id']==3]
# id4=tab[tab['id']==4]
# id5=tab[tab['id']==5]
# id6=tab[tab['id']==6]   

# donnee = id1[start_date:end_date] 
# print ("L'indice de corrélation du capteur 1 entre la température et l'humidité est:",correlation(donnee['temp'],donnee['humidity']))
# print (correlation(id1['temp'],id1['humidity']))

# id1_temperature = id1['temp']
# periode3 = id3['2019-08-23':'2019-08-24']
# periode2 = id2['2019-08-23':'2019-08-24']
# periode5 = id5['2019-08-23':'2019-08-24']
# print (id1_temperature)
# print (periode['temp'])
# plt.plot(periode3['lum'])
# plt.plot(periode2['lum'])
# plt.plot(periode5['lum'])
# plt.show()


