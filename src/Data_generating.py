#!/usr/bin/env python
# coding: utf-8

# In[66]:


import random
import pandas as pd  
import math
import warnings
random.seed(5)


# In[42]:


# ignore the warning
warnings.filterwarnings('ignore')


# In[51]:


Papers = pd.read_csv('../data/raw/publication-data/Papers.csv')
Conferences = pd.read_csv('../data/raw/publication-data/Conferences.csv')
Authors = pd.read_csv('../data/raw/publication-data/Authors.csv')
Reviews = pd.read_csv('../data/raw/publication-data/Reviews.csv')

# In[12]:


def types_creation_paper(Paper):
    Paper['type'] = ""
    
#assumed that all papers from conferences have a type - 'poster', a journal's paper has one of three types 
# "full paper", "short paper" or "demo paper"
    types = ["full paper", "short paper", "demo paper"]
    for a in range(len(Paper['type'])):
        if Papers['confjournal'][a] == "Journal":
 
            Paper['type'][a] = random.choice(types)
    
        else:
            Paper['type'][a] = "poster"
            
#the colums id is the id of each journal         
    Paper[['idP', 'type']].to_csv('../data/processed/Papers_type.csv',index=False)


# In[13]:


types_creation_paper(Papers)


# In[14]:


def types_creation_conference(Conference):
    Conference['type'] = ""
    types = ["workshop", "symposium", "regular conference", "expert group"]
    for a in range(len(Conference['type'])):

           Conference['type'][a] = random.choice(types)
            
#the colums id is the id of each conference         
    Conference[['idC', 'type']].to_csv('../data/raw/publication-data/Conferences_type.csv',index=False)


# In[15]:


types_creation_conference(Conferences)


# In[43]:


def submition_data_creation(Paper):
    
    Submition = Paper[ ['title']]
    Submition['idS'] = ""
    Submition['idP'] = ""
    
    for a in range(len(Submition['idS'])):
    
        Submition['idS'][a] = f's{a}'
        Submition['idP'][a] = f'p{a}'
        
    Submition.to_csv('../data/raw/publication-data/Submissions.csv',index=False)


# In[44]:


submition_data_creation(Papers)


# In[78]:


def submission_data_creation(Paper, Author):
    
    amount_of_papers = len(Papers['title'])
    Reviewers = pd.DataFrame({'name' : [None] *2*amount_of_papers, 'idR': [None] *2*amount_of_papers, 
                              'idP': [None] *2*amount_of_papers})
    Paper[['idP']] = ""
    
    for a in range(amount_of_papers):
        Paper['idP'][a] = f'p{a}'
        
    for a in range(amount_of_papers*2):
        Reviewers['name'][a] = random.choice(Author['name'])
        Reviewers['idR'][a] = f'r{a}'
        Reviewers['idP'][a] = f'p{math.floor(a/2)}'
        
    Reviewers.join(Paper.set_index('idP'), on='idP')

    Reviewers.to_csv('../data/raw/publication-data/Reviewers.csv',index=False)


# In[ ]:


submission_data_creation(Papers, Authors)


# In[87]:


def chair_data_creadion(Paper, Author):
    amount_of_conferences = sum(Paper['confjournal'] == 'Conference')
    Chairs = pd.DataFrame({'name' : [None] *amount_of_conferences, 'idCC': [None] *amount_of_conferences, 
                              'idC': [None] *amount_of_conferences})
    for a in range(amount_of_conferences):
        Chairs['idC'][a] = f'c{a}'
        Chairs['idCC'][a] = f'cc{a}'
        Chairs['name'][a] = random.choice(Author['name'])
        
    Chairs.to_csv('../data/raw/publication-data/Chairs.csv',index=False)


# In[88]:


chair_data_creadion(Papers, Authors)


# In[89]:


def chair_data_creadion(Paper, Author):
    amount_of_journals = sum(Paper['confjournal'] == 'Journal')
    Editor = pd.DataFrame({'name' : [None] *amount_of_journals, 'idJE': [None] *amount_of_journals, 
                              'idJ': [None] *amount_of_journals})
    for a in range(amount_of_journals):
        Editor['idJ'][a] = f'j{a}'
        Editor['idJE'][a] = f'je{a}'
        Editor['name'][a] = random.choice(Author['name'])
        
    Editor.to_csv('../data/raw/publication-data/Editors.csv',index=False)


# In[90]:


chair_data_creadion(Papers, Authors)


# In[ ]:




