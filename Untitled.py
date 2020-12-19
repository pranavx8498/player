#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import pickle
df=pd.read_csv('data.csv')
x=np.array(df.drop('international_reputation',axis=1))
y=np.array(df['international_reputation'])
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=10)
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(criterion='entropy',
 max_depth= 11,
 max_features= 2,
 n_estimators= 488)
model.fit(x_train,y_train)
model.score(x_test,y_test)
pickle.dump(model,open('model.pkl','wb'))


# In[ ]:




