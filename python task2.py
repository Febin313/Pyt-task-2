#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
d = pd.read_csv('C:\\Users\\user\\Downloads\\01.Data Cleaning and Preprocessing.csv')
type(d)


# In[3]:


d.info


# In[4]:


d.head()


# In[5]:


d.tail()


# In[6]:


d.drop_duplicates()


# In[7]:


d.isnull().sum()


# In[8]:


d.notnull()


# In[9]:


d.isnull().sum().sum()


# In[10]:


d1=d.fillna(0)
d1


# In[11]:


d1.ffill(inplace=True)
d1


# In[12]:


d1.bfill(inplace=True)
d1


# In[13]:


import matplotlib as plt
from scipy import stats
d.columns


# In[14]:


d.drop(['Observation'],axis=1,inplace=True)
d.columns


# In[16]:


q1=d.quantile(0.25)
q3=d.quantile(0.75)
iqr=q3=q1
print(iqr)


# In[18]:


d=d[-((d<(q1-1.5*iqr))|(d>(q3+1.5*iqr))).any(axis=1)]
d


# In[19]:


d.describe()


# In[ ]:




