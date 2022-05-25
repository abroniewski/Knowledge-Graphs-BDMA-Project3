
import random
import pandas as pd  
import math
import warnings
random.seed(5)

# ignore the warning
warnings.filterwarnings('ignore')

filepath = '../data/raw/publication-data/'
outpath = '../data/processed/'

Papers = pd.read_csv(f"{filepath}Papers.csv")
Conferences = pd.read_csv(f"{filepath}Conferences.csv")
Authors = pd.read_csv(f"{filepath}Authors.csv")
Keyword_paper = pd.read_csv(f"{filepath}Keyword_paper.csv")
Keywords = pd.read_csv(f"{filepath}Keywords.csv")
Journals = pd.read_csv(f"{filepath}Journals.csv")
Reviews = pd.read_csv(f"{filepath}Reviews.csv")

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
    Paper[['id', 'type']].to_csv(f"{outpath}Papers_type.csv",index=False)


types_creation_paper(Papers)


def types_creation_conference(Conference):
    Conference['type'] = ""
    types = ["workshop", "symposium", "regular conference", "expert group"]
    for a in range(len(Conference['type'])):

           Conference['type'][a] = random.choice(types)
            
#the colums id is the id of each conference         
    Conference[['id', 'type']].to_csv(f"{outpath}Conferences_type.csv",index=False)


types_creation_conference(Conferences)


def submition_data_creation(Paper):
    
    Submition = Paper[ ['title']]
    Submition['idS'] = ""
    Submition['idP'] = ""
    
    for a in range(len(Submition['idS'])):
    
        Submition['idS'][a] = f's{a}'
        Submition['idP'][a] = f'p{a}'
        
    Submition.to_csv(f"{outpath}Submitions.csv",index=False)


submition_data_creation(Papers)


def reviewer_data_creation(Paper , Author ):
    
    amount_of_papers = len(Papers['title'])
    Reviewers = pd.DataFrame({'idR' : [None] *2*amount_of_papers, 'idA': [None] *2*amount_of_papers,
                              'idS': [None] *2*amount_of_papers})
    Paper[['idS']] = ""
    Paper.rename(columns={'id': 'idP'}, inplace=True)
    Author.rename(columns={'id': 'idA'}, inplace=True)
    
    for a in range(amount_of_papers):
        Paper['idP'][a] = f'p{a}'
        
    for a in range(amount_of_papers*2):
        Reviewers['idR'][a] = random.choice(Author['idA'])
        # Reviewers['idR'][a] = f'r{a}'
        # TODO: Why are we assigning the same submission to same paper?
        Reviewers['idS'][a] = f's{math.floor(a/2)}'
        
    Reviewers = Reviewers.set_index('idA').join(Author.set_index('idA')).reset_index()
    Reviewers.rename(columns = {'index': 'reviewer'}, inplace = True)
    
    Reviewers.to_csv(f"{outpath}Reviewers.csv",index=False)
    Author.to_csv(f"{outpath}Authors.csv",index=False)
    Paper.to_csv(f"{outpath}Papers.csv", index=False)

reviewer_data_creation(Papers , Authors )
Papers = pd.read_csv(f"{outpath}Papers.csv")


def chair_data_creadion(Paper, Author):
    amount_of_conferences = sum(Paper['confjournal'] == 'Conference')
    Chairs = pd.DataFrame({'chair' : [None] *amount_of_conferences, 'idCC': [None] *amount_of_conferences, 
                              'idC': [None] *amount_of_conferences})
    for a in range(amount_of_conferences):
        Chairs['idC'][a] = f'c{a}'
        Chairs['idCC'][a] = f'cc{a}'
        Chairs['chair'][a] = random.choice(Author['name'])
        
    Chairs.to_csv(f"{outpath}Chairs.csv",index=False)


chair_data_creadion(Papers, Authors)


def editor_data_creadion(Paper, Author):
    amount_of_journals = sum(Paper['confjournal'] == 'Journal')
    Editor = pd.DataFrame({'editor' : [None] *amount_of_journals, 'idJE': [None] *amount_of_journals, 
                              'idJ': [None] *amount_of_journals})
    for a in range(amount_of_journals):
        Editor['idJ'][a] = f'j{a}'
        Editor['idJE'][a] = f'je{a}'
        Editor['editor'][a] = random.choice(Author['name'])
        
    Editor.to_csv(f"{outpath}Editors.csv",index=False)


editor_data_creadion(Papers, Authors)



def keywords_journal_set(Paper, Keyword_paper, Journal, Keywords):
    
    Paper = pd.DataFrame(Paper[Paper['confjournal'] == 'Journal'])
    Paper = Paper.set_index('idP').join(Keyword_paper.set_index('idP'), how='inner').reset_index('idP')
    # TODO: the next join returns nothing because the idK of keywords does not have the "k" in the id.
    Paper = Paper.set_index('idK').join(Keywords.set_index('idK'), how='inner').reset_index('idK')
    Paper = Journal.set_index('idJ').join(Paper.set_index('idEidV'), how='inner').reset_index()
    Paper.rename(columns = {'idEidV':'idJ'}, inplace = True)
        
    Paper[['idJ', 'idK']].to_csv(f"{outpath}Keyword_journal.csv",index=False)
    Paper.to_csv(f"{outpath}Paper.csv",index=False)

keywords_journal_set(Papers, Keyword_paper,Journals, Keywords )
Papers = pd.read_csv(f"{outpath}Papers.csv")


def keywords_conference_set(Paper, Keyword_paper,Conference, Keywords ):
    
    Paper = pd.DataFrame(Paper[Paper['confjournal'] == 'Conference'])
    Paper = Paper.set_index('idP').join(Keyword_paper.set_index('idP'), how='inner').reset_index('idP')
    # TODO: remove, these two are just joining with the string keyword and titles
    Paper = Paper.set_index('idK').join(Keywords.set_index('idK'), how='inner').reset_index('idK')
    Paper = Conference.set_index('idC').join(Paper.set_index('idEidV'), how='inner').reset_index()
    Paper.rename(columns = {'idEidV':'idC'}, inplace = True)
        
    Paper[['idC','idK']].to_csv(f"{outpath}Keyword_conference.csv",index=False)
    Paper.to_csv(f"{outpath}Paper.csv", index=False)


keywords_conference_set(Papers, Keyword_paper,Conferences, Keywords )


#using already generated csv to generate new ones
Reviewers = pd.read_csv(f"{outpath}Reviewers.csv")
Papers = pd.read_csv(f"{outpath}Papers.csv")
Submitions = pd.read_csv(f"{outpath}Submitions.csv")
Editors = pd.read_csv(f"{outpath}Editors.csv")
Chairs = pd.read_csv(f"{outpath}Chairs.csv")
JVolumes = pd.read_csv(f"{filepath}JVolumes.csv")
CEditions = pd.read_csv(f"{filepath}CEditions.csv")


def editor_reviewer_set(Reviewers, Submitions, Papers, JVolumes, Editors ):

    amount_of_journals = len(JVolumes['volume'])
    for a in range(amount_of_journals):
        JVolumes['idJ'][a] = f'j{a}'

    Reviewers = Reviewers.set_index('idS').join(Submitions.set_index('idS')).reset_index('idS')
    Reviewers = Reviewers.set_index('idP').join(Papers[['idEidV','idP']].set_index('idP')).reset_index('idP')
    Reviewers = JVolumes.set_index('idJ').join(Reviewers.set_index('idEidV')).reset_index()
    Editors = Editors.set_index('idJ').join(Reviewers.set_index('idJ')).reset_index()
    Editors.rename(columns = {'index':'idJV'}, inplace = True)
    
    Editors[['editor','idJE', 'idJ', 'reviewer','idR','idJV', 'idP'  ]].to_csv(f"{outpath}Editor_reviewers.csv",index=False)


editor_reviewer_set(Reviewers, Submitions, Papers, JVolumes, Editors )


def chair_reviewer_set(Reviewers, Submitions, Papers, CEditions, Chairs ):
    
    Reviewers = Reviewers.set_index('idS').join(Submitions.set_index('idS')).reset_index('idS')
    Reviewers = Reviewers.set_index('idP').join(Papers[['idEidV','idP']].set_index('idP')).reset_index('idP')
    Reviewers = CEditions.set_index('idCE').join(Reviewers.set_index('idEidV')).reset_index()
    Chairs = Chairs.set_index('idC').join(Reviewers.set_index('idC')).reset_index()
    Chairs.rename(columns = {'index':'idCE'}, inplace = True)
    
    Chairs[['chair','idCC', 'idC', 'reviewer','idR','idCE', 'idP'  ]].to_csv(f"{outpath}Chair_reviewers.csv",index=False)


chair_reviewer_set(Reviewers, Submitions, Papers, CEditions, Chairs )


def modify_reviews_id(Review, Submition):
    
    Review = Review.join(Submition.set_index('idP'), on="idP")
    Review[['idA', 'idS', 'decision', 'content']].to_csv(f"{outpath}Reviews.csv",index=False)

    
modify_reviews_id(Reviews, Submitions)
    
