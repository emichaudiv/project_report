#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd


# In[2]:


#Import all the things to work


# In[3]:


from aqcuire import telco_data


# In[15]:


telco = telco_data()


# In[5]:


#Disaster, I can not use the aquired data due to 'null' being foreign, I tried to create a value for null, 
#but it was Ignored


# In[16]:


telco_prep= telco.drop(columns=['senior_citizen',
                             'partner',
                             'dependents',
                             'internet_service_type_id',
                             'online_security',
                             'device_protection',
                             'tech_support',
                             'paperless_billing',
                             'payment_type_id'])


# In[9]:


#Dropping what doesn't seem necessary 


# In[17]:


telco_prep.head()


# In[11]:


#And it's time for the main project

