
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import calendar


def convtime(strtime):
    """Converts a string date "YYYY-MM-DD HH;MM;SS" as a time in sec"""
    moment = datetime.strptime(strtime, '%Y-%m-%d %H:%M:%S+02:00')
    return calendar.timegm(moment.timetuple())

tab = pd.read_csv('EIVP_KM.csv', sep=';', index_col = 'sent_at',parse_dates = True)
tab
# print (tab)
tab1 = pd.read_csv('EIVP_KM.csv', sep=';')
tab1['duree']= [convtime(i) for i in tab1.sent_at]
# # print (tab1)
# tab1


#Rajoutons une colonne dans notre fichier correspondant à l'indice humidex
a=17.27   #coefficients utiles pour le calcul de humidex
b=237.7

def alpha(T,humid):
    return (((a*T)/(b+T))+ np.log(humid))

def temprose(T,humid): #calcul de la température de rosée
    return ((b*alpha(T,humid))/(a-alpha(T,humid)))

#on ajoute une colonne pour notre indice humidex
tab['humidex']= tab['temp']+0.5555*(6.11*np.exp(5417.7530*((1/273.16)-(1/(273.15 + temprose(tab['temp'],tab['humidity'])))))-10)

#on créer une liste pour légender plus facilement nos graphes
capteur=['capteur 1','capteur 2','capteur 3','capteur 4','capteur 5','capteur 6']

###############Déterminons le temps d'occupation de bureaux####################
#On rajoute des colonnes pour une meilleure visibilité des horaires
tab1['date'] = pd.to_datetime(tab1['sent_at']).dt.date  #Une colonne avec juste les dates
tab1['Time'] = pd.to_datetime(tab1['sent_at']).dt.time  #Une colonne avec juste l'heure
tab1['jour_de_la_semaine'] = pd.to_datetime(tab1['date']).dt.day_name()     #jour correspondant à la date donnée

#On crée deux tableaux avec uniquement les donnéees précédemments ajoutés
#Le premier permet d'avoir quand la journée débute
t1 = {'date': tab1['date'], 'debut' : tab1['Time'], 'jour': tab1['jour_de_la_semaine'] }
tf1 = pd.DataFrame(data=t1) 
tf1.drop_duplicates(subset='date', keep='first', inplace=True) #on supprime 
#toutes les lignes dont la date apparait en doublon excepté la première pour 
#connaitre l'horaire de début de journée pour chaque jour
 
#Le deuxième, quand la journée se termine
t2 = {'date': tab1['date'], 'fin' : tab1['Time'], 'jour': tab1['jour_de_la_semaine'] }
tf2 = pd.DataFrame(data=t2)
tf2.drop_duplicates(subset='date', keep='last', inplace=True)#on supprime 
#toutes les lignes dont la date apparait en doublon excepté la dernière pour 
#connaitre l'heure de la fin de journée pour chaque jour

#On affiche nos résultats
print ('Les périodes doccupations de bureaux')
print ('Les journées commencent à :')
print (tf1)

print ('Puis se terminent à:')
print (tf2)

##############################################################################

#On entre la variable des données qui nous intéressent avec les dates qui nous intéresse
# variable = input('entrer une chaîne de caractère soit noise,humidity,lum,temp,co2,humidex:')
# if variable == 'humidex':
#         print (tab.humidex)
#         for i in range(1,7):
#             idn = tab[tab['id'] == i] #on sélectionne que les données d'un capteur 1,2,3,4,5 ou 6"
#             plt.plot(idn[variable]) #On trace le graphe de la donnée qui nous intéresse sur la période demandée"
#         plt.legend(['capteur 1', 'capteur 2', 'capteur 3','capteur 4','capteur 5','capteur 6']) #légende par numéro de capteur"
#         plt.title('Variation pour chaque capteur en fonction du temps')
#         plt.ylabel(variable)
#         plt.xlabel('date')
#         plt.show()

variable='lum'
start_date ='2019-08-13'
end_date = '2019-08-14'

# start_date = input('entrer une date sous la forme AAAA-MM-JJ:')
# end_date= input('entrer une date sous la forme AAAA-MM-JJ:')
    


##Afficher le graphe d'une variable pour nos différents capteurs sur une periode donnée##
for i in range(1,7):
    idn = tab[tab['id'] == i] #on sélectionne que les données d'un capteur 1,2,3,4,5 ou 6"
    periode = idn[ start_date : end_date ] #on choisit notre intervalle de temps qui nous intéresse"
    plt.plot(periode[variable]) #On trace le graphe de la donnée qui nous intéresse sur la période demandée"
plt.legend(['capteur 1', 'capteur 2', 'capteur 3','capteur 4','capteur 5','capteur 6']) #légende par numéro de capteur"
plt.title('Courbes de chaque capteur en fonction du temps')
plt.xlabel('date')
plt.ylabel(variable)
plt.show()  #afficher notre graphe avec les différentes courbes

# for i in range(1,7):
#     idn = tab[tab['id'] == i] #on sélectionne que les données d'un capteur 1,2,3,4,5 ou 6"
#     plt.plot(idn[variable]) #On trace le graphe de la donnée qui nous intéresse sur la période demandée"
# plt.legend(['capteur 1', 'capteur 2', 'capteur 3','capteur 4','capteur 5','capteur 6']) #légende par numéro de capteur"
# plt.title('Variation pour chaque capteur en fonction du temps')
# plt.ylabel(variable)
# plt.xlabel('date')
# plt.show() 

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


###Fonctions permettant de créer une liste de nos données statistiques de chaque
#variable pour une variable demandée

def moyenne1(dimension):  #déterminer la moyenne d'une variable pour chaque capteur
    moy1=[]
    for i in range(1,7):
        idn = tab[tab['id'] == i]
        periode = idn[start_date : end_date]
        moy1.append(moyenne(periode[dimension]))
    return (moy1)
# print (moyenne1(variable))

def median1(dimension):     #déterminer la médiane d'une variable pour chaque capteur
    med=[]
    for i in range(1,7):
        idn = tab[tab['id'] == i]
        periode = idn[start_date : end_date]
        med.append(mediane(periode[dimension]))
    return (med)
# print (median1(variable))

def ecarttype1(dimension):  #déterminer l'écart-type d'une variable pour chaque capteur
    e=[]
    for i in range(1,7):
        idn = tab[tab['id'] == i]
        periode = idn[start_date : end_date]
        e.append(ecarttype(periode[dimension]))
    return (e)
# print (ecarttype1(variable))

def maximum1(dimension):    #déterminer le maximum d'une variable pour chaque capteur
    maxi=[]
    for i in range (1,7):
        idn = tab[tab['id'] == i]
        periode = idn[start_date : end_date]
        maxi.append(maximum(periode[dimension]))
    return (maxi)
# print (maximum1(variable))

def minimum1(dimension):    #déterminer le minimum d'une variable pour chaque capteur
    mini=[]
    for i in range (1,7):
        idn = tab[tab['id'] == i]
        periode = idn[start_date : end_date]
        mini.append(minimum(periode[dimension]))
    return (mini)



###Création d'un tableur donnant les valeurs statistiques de chaque capteur###
print ('Pour', variable,', on a ces valeurs statistiques:')
d = {'id':[i for i in range (1,7)], 'moyenne':[i for i in moyenne1(variable)], 'ecart_type':[i for i in ecarttype1(variable)], 'mediane':[i for i in median1(variable)], 'maximum':[i for i in maximum1(variable)], 'mimumum':[i for i in minimum1(variable)] }
df = pd.DataFrame(data=d)
print(df)

# df_sort1= df.id[(df['moyenne']-moyenne(moyenne1(variable))).abs().argsort()[:2]]   #on récupérer les numéros de capteurs similaires par rapport à leur moyenne
# df_sort2= df.moyenne[(df['moyenne']-moyenne(moyenne1(variable))).abs().argsort()[:2]]  #on récupérer les moyennes de capteurs similaires par rapport à leur moyenne
# df_sort3= df.ecart_type[(df['moyenne']-moyenne(moyenne1(variable))).abs().argsort()[:2]]  #on récupérer les écart-types des capteurs similaires par rapport à leur moyenne
# df_sort4= df.id[(df['ecart_type']-moyenne(ecarttype1(variable))).abs().argsort()[:2]]  #on récupérer les écart-types des capteurs similaires par rapport à leur écart-type
# df_sort5= df.ecart_type[(df['ecart_type']-moyenne(ecarttype1(variable))).abs().argsort()[:3]]  #on récupérer les écart-types des capteurs similaires par rapport à leur écart-type
# df_sort0= df.id[(df['maximum']-moyenne(maximum1(variable))).abs().argsort()[:2]]
# df_sort.id.tolist()

# print ('Les capteurs',df_sort0.tolist(), 'sont similaires vis à vis de', variable)
# print ('Avec pour moyennes, respectivement', df_sort2.tolist(), 'pour', variable)
# print ('Avec pour ecartype, respectivement', df_sort3.tolist(), 'pour', variable)

#Courbes des capteurs qui sont similaires par rapport à leur valeur statistique
# for i in df_sort1.tolist():
#     idi = tab[tab['id'] == i] #on sélectionne le tableau correspond aux capteurs similaires
#     periode = idi[ start_date : end_date ] #on choisit notre intervalle de temps qui nous intéresse
#     plt.plot(periode[variable]) #On trace le graphe de la donnée qui nous intéresse sur la période demandée
# plt.axhline(df_sort2.tolist()[0])   #on trace la moyenne de nos capteurs
# plt.axhline(df_sort2.tolist()[1], c='y')
# legend1= plt.legend(df_sort1.tolist(), title = 'Capteur',loc='upper right')
# plt.gca().add_artist(legend1)
# plt.legend(df_sort1.tolist(), title = 'Moyenne', loc = 'upper left')
# plt.title('Les capteurs similaires en fonction du temps') 
# plt.ylabel(variable)
# plt.xlabel('date')
# plt.show()


#Traçons tous les capteurs similaires

# print ('Les capteurs 2 et 4 sont similaires par rapport à la température en se basant sur leur moyenne')
# print ('Par lecture graphique et avec les valeurs statistiques, on a aussi que 1, 3, 2 et 4 le sont aussi)


# print ('Les capteurs 2 et 4 sont similaires par rapport aux bruits')
# plt.plot(id2['noise'])
# plt.plot(id4['noise'])
# plt.show()


# tab_sort = tab.id[(tab[variable]-moyenne(moyenne1(variable))).abs().argsort()[:2]]
# print (tab_sort)
# print ('Les capteurs',tab_sort.tolist(), 'sont similaires vis à vis de', variable)
# # print ('Avec pour moyennes, respectivement', df_sort2.tolist(), 'pour', dimension)
# # print ('Avec pour ecartype, respectivement', df_sort4.tolist(), 'pour', dimension)
# for i in tab_sort.tolist():
#     idi = tab[tab['id'] == i] #on sélectionne que les données d'un capteur 1,2,3,4,5 ou 6"
#     periode = idi[ start_date : end_date ] #on choisit notre intervalle de temps qui nous intéresse"
#     plt.plot(periode[variable]) #On trace le graphe de la donnée qui nous intéresse sur la période demandée"
# # plt.axhline(df_sort2.tolist()[0])   #on trace la moyenne de nos capteurs
# # plt.axhline(df_sort2.tolist()[1], c='y')
# legend1= plt.legend(tab_sort.tolist(), title = 'Capteur',loc='upper right')
# plt.gca().add_artist(legend1)
# # plt.legend(df_sort2.tolist(), title = 'Moyenne', loc = 'best')
# plt.title('Les capteurs similaires en fonction du temps') 
# plt.ylabel(variable)
# plt.xlabel('date')
# plt.show()

def plus_proche(liste, valeur):
    liste = np.asarray(liste)
    idx = (np.abs(liste-valeur)).argmin()
    return (liste[idx])


####Afficher la moyenne d'une variable sur un graphe pour chaque capteur####
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
# for i in range(6):
#     sim=[]
#     moy=[]
#     depart=
#     moy[0]=depart[i]
    
#     for j in 
    
