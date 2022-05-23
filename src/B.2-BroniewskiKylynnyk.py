# ABOX definition
import pandas as pd
from rdflib.namespace import RDF, RDFS, FOAF, XSD
from rdflib import Graph
import pandas as pd
from rdflib import Namespace
from rdflib import Literal

Author = pd.read_csv('../data/raw/publication-data/Authors.csv')
Papers = pd.read_csv('../data/raw/publication-data/Papers.csv')
Author_by = pd.read_csv('../data/raw/publication-data/Authored_by.csv')

Author.rename(columns={"id": "idA"}, inplace=True)
Author_Papers = Author.join(Author_by.set_index('idA'), on="idA").join(Papers.set_index('id'), on="idP")
Author_Papers['idP'] = Author_Papers['idP'].map('p{}'.format)

g = Graph()
KG = Namespace("http://KG-SDM-Lab3.org/")
g.bind("kg", KG)

# Create instances of Authors, Papers (of different subtypes) and connect them
for index, row in Author_Papers.iterrows():
    id_paper = row['idP']  # use the unique paper id as the URI
    id_author = row['idA']
    paper_type = row['paper_type']

    g.add((KG[id_author], RDF.type, KG.Author))  # this creates "name" as a type of Author
    g.add((KG[id_author], KG.name, Literal(row['name'])))  # adds human-readable string

    if paper_type == "fullpaper":
        g.add((KG[id_paper], RDF.type, KG.FullPaper))
    elif paper_type == "demopaper":
        g.add((KG[id_paper], RDF.type, KG.DemoPaper))
    elif paper_type == "poster":
        g.add((KG[id_paper], RDF.type, KG.Poster))
    elif paper_type == "shortpaper":
        g.add((KG[id_paper], RDF.type, KG.ShortPaper))


    g.add((KG[id_paper], KG.title, Literal(row['title'])))  # adds human-readable string
    g.add((KG[id_author], KG.participatedIn, KG[id_paper]))  # creates link between paper/name





g.serialize(destination=f'../data/processed/adams-output.ttl')
