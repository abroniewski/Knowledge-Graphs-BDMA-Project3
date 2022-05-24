# ABOX definition
import pandas as pd
from rdflib.namespace import RDF, RDFS, FOAF, XSD
from rdflib import Graph
from rdflib import Namespace
from rdflib import Literal

#%% Import CSVs
filepath = '../data/raw/publication-data/'
Affiliations = pd.read_csv(f"{filepath}Affiliations.csv")
Authored_by = pd.read_csv(f"{filepath}Authored_by.csv")
Authors = pd.read_csv(f"{filepath}Authors.csv")
CEditions = pd.read_csv(f"{filepath}CEditions.csv")
Chairs = pd.read_csv(f"{filepath}Chairs.csv")
Conferences = pd.read_csv(f"{filepath}Conferences.csv")
Conferences_type = pd.read_csv(f"{filepath}Conferences_type.csv")
Editors = pd.read_csv(f"{filepath}Editors.csv")
Journals = pd.read_csv(f"{filepath}Journals.csv")
JVolumes = pd.read_csv(f"{filepath}JVolumes.csv")
Keyword_paper = pd.read_csv(f"{filepath}Keyword_paper.csv")
Keywords = pd.read_csv(f"{filepath}Keywords.csv")
Papers = pd.read_csv(f"{filepath}Papers.csv")
Papers_type = pd.read_csv(f"{filepath}Papers_type.csv")
Reviewers = pd.read_csv(f"{filepath}Reviewers.csv")
Reviews = pd.read_csv(f"{filepath}Reviews.csv")
Submissions = pd.read_csv(f"{filepath}Submissions.csv")

g = Graph()
KG = Namespace("http://KG-SDM-Lab3.org/")
g.bind("kg", KG)

for index, row in Authors.iterrows():
    id_A = row['idA']
    name = row['name']
    g.add((KG[id_A], RDF.type, KG.Author))
    g.add((KG[id_A], RDFS.label, Literal(name)))


# Create instances of Authors, Papers (of different subtypes) and connect them
for index, row in Papers_type.iterrows():
    id_paper = row['idP']  # use the unique paper id as the URI
    paper_type = row['type']

    if paper_type == "full paper":
        g.add((KG[id_paper], RDF.type, KG.FullPaper))
    elif paper_type == "demo paper":
        g.add((KG[id_paper], RDF.type, KG.DemoPaper))
    elif paper_type == "poster":
        g.add((KG[id_paper], RDF.type, KG.Poster))
    elif paper_type == "short paper":
        g.add((KG[id_paper], RDF.type, KG.ShortPaper))

for index, row in Papers.iterrows():
    id_P = row['idP']
    title = row['title']
    g.add((KG[id_P], KG.title, Literal(title)))

for index, row in Journals.iterrows():
    id_J = row['idJ']
    title = row['journal']
    g.add((KG[id_J], RDF.type, KG.Journal))
    g.add((KG[id_J], KG.title, Literal(title)))

# TODO: TOBX add Journal volume
for index, row in JVolumes.iterrows():
    id_J = row['idJ']
    id_JV = row['idJV']
    volume = row['volume']
    g.add((KG[id_J], KG.Volume, KG[id_JV]))
    g.add((KG[id_JV], KG.title, Literal(volume)))

for index, row in Conferences_type.iterrows():
    id_conf = row['idC']
    conf_type = row['type']

    if conf_type == "workshop":
        g.add((KG[id_conf], RDF.type, KG.Workshop))
    elif conf_type == "expert group":
        g.add((KG[id_conf], RDF.type, KG.ExpertGroup))
    elif conf_type == "symposium":
        g.add((KG[id_conf], RDF.type, KG.Symposium))
    elif conf_type == "regular conference":
        g.add((KG[id_conf], RDF.type, KG.RegularConference))

for index, row in Conferences.iterrows():
    id_conf = row['idC']
    conf_name = row['conference']
    g.add((KG[id_conf], KG.title, Literal(conf_name)))

for index, row in CEditions.iterrows():
    id_CE = row['idCE']
    id_C = row['idC']
    date = row['date']
    g.add((KG[id_J], KG.Volume, KG[id_JV]))
    g.add((KG[id_JV], RDFS.label, Literal(volume)))

# TODO: CSV Papers to show specific volume (idJV) or edition (idCE) (not which idJ or idC)
for index, row in Papers.iterrows():
    id_P = row['idP']
    idEidV = row['idEidV']
    g.add((KG[id_P], KG.publishedIn, KG[idEidV]))

for index, row in Keywords.iterrows():
    id_kw = row['idK']
    keyword = row['keyword']
    g.add((KG[id_kw], RDF.type, KG.SubjectArea))
    g.add((KG[id_kw], RDFS.label, Literal(keyword)))

for index, row in Chairs.iterrows():
    id_Chair = row['idCC']
    id_Conf = row['idC']
    g.add((KG[id_Chair], RDF.type, KG.Chair))
    g.add((KG[id_Chair], KG.chairs, KG[id_Conf]))

for index, row in Editors.iterrows():
    id_Editor = row['idJE']
    id_J = row['idJ']
    g.add((KG[id_Editor], RDF.type, KG.Editor))
    g.add((KG[id_Editor], KG.edits, KG[id_J]))

# TODO: CSV Reviews.csv, change idP to idS
# TODO: in TBOX add Review as a class to keep track of a specific review related to a submission
# TODO: in TBOX change property of reviewed
for index, row in Reviews.iterrows():
    id_A = row['idA']
    id_S = row['idS']
    id_R = id_S + id_A
    comment = row['content']
    if row['decision'] == "Accepted":
        decided = True
    elif row['decision'] == "Rejected":
        decided = False
    g.add((KG[id_A], RDF.type, KG.Reviewer))
    g.add((KG[id_R], RDF.type, KG.ReviewContent))
    g.add((KG[id_A], KG.reviewed, KG[id_R]))
    g.add((KG[id_R], KG.review, KG[id_S]))
    g.add((KG[id_R], KG.commented, Literal(comment)))
    g.add((KG[id_R], KG.decided, Literal(decided)))

#################################################################
#    Properties
#################################################################
for index, row in Authored_by.iterrows():
    id_A = row['idA']
    id_P = row['idP']
    g.add((KG[id_A], KG.participatedIn, KG[id_P]))  # creates link between paper/name

for index, row in Keyword_paper.iterrows():
    id_K = row['idK']
    id_P = row['idP']
    g.add((KG[id_P], KG.paperRelatedTo, KG[id_K]))

# TODO: CSV add new file Keyword_conference.csv
for index, row in Keyword_conference.iterrows():
    id_K = row['idK']
    id_P = row['idC']
    g.add((KG[id_C], KG.venueRelatedTo, KG[id_K]))

# TODO: CSV add new file Keyword_journal.csv
for index, row in Keyword_journal.iterrows():
    id_K = row['idK']
    id_P = row['idJ']
    g.add((KG[id_J], KG.venueRelatedTo, KG[id_K]))

# TODO: CSV add new file Editor_reviewers.csv showing which editor assigned which reviewer
# TODO: ABOX add editor/reviewer code

# TODO: CSV add new file Chair_reviewers.csv showing which chair assigned which reviewer
# TODO: ABOX add chair/reviewer code


# for index, row in Paper_Submissions.iterrows():
#     id_paper = row['idP']
#     id_submission = row['idS']
#     submission_name = row['submission_name']
#
#     g.add((KG[id_submission], RDF.type, KG.Submission))
#     g.add((KG[id_submission], RDFS.label, Literal(submission_name)))
#     g.add((KG[id_paper], KG.submitted, KG[id_submission]))




g.serialize(destination=f'../data/processed/adams-output.ttl')
