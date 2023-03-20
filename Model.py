#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, plot_confusion_matrix
from pydataset import data
from prepare import telco_prep as telco


# In[12]:


telco.head()


# In[2]:


train, test = train_test_split(telco, 
                               stratify=telco['churn'], 
                               train_size=0.8, 
                               random_state=1729)

train, validate = train_test_split(train, 
                                   stratify=train['churn'], 
                                   train_size=0.7, 
                                   random_state=1729)


# In[3]:


X_train = train.drop(columns = ['churn','monthly_charges','tenure'])
y_train = train.churn


# In[4]:


X_validate = validate.drop(columns = ['churn','monthly_charges','tenure'])
y_validate = validate.churn


# In[5]:


X_test = test.drop(columns = ['churn','monthly_charges','tenure'])
y_test = test.churn


# In[73]:


def churn_sctr(train):
    
    sns.scatterplot(data = train,y='monthly_charges',x='tenure',hue='churn')
    plt.show()


# In[7]:


knn=KNeighborsClassifier(n_neighbors=1)


# In[8]:


knn.fit(train[['monthly_charges']],y_train)


# In[9]:


y_pred = knn.predict(train[['monthly_charges']])


# In[10]:


y_pred


# In[11]:


pd.DataFrame(y_pred).to_csv('test_pred.csv')


# In[69]:


def churn_count(train): 
    
    sns.countplot(x=train['churn'],data=telco)
    plt.show()


# In[70]:


def phone_churn(train):
    
    sns.countplot(x=train['phone_service'], data=train['churn'])
    plt.show()


# In[75]:


def mult_lines(train): 
    
    sns.countplot(x=train['multiple_lines'], data=train['churn'])
    plt.show()


# In[72]:


def contract_tenure_cnt(train):
    
    sns.countplot(x=train['contract_type_id'], data=train['churn'])
    plt.show()


# In[71]:


def contract_tenure(train): 
    
    sns.barplot(x=train['contract_type_id'], y=train['tenure'])
    plt.show()


# In[ ]:




