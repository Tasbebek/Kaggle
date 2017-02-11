# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 21:05:23 2017

@author: Serife
"""
import pandas as pd


df_train = pd.read_csv('train.csv', sep=',')
df_sevt = pd.read_csv('severity_type.csv')
df_element = pd.read_csv('event_type.csv')
df_feature = pd.read_csv('log_feature.csv')
df_resource = pd.read_csv('resource_type.csv')
df_test = pd.read_csv('test.csv')


def change_values(df):
    """
    Pour un DataFrame, change les valeurs en int 
    """
    col_names = list(df) #Récupère la liste des noms de colonne
    df_bis = pd.DataFrame(index = [i for i in range(len(df["id"]))], columns = col_names) # Crée le DataFrame de même taille
    renom = False
    third_col = False
    
    try : #S'il peut séparer les élements de la 2ème colonne [location 2234] alors on doit modifier toute la colonne 
        df[col_names[1]][1].split() 
        renom = True
    except :
        pass
    
    
    col = col_names[1]

    if len(col_names) > 2 : #Si dans un DataFrame il y a plus de 2 colonnes (dans notre cas, au max 3)
        third_col = True
        
    print(renom, third_col)
    for i in range(len(df['id'])): #Pour chaque ligne du DataFrame
    
        if renom == True :
            
            value = df["{0}".format(col)][i] # Récupère le contenu de la case de la colonne 'col' à la i-ème ligne
            value = value.split()[1] # Sépare le contenu en fonction de l'espace > on a soit une liste à 2 élements (ou 1 mais non) et récupère le 2ème élément 
            df_bis["{0}".format(col)][i] = int(value) # Dans le dataframe temporaire place la 
            df_bis["id"][i] = df["id"][i] #Copie l'id
            
            if third_col: #Transforme les valeurs de la 3ème colonne en int
                
                df_bis[col_names[2]][i] = int(df[col_names[2]][i])
                
        else : #Pas de renommage 

                value = df["{0}".format(col)][i]
                df_bis["{0}".format(col)][i] = int(value) 
                df_bis["id"][i] = df["id"][i]

                if third_col :
                    df_bis[col_names[2]][i] = int(df[col_names[2]][i])
    return df_bis
    
print(df_train)    
df_train_bis = change_values(df_train)
print(df_train_bis)
df_train_bis.to_csv('train_bis.csv', index = False)

print(df_sevt)    
df_sevt_bis = change_values(df_sevt)
print(df_sevt_bis)
df_sevt_bis.to_csv('sevt_bis.csv', index = False)

print(df_element)    
df_element_bis = change_values(df_element)
print(df_element_bis)
df_element_bis.to_csv('element_bis.csv', index = False)

print(df_feature)    
df_feature_bis = change_values(df_feature)
print(df_feature_bis)
df_feature_bis.to_csv('feature_bis.csv', index = False)

print(df_resource)    
df_resource_bis = change_values(df_resource)
print(df_resource_bis)
df_resource_bis.to_csv('resource_bis.csv', index = False)


print(df_test)    
df_test_bis = change_values(df_test)
print(df_test_bis)
df_test_bis.to_csv('test_bis.csv', index = False)