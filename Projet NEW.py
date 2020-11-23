import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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




#Entrer la variable qui nous intéresse#
variable = input('entrer une chaîne de caractère soit noise,humidity,lum,temp,co2,humidex:')
start_date = '2019-08-23'
end_date= '2019-08-24'

##Afficher le graphe d'une variable pour nos différents capteurs##
indice = []
for i in range(1,7):
    idn = tab[tab['id'] == i] #on sélectionne que les données d'un capteur 1,2,3,4,5 ou 6"
    indice.append(i)
    periode = idn[ start_date : end_date ] #on choisit notre intervalle de temps qui nous intéresse"
    plt.plot(periode[variable]) #On trace le graphe de la donnée qui nous intéresse"
plt.legend(indice) #légende par numéro de capteur"
plt.title("Graphe de la donnée choisie en fonction du temps")
plt.show()

##Trouver les similarités##
# def similarite(capteur):
    



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

print ('ecart type est:', ecarttype(tab[variable]))
print ('moyenne',moyenne(tab[variable]))


id1=tab[tab['id']==1]
id2=tab[tab['id']==2]
id3=tab[tab['id']==3]
id4=tab[tab['id']==4]
id5=tab[tab['id']==5]
id6=tab[tab['id']==6]   

donnee = id1[start_date:end_date] 
print ("L'indice de corrélation du capteur 1 entre la température et l'humidité est:",correlation(donnee['temp'],donnee['humidity']))
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