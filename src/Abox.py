#!/usr/bin/env python
# coding: utf-8

# In[36]:


from rdflib.namespace import RDF, RDFS, FOAF, XSD
from rdflib import Graph
import pandas as pd
from rdflib import Namespace
from rdflib import Literal


# In[28]:


# Create a Graph
g = Graph()


# In[168]:


#upload a csv file with instances 
Author = pd.read_csv('/home/vladka/Downloads/output/Authors.csv') 
Papers = pd.read_csv('/home/vladka/Downloads/output/Papers.csv') 
Author_by = pd.read_csv('/home/vladka/Downloads/output/Authored_by.csv')
Affiliations = pd.read_csv('/home/vladka/Downloads/output/Affiliations.csv')
CEditions = pd.read_csv('/home/vladka/Downloads/output/CEditions.csv')
Citations = pd.read_csv('/home/vladka/Downloads/output/Citations.csv')
Conferences = pd.read_csv('/home/vladka/Downloads/output/Conferences.csv')
Journals = pd.read_csv('/home/vladka/Downloads/output/Journals.csv')
JVolumes = pd.read_csv('/home/vladka/Downloads/output/JVolumes.csv')
Keyword_paper = pd.read_csv('/home/vladka/Downloads/output/Keyword_paper.csv')
Keywords = pd.read_csv('/home/vladka/Downloads/output/Keywords.csv')
Organizations = pd.read_csv('/home/vladka/Downloads/output/Organizations.csv')
Reviews = pd.read_csv('/home/vladka/Downloads/output/Reviews.csv')


# In[90]:


Author_Papers = (Author.set_index('id').join(Author_by.set_index('idA'))).set_index('idP').join(Papers.set_index('id')).reset_index()


# In[184]:


Author_Papers.head()


# In[130]:


Keyword_Papers = Keywords.set_index('id').join(Keyword_paper.set_index('idK')).set_index('idP').join(Papers.set_index('id')).reset_index()


# In[185]:


Keyword_Papers.head()


# In[191]:


Journal_Keyword = Journals.set_index('id').join(JVolumes.set_index('idJ')).set_index('id').join(Keyword_Papers.set_index('idEidV')).reset_index()


# In[192]:


Journal_Keyword.head()


# In[188]:


Paper_volume = Conferences.set_index('id').join(CEditions.set_index('idC')).set_index('id').join(Keyword_Papers.set_index('idEidV')).reset_index()


# In[189]:


Paper_volume.head()


# In[196]:


Review_Papers = Reviews.set_index('idA').join(Author.set_index('id')).set_index('idP').join(Papers.set_index('id')).reset_index()


# In[197]:


Review_Papers.head()


# In[198]:


Editor_Chair = Review_Papers.merge(Journal_Keyword, left_on='title', right_on='title',
                                   how='left').merge(Paper_volume, left_on='title', 
                                                     right_on='title',how='left')


# In[199]:


Editor_Chair.head()


# In[203]:


KG = Namespace("http://KG-SDM-Lab3.org/")
g.bind("kg", KG)

g.add((KG.Author, KG.participatedIn, KG.Paper))   
for k in range(len(Author_Papers['name'])):
    g.add((Literal(Author_Papers['name'][k]), KG.participatedIn, Literal(Author_Papers['title'][k])))

g.add((KG.Paper, KG.PaperRelatedTo, KG.SubjectArea))
for k in range(len(Keyword_Papers['keyword'])):
    g.add((Literal(Keyword_Papers['title'][k]), KG.PaperRelatedTo, Literal(Keyword_Papers['keyword'][k])))

g.add((KG.Journal, KG.JournalRelatedTo, KG.SubjectArea))
for k in range(len(Journal_Keyword['keyword'])):
    g.add((Literal(Journal_Keyword['journal'][k]), KG.JournalRelatedTo, Literal(Journal_Keyword['keyword'][k])))

g.add((KG.Conference, KG.ConferenceRelatedTo, KG.SubjectArea))
for k in range(len(Paper_volume['keyword'])):
    g.add((Literal(Paper_volume['conference'][k]), KG.ConferenceRelatedTo, Literal(Paper_volume['keyword'][k])))

g.add((KG.Journal, KG.published, KG.Volume))
for k in range(len(Journal_Keyword['journal'])):
    g.add((Literal(Journal_Keyword['journal'][k]), KG.published, Literal(Journal_Keyword['volume'][k])))

g.add((KG.Conference, KG.published, KG.Proceeding))
for k in range(len(Paper_volume['conference'])):
    g.add((Literal(Paper_volume['conference'][k]), KG.published, Literal(Paper_volume['date'][k])))

g.add((KG.Reviewer, KG.decided, KG.Decision))
for k in range(len(Review_Papers['name'])):
    g.add((Literal(Review_Papers['name'][k]), KG.decided, Literal(Review_Papers['decision'][k])))


g.add((KG.Conference, KG.handledBy, KG.Chair))
g.add((KG.Journal, KG.handledBy, KG.Editor))
for k in range(len(Editor_Chair['conference'])):
    if Editor_Chair['confjournal'][k] == 'Conference':
        g.add((Literal(Editor_Chair['conference'][k]), KG.handledBy, Literal(Editor_Chair['name'][k])))
    else:
        g.add((Literal(Editor_Chair['journal'][k]), KG.handledBy, Literal(Editor_Chair['name'][k])))
        
#Not resonable       
g.add((KG.Chair, KG.assigned, KG.Reviewer))
g.add((KG.Editor, KG.assigned, KG.Reviewer))
for k in range(len(Editor_Chair['conference'])):
    if Editor_Chair['confjournal'][k] == 'Conference':
        g.add((Literal(Editor_Chair['name'][k]), KG.assigned, Literal(Editor_Chair['name'][k])))
    else:
        g.add((Literal(Editor_Chair['name'][k]), KG.assigned, Literal(Editor_Chair['name'][k])))
        
g.add((KG.Reviewer, KG.reviewed, KG.Submission))
g.add((Literal(Editor_Chair['name'][k]), KG.reviewed, Literal(int(Editor_Chair['date_y'][k]))))


# In[204]:


g


# In[ ]:




