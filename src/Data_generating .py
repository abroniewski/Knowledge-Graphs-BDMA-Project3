#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import pandas as pd  
random.seed(5)


# In[11]:


Paper = pd.read_csv('../data/processed/Papers.csv')
Conferences = pd.read_csv('../data/processed/Conferences.csv')


# In[12]:


def types_creation_paper(Paper):
    Paper['type'] = ""
    
#assumed that all papers from conferences have a type - 'poster', a journal's paper has one of three types 
# "full paper", "short paper" or "demo paper"
    types = ["full paper", "short paper", "demo paper"]
    for a in range(len(Paper['type'])):
        if Paper['confjournal'][a] == "Journal":
 
            Paper['type'][a] = random.choice(types)
    
        else:
            Paper['type'][a] = "poster"
            
#the colums id is the id of each journal         
    Paper[['id', 'type']].to_csv('../data/processed/Papers_type.csv',index=False)


# In[13]:


types_creation_paper(Paper)


# In[14]:


def types_creation_conference(Conference):
    Conference['type'] = ""
    types = ["workshop", "symposium", "regular conference", "expert group"]
    for a in range(len(Conference['type'])):

           Conference['type'][a] = random.choice(types)
            
#the colums id is the id of each conference         
    Conference[['id', 'type']].to_csv('../data/processed/Conferences_type.csv',index=False)


# In[15]:


types_creation_conference(Conferences)


# In[ ]:




