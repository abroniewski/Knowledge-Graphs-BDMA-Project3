#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import pandas as pd  
import math
import warnings
random.seed(5)


# In[2]:


# ignore the warning
warnings.filterwarnings('ignore')


# In[3]:


filepath = '../data/raw/publication-data/'


# In[115]:


Papers = pd.read_csv(f"{filepath}Papers.csv")
Conferences = pd.read_csv(f"{filepath}Conferences.csv")
Authors = pd.read_csv(f"{filepath}Authors.csv")
Keyword_paper = pd.read_csv(f"{filepath}Keyword_paper.csv")
Keywords = pd.read_csv(f"{filepath}Keywords.csv")
Journals = pd.read_csv(f"{filepath}Journals.csv")


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
    Paper[['id', 'type']].to_csv(f"{filepath}Papers_type.csv",index=False)


# In[13]:


types_creation_paper(Papers)


# In[14]:


def types_creation_conference(Conference):
    Conference['type'] = ""
    types = ["workshop", "symposium", "regular conference", "expert group"]
    for a in range(len(Conference['type'])):

           Conference['type'][a] = random.choice(types)
            
#the colums id is the id of each conference         
    Conference[['id', 'type']].to_csv(f"{filepath}Conferences_type.csv",index=False)


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
        
    Submition.to_csv(f"{filepath}Submitions.csv",index=False)


# In[44]:


submition_data_creation(Papers)


# In[11]:


def reviewer_data_creation(Paper , Author ):
    
    amount_of_papers = len(Papers['title'])
    Reviewers = pd.DataFrame({'reviewer' : [None] *2*amount_of_papers, 'idR': [None] *2*amount_of_papers, 
                              'idS': [None] *2*amount_of_papers})
    Paper[['idS']] = ""
    
    for a in range(amount_of_papers):
        Paper['idP'][a] = f'p{a}'
        
    for a in range(amount_of_papers*2):
        Reviewers['reviewer'][a] = random.choice(Author['name'])
        Reviewers['idR'][a] = f'r{a}'
        Reviewers['idS'][a] = f's{math.floor(a/2)}'
    
    Reviewers.to_csv(f"{filepath}Reviewers.csv",index=False)


# In[12]:


reviewer_data_creation(Papers , Authors )


# In[87]:


def chair_data_creadion(Paper, Author):
    amount_of_conferences = sum(Paper['confjournal'] == 'Conference')
    Chairs = pd.DataFrame({'chair' : [None] *amount_of_conferences, 'idCC': [None] *amount_of_conferences, 
                              'idC': [None] *amount_of_conferences})
    for a in range(amount_of_conferences):
        Chairs['idC'][a] = f'c{a}'
        Chairs['idCC'][a] = f'cc{a}'
        Chairs['chair'][a] = random.choice(Author['name'])
        
    Chairs.to_csv(f"{filepath}Chairs.csv",index=False)        


# In[88]:


chair_data_creadion(Papers, Authors)


# In[89]:


def editor_data_creadion(Paper, Author):
    amount_of_journals = sum(Paper['confjournal'] == 'Journal')
    Editor = pd.DataFrame({'editor' : [None] *amount_of_journals, 'idJE': [None] *amount_of_journals, 
                              'idJ': [None] *amount_of_journals})
    for a in range(amount_of_journals):
        Editor['idJ'][a] = f'j{a}'
        Editor['idJE'][a] = f'je{a}'
        Editor['editor'][a] = random.choice(Author['name'])
        
    Editor.to_csv(f"{filepath}Editors.csv",index=False)


# In[90]:


editor_data_creadion(Papers, Authors)


# In[82]:


def keywords_journal_set(Paper, Keyword_paper,Journal, Keywords ):
    
    Paper = pd.DataFrame(Paper[Paper['confjournal'] == 'Journal'])
    Paper = Paper.set_index('idP').join(Keyword_paper.set_index('idP'), how='inner').reset_index('idP')
    Paper = Paper.set_index('idK').join(Keywords.set_index('idK'), how='inner').reset_index('idK')
    Paper = Journal.set_index('idJ').join(Paper.set_index('idEidV'), how='inner').reset_index()
    Paper.rename(columns = {'index':'idJ'}, inplace = True)
        
    Paper[['journal','idJ','idP', 'title', 'idK', 'keyword' ]].to_csv(f"{filepath}Keyword_journal.csv",index=False)


# In[85]:


keywords_journal_set(Papers, Keyword_paper,Journals, Keywords )


# In[88]:


def keywords_conference_set(Paper, Keyword_paper,Conference, Keywords ):
    
    Paper = pd.DataFrame(Paper[Paper['confjournal'] == 'Conference'])
    Paper = Paper.set_index('idP').join(Keyword_paper.set_index('idP'), how='inner').reset_index('idP')
    Paper = Paper.set_index('idK').join(Keywords.set_index('idK'), how='inner').reset_index('idK')
    Paper = Conference.set_index('idC').join(Paper.set_index('idEidV'), how='inner').reset_index()
    Paper.rename(columns = {'index':'idC'}, inplace = True)
        
    Paper[['conference','idC','idP', 'title', 'idK', 'keyword' ]].to_csv(f"{filepath}Keyword_conference.csv",index=False)


# In[89]:


keywords_conference_set(Papers, Keyword_paper,Conferences, Keywords )


# In[ ]:


#using already generated csv to generate new ones


# In[134]:


Reviewers = pd.read_csv(f"{filepath}Reviewers.csv")
Submitions = pd.read_csv(f"{filepath}Submitions.csv")
Editors = pd.read_csv(f"{filepath}Editors.csv")
Chairs = pd.read_csv(f"{filepath}Chairs.csv")
JVolumes = pd.read_csv(f"{filepath}JVolumes.csv")
CEditions = pd.read_csv(f"{filepath}CEditions.csv")


# In[138]:


def editor_reviewer_set(Reviewers, Submitions, Papers, JVolumes, Editors ):
    
    Reviewers = Reviewers.set_index('idS').join(Submitions.set_index('idS')).reset_index('idS')
    Reviewers = Reviewers.set_index('idP').join(Papers[['idEidV','idP']].set_index('idP')).reset_index('idP')
    Reviewers = JVolumes.set_index('idJV').join(Reviewers.set_index('idEidV')).reset_index()
    Editors = Editors.set_index('idJ').join(Reviewers.set_index('idJ')).reset_index()
    Editors.rename(columns = {'index':'idJV'}, inplace = True)
    
    Editors[['editor','idJE', 'idJ', 'reviewer','idR','idJV', 'idP'  ]].to_csv(f"{filepath}Editor_reviewers.csv",index=False)


# In[139]:


editor_reviewer_set(Reviewers, Submitions, Papers, JVolumes, Editors )


# In[144]:


def chair_reviewer_set(Reviewers, Submitions, Papers, CEditions, Chairs ):
    
    Reviewers = Reviewers.set_index('idS').join(Submitions.set_index('idS')).reset_index('idS')
    Reviewers = Reviewers.set_index('idP').join(Papers[['idEidV','idP']].set_index('idP')).reset_index('idP')
    Reviewers = CEditions.set_index('idCE').join(Reviewers.set_index('idEidV')).reset_index()
    Chairs = Chairs.set_index('idC').join(Reviewers.set_index('idC')).reset_index()
    Chairs.rename(columns = {'index':'idCE'}, inplace = True)
    
    Chairs[['chair','idCC', 'idC', 'reviewer','idR','idCE', 'idP'  ]].to_csv(f"{filepath}Chair_reviewers.csv",index=False)


# In[145]:


chair_reviewer_set(Reviewers, Submitions, Papers, CEditions, Chairs )

