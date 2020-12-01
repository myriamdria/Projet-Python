
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import calendar


tab = pd.read_csv('EIVP_KM.csv', sep=';', index_col = 'sent_at',parse_dates = True)
tab


tab1 = pd.read_csv('EIVP_KM.csv', sep=';')
tab1

################Définition de l'indice humidex################################

#Rajoutons une colonne dans notre fichier correspondant à l'indice humidex

#coefficients utiles pour le calcul de humidex
a=17.27   
b=237.7

def alpha(T,humid):
    return (((a*T)/(b+T))+ np.log(humid))

def temprose(T,humid): #calcul de la température de rosée
    return ((b*alpha(T,humid))/(a-alpha(T,humid)))

#on ajoute une colonne pour notre indice humidex
tab['humidex']= tab['temp']+0.5555*(6.11*np.exp(5417.7530*((1/273.16)-(1/(273.15 + temprose(tab['temp'],tab['humidity'])))))-10)

###############################################################################



##################Convertisseur de date en durée (secondes)####################
def convtime2(strtime):
    """Convertir l'heure donnée "HH:MM:SS" en seconde"""
    instant = datetime.strptime(strtime, 'H:%M:%S+02:00')
    return calendar.timegm(instant.timetuple())

def convtime(date):
    """Convertir une date "YYYY-MM-DD HH;MM;SS" en une durée en sec"""
    instant = datetime.strptime(date, '%Y-%m-%d %H:%M:%S+02:00')
    return calendar.timegm(instant.timetuple())

###############################################################################



############Fonctions pour déterminer les valeurs statistiques#################
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
    if len(Liste1) != len(Liste2):
        return ('prendre un rautre intervalle')
    m1= moyenne(Liste1)
    m2= moyenne(Liste2)
    S=0
    for i in range(len(Liste1)):
        S += (Liste1[i]-m1)*(Liste2[i]-m2)
    return (S/(len(Liste1)-1))

def correlation(Liste1,Liste2):
    return (covariance(Liste1,Liste2)/(ecarttype(Liste1)*ecarttype(Liste2)))


###Mettre les valeurs statistiques de chaque capteur dans une liste###########
def moyenne1(dimension):  #déterminer la moyenne d'une variable pour chaque capteur
    moy1=[]
    for i in range(1,7):
        idn = tab[tab['id'] == i]
        # periode = idn[start_date : end_date]
        moy1.append(moyenne(idn[dimension]))
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
        # periode = idn[start_date : end_date]
        mini.append(minimum(idn[dimension]))
    return (mini)

def variance1(dimension):  #déterminer l'écart-type d'une variable pour chaque capteur
    v=[]
    for i in range(1,7):
        idn = tab[tab['id'] == i]
        # periode = idn[start_date : end_date]
        v.append(variance(idn[dimension]))
    return (v)


###############################################################################


######################Partie Similarité#######################################
L=['noise','humidity','lum','temp','co2']  #Création d'une liste de caractéristiques évaluées par nos capteurs

def normalise(valeur,variable): #Normaliser les valeurs
    mini=minimum(variable)
    maxi=maximum(variable)
    return ((valeur-mini)/(maxi-mini))

for mesure in L: #On va comparer nos capteurs par rapport à chacune de leurs caractéristiques mesurées
    for i in range(1,7): #On a 6 capteurs à comparer
        id1 = tab[tab['id'] == i] #on sélectionne que les données du capteur 1,2,3,4,5 ou 6
        # periode1= id1[start_date : end_date]
        n1= len(id1) #nombre de ligne
        for j in range(i+1,7): #On compare le capteur i avec le capteur i+1
            sim=[]  #On initialise une liste vide qui nous donnera pour chaque variable leur similitude
            norm_distance=[]    #Initialise une liste vide qui contiendra les distances normalisés
            compteur=0
            id2 = tab[tab['id'] == j]   #Les données du capteur i+1
            # periode2 = id2[start_date : end_date]
            n2 = len(id2)  #nombre de ligne
            m=[]    #liste vide qui contiendra les distances entre chaque point
            if n1 > n2 :    #on vérifie qu'on prend uniquement le nombre d'élément de la plus petite liste pour comparer 2 listes
                n= n2
            else:
                n= n1
            for k in range(n):  #on calcule l'écart entre chaque point
                m.append((abs(id2[mesure][k]-id1[mesure][k])))  #qu'on ajoute dans notre liste
            # print (m)
            for valeur in m:
                norm_distance.append(normalise(valeur,m)) #on normalise les distances trouvés qui sont non similaires
            for non_similaire in norm_distance:
                sim.append((1-non_similaire))   
            for seuil in sim:   #On détermine si les valeurs sont similaires
                if seuil > 0.86:    #Notre seuil de similarité
                    compteur+=1     #Si similaire on ajoute 1 à notre compteur
                else:
                    compteur+=0     #sinon non
            if compteur > 0.75*n:   #On considère que nos deux capteurs sont similaires si plus de trois quart de nos valeurs sont similaires
                print ('Les capteurs', i, 'et', j, 'sont similaires par rapport à',mesure)
                plt.plot(id1[mesure])
                plt.plot(id2[mesure])
                plt.title('Les capteurs similaires')
                plt.legend([i,j])
                plt.ylabel(mesure)
                plt.xlabel('date')
                plt.xticks(rotation = 'vertical')
                plt.show()


##############################Partie utilisateur##############################

action = input('Que souhaitez-vous faire ? (diplay/displayStat/correlation):')
 
if action == 'correlation' :
    variable1 = input('Quelle est la première variable ?(noise/humidity/lum/temp/co2/humidex)')
    variable2 =input('Quelle est la seconde variable ? (noise/humidity/lum/temp/co2/humidex)')
    start_date = input('Entrer une date de début sous la forme AAAA-MM-JJ:')
    end_date = input('Entrer une date de fin sous la forme AAAA-MM-JJ:')
    for i in range (1,7):
        id1= tab[tab['id']== i]
        donnee = id1[start_date:end_date] 
        print ('indice de corrélation pour le capteur',i,'entre',variable1, 'et', variable2, 'est:', correlation(donnee[variable1],donnee[variable2]))


if action == 'display' :
    variable=input('Pour quelle variable ? (noise/humidity/lum/temp/co2/humidex):')

    if variable=='humidex' :
        print (tab.humidex)
        for i in range(1,7):
            idn = tab[tab['id'] == i] #on sélectionne que les données d'un capteur 1,2,3,4,5 ou 6"
            plt.plot(idn[variable]) #On trace le graphe de la donnée qui nous intéresse sur la période demandée"
        plt.legend(['capteur 1', 'capteur 2', 'capteur 3','capteur 4','capteur 5','capteur 6']) #légende par numéro de capteur"
        plt.title('Variation pour chaque capteur en fonction du temps')
        plt.ylabel(variable)
        plt.xlabel('date')
        plt.xticks(rotation = 'vertical')
        plt.show()


    else:
        end_date= input('(optionnel)Entrer une date de fin sous la forme AAAA-MM-JJ:')    
        start_date = input('(optionnel)Entrer une date de début sous la forme AAAA-MM-JJ:')
        for i in range(1,7):
            idn = tab[tab['id'] == i] #on sélectionne que les données d'un capteur 1,2,3,4,5 ou 6"
            periode = idn[ start_date : end_date ] #on choisit notre intervalle de temps qui nous intéresse"
            plt.plot(periode[variable]) #On trace le graphe de la donnée qui nous intéresse sur la période demandée"
        plt.legend(['capteur 1', 'capteur 2', 'capteur 3','capteur 4','capteur 5','capteur 6']) #légende par numéro de capteur"
        plt.title('Capteurs en fonction du temps, de la période donnée')
        plt.axes().set(xlabel= 'Date', ylabel=variable)
        plt.show()
    
        for i in range(1,7):
            idn = tab[tab['id'] == i] #on sélectionne que les données d'un capteur 1,2,3,4,5 ou 6"
            plt.plot(idn[variable]) #On trace le graphe de la donnée qui nous intéresse sur la période demandée"
            plt.legend(['capteur 1', 'capteur 2', 'capteur 3','capteur 4','capteur 5','capteur 6']) #légende par numéro de capteur"
            plt.title('Variation pour chaque capteur en fonction du temps')
            plt.ylabel(variable)
            plt.xlabel('date')
            plt.xticks(rotation = 'vertical')
            plt.show() 
     
if action == 'displayStat':
    d = {'id':[i for i in range (1,7)], 'moyenne':[i for i in moyenne1(variable)], 'ecart_type':[i for i in ecarttype1(variable)], 'mediane':[i for i in median1(variable)] }
    df = pd.DataFrame(data=d)
    print ('Pour', variable)
    print (df)
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
    # cx1.set_ylabel(variable)
    cx2.plot(id2[variable])
    cx2.axhline(moyenne(id1[variable]))
    cx2.legend([moyenne(id2[variable])], loc='best')
    # plt.legend(moyenne(id2[variable]))
    cx2.set_ylabel(variable)
    cx3.plot(id3[variable])
    cx3.axhline(moyenne(id3[variable]))
    cx3.legend([moyenne(id3[variable])], loc='best')
    cx3.set_xlabel('temps')
    plt.xticks(rotation = 'vertical')
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
    plt.xticks(rotation = 'vertical')
    plt.show()




          
###############Déterminons le temps d'occupation de bureaux####################
# #On rajoute des colonnes pour une meilleure visibilité des horaires
# tab1['date'] = pd.to_datetime(tab1['sent_at']).dt.date  #Une colonne avec juste les dates
# tab1['Time'] = pd.to_datetime(tab1['sent_at']).dt.time  #Une colonne avec juste l'heure
# tab1['jour_de_la_semaine'] = pd.to_datetime(tab1['date']).dt.day_name()     #jour correspondant à la date donnée

# #On crée deux tableaux avec uniquement les donnéees précédemments ajoutés
# #Le premier permet d'avoir quand la journée débute
# t1 = {'date': tab1['date'], 'debut' : tab1['Time'], 'jour': tab1['jour_de_la_semaine'] }
# tf1 = pd.DataFrame(data=t1) 
# tf1.drop_duplicates(subset='date', keep='first', inplace=True) #on supprime 
# #toutes les lignes dont la date apparait en doublon excepté la première pour 
# #connaitre l'horaire de début de journée pour chaque jour
 
# #Le deuxième, quand la journée se termine
# t2 = {'date': tab1['date'], 'fin' : tab1['Time'], 'jour': tab1['jour_de_la_semaine'] }
# tf2 = pd.DataFrame(data=t2)
# tf2.drop_duplicates(subset='date', keep='last', inplace=True)#on supprime 
# #toutes les lignes dont la date apparait en doublon excepté la dernière pour 
# #connaitre l'heure de la fin de journée pour chaque jour

# #On affiche nos résultats
# print ('Les périodes doccupations de bureaux')
# print ('Les journées commencent à :')
# print (tf1)
# print ('Puis se terminent à:')
# print (tf2)

##############################################################################              




    
