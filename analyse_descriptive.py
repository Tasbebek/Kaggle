# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 14:47:53 2017

@author: 140395
"""
import pandas as pd
import numpy as np
import sklearn.ensemble as sk_ens

#conversion de tous les fichiers en data frame

train = pd.read_csv('train.csv', sep=',')

sevt = pd.read_csv('severity_type.csv')

element = pd.read_csv('event_type.csv')

feature = pd.read_csv('log_feature.csv')

resource = pd.read_csv('resource_type.csv')

test = pd.read_csv('test.csv')

#fusion des dataframe entre eux

#m_df = train.merge(sevt, on='id', how='left')

m_df = pd.merge(train, sevt, on='id', how='left')
m_df2 = pd.merge(m_df, element, on='id', how='left')
m_df3 = pd.merge(m_df2, feature, on='id', how='left')
m_df4 = pd.merge(m_df3, resource, on='id', how='left')
#m_df5 = pd.merge(m_df4, test, on='id', how='left')


#suppression de l'index

#essai d'algorithme de random forest
"""
X = m_df4[, ]
clf = sk_ens.ExtraTreesClassifier(n_estimators=6, max_depth=None, min_samples_split=2, random_state=0)
scores = cross_val_score(clf, )
"""
print(m_df4)