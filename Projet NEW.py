
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from datetime import datetime
# import calendar

tab = pd.read_csv('EIVP_KM.csv', sep=';', index_col = 'sent_at',parse_dates = True)
tab
# print (tab.id)
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
variable= 'humidity'
variable1= 'temp'
variable2= 'humidity'
# variable = input('entrer une chaîne de caractère soit noise,humidity,lum,temp,co2,humidex:')
start_date = '2019-08-12'
end_date= '2019-08-13'


# def convtime2(strtime):
#     """Converts a string date "YYYY-MM-DD" as a time in sec"""
#     moment = datetime.strptime(strtime, '%Y-%m-%d')
#     return calendar.timegm(moment.timetuple())

##Afficher le graphe d'une variable pour nos différents capteurs##
for i in range(1,7):
    idn = tab[tab['id'] == i] #on sélectionne que les données d'un capteur 1,2,3,4,5 ou 6"
    periode = idn[ start_date : end_date ] #on choisit notre intervalle de temps qui nous intéresse"
    plt.plot(periode[variable]) #On trace le graphe de la donnée qui nous intéresse sur la période demandée"
plt.legend(['capteur 1', 'capteur 2', 'capteur 3','capteur 4','capteur 5','capteur 6']) #légende par numéro de capteur"
plt.title('Graphe en fonction du temps')
plt.show()

for i in range(1,7):
    idn = tab[tab['id'] == i] #on sélectionne que les données d'un capteur 1,2,3,4,5 ou 6"
    plt.plot(idn[variable]) #On trace le graphe de la donnée qui nous intéresse sur la période demandée"
plt.legend(['capteur 1', 'capteur 2', 'capteur 3','capteur 4','capteur 5','capteur 6']) #légende par numéro de capteur"
plt.title('Graphe en fonction du temps')
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
        S = S + i
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

# print ('ecart type est:', ecarttype(tab[variable]))
# print ('moyenne',moyenne(tab[variable]))

##Trouver les similarités##

L=['noise','humidity','lum','temp','co2']

# for dimension in L:
#     moy=[] 
#     e=[]
#     maxi=[]
#     mini=[]
#     median=[]
#     for i in range(1,7):
#         idn = tab[tab['id'] == i] #on sélectionne que les données du capteur 1,2,3,4,5 ou 6"
#         periode = idn[ start_date : end_date ] #on choisit notre intervalle de temps qui nous intéresse"
#         moy.append(moyenne(periode[dimension]))
#         e.append(ecarttype(periode[dimension]))
#         maxi.append(maximum(periode[dimension]))
#         mini.append(minimum(periode[dimension]))
#         median.append(mediane(periode[dimension]))
#     print ('Pour', dimension)
#     print ('Le maximum', maxi)
#     print ('Le minimum', mini)
#     print ('Les moyennes:', moy)
#     print ('les écart-types', e)
#     print ('La médiane', median)

# for dimension in L:
#     moy=[] 
#     e=[]
#     maxi=[]
#     mini=[]
#     median=[]
#     for i in range(1,7):
#         idn = tab[tab['id'] == i] #on sélectionne que les données du capteur 1,2,3,4,5 ou 6"
#         moy.append(moyenne(idn[dimension]))
#         e.append(ecarttype(idn[dimension]))
#         maxi.append(maximum(idn[dimension]))
#         mini.append(minimum(idn[dimension]))
#         median.append(mediane(idn[dimension]))
#     print ('Pour', dimension)
#     print ('Le maximum', maxi)
#     print ('Le minimum', mini)
#     print ('Les moyennes:', moy)
#     print ('les écart-types', e)
#     print ('La médiane', median)
                
def moyenne1(dimension):  ##déterminer les moyennes d'une variable pour chaque capteur
    moy1=[]
    for i in range(1,7):
        idn = tab[tab['id'] == i]
        periode = idn[ start_date : end_date ]
        moy1.append(moyenne(periode[dimension]))
    return (moy1)
# print (moyenne1('co2'))

def median1(dimension):
    med=[]
    for i in range(1,7):
        idn = tab[tab['id'] == i]
        periode = idn[ start_date : end_date ]
        med.append(mediane(periode[dimension]))
    return (med)
# print (median1('temp'))

def ecarttype1(dimension):
    e=[]
    for i in range(1,7):
        idn = tab[tab['id'] == i]
        periode = idn[ start_date : end_date ]
        e.append(ecarttype(periode[dimension]))
    return (e)
# print (ecarttype1('temp'))




###Trouver les capteurs similaires selon la variable
dimension='co2' 



d = {'id':[i for i in range (1,7)], 'moyenne':[i for i in moyenne1(dimension)], 'ecart_type':[i for i in ecarttype1(dimension)], 'mediane':[i for i in median1(dimension)] }
df = pd.DataFrame(data=d)
print (df)
df_sort1= df.id[(df['moyenne']-moyenne(moyenne1(dimension))).abs().argsort()[:2]]
df_sort2= df.moyenne[(df['moyenne']-moyenne(moyenne1(dimension))).abs().argsort()[:2]]
# df_sort.id.tolist()

print ('Les capteurs',df_sort1.tolist(), 'sont similaires')
print ('Avec pour moyennes, respectivement', df_sort2.tolist(), 'pour', dimension)






#Pour les valeurs

# for dimension in L:
#     moy_sim = []
#     m = moyenne1(dimension)
#     me = moyenne(ecarttype1(dimension)) #moyenne des écart-types de la dimension pour chaque capteur
#     median = median1(dimension)
#     med_sim = []
#     similarite= []
#     for i in range(6):
#         moy_sim.append(m[i])
#         med_sim.append(median[i])
#         similarite.append(i)
#         for j in range(6):
#             if i != j:
#                 if (moy_sim[i]- me < m[j] < moy_sim[i]+ me) and (med_sim[i] -1 < median[j] < med_sim[i] +1):
#                     moy_sim.append(m[j])
#                     med_sim.append(median[j])
#                     similarite.append(j)
#     print (similarite)            

            
# moy_sim = []
m = moyenne1(dimension)
me = moyenne(ecarttype1(dimension)) #moyenne des écart-types de la dimension pour chaque capteur
median = median1(dimension)
# med_sim = []

for i in range(1,7):
    moy_sim = []
    similarite= []
    med_sim = []
    for j in range(i+1,6):
        if (m[i]- me < m[j] < m[i]+ me) :
            moy_sim.append(m[j])
            med_sim.append(median[j])
            similarite.append(j)
    # print (moy_sim)
    # print (similarite)
                  
                
##################
            
    

# for i in range(1,7):
#     idn = tab[tab['id'] == i] #on sélectionne que les données d'un capteur 1,2,3,4,5 ou 6"
#     plt.plot(idn[variable]) #On trace le graphe de la donnée qui nous intéresse"
#     plt.title("Graphe")
#     plt.axhline(moyenne(idn[variable]))
#     plt.show() 
# plt.legend(capteur) #légende par numéro de capteur"

# plt.title("Graphe de notre variable en fonction du temps avec ses valeurs stats")

# plt.show()       
 
id1=tab[tab['id']==1]
id2=tab[tab['id']==2]
id3=tab[tab['id']==3]
id4=tab[tab['id']==4]
id5=tab[tab['id']==5]
id6=tab[tab['id']==6]   

donnee = id1[start_date:end_date] 
print ("l'indice de corrélation entre",variable1, "et", variable2, "est:",correlation(donnee[variable1],donnee[variable2]))

# print (moyenne(donnee[variable1]))

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



    
