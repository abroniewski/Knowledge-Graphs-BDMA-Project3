# TBOX definition
from rdflib import Graph
from rdflib.namespace import RDFS, RDF
from rdflib import URIRef


def create_TBOX():
    """
    Creates all classes, subclasses and properties through domain and range definitions.
    Each class must be created explicitly regardless of RDFS inference rules due to limitations
    in RDFlib capabilities.
    :return: None
    """

    # Creating superclasses
    Paper = URIRef(f'{baseURI}/Paper')
    graph.add((Paper, RDF.type, RDFS.Class))

    SubjectArea = URIRef(f'{baseURI}/SubjectArea')
    graph.add((SubjectArea, RDF.type, RDFS.Class))

    Submission = URIRef(f'{baseURI}/Submission')
    graph.add((Submission, RDF.type, RDFS.Class))

    Keyword = URIRef(f'{baseURI}/Keyword')
    graph.add((Keyword, RDF.type, RDFS.Class))

    Venue = URIRef(f'{baseURI}/Venue')
    graph.add((Venue, RDF.type, RDFS.Class))

    Author = URIRef(f'{baseURI}/Author')
    graph.add((Author, RDF.type, RDFS.Class))

    Organization = URIRef(f'{baseURI}/Organization')
    graph.add((Organization, RDF.type, RDFS.Class))

    Review = URIRef(f'{baseURI}/Review')
    graph.add((Review, RDF.type, RDFS.Class))

    Feedback = URIRef(f'{baseURI}/Feedback')
    graph.add((Feedback, RDF.type, RDFS.Class))

    Decision = URIRef(f'{baseURI}/Decision')
    graph.add((Decision, RDF.type, RDFS.Class))

    Year = URIRef(f'{baseURI}/Year')
    graph.add((Year, RDF.type, RDFS.Class))

    Chair = URIRef(f'{baseURI}/Chair')
    graph.add((Chair, RDF.type, RDFS.Class))

    Editor = URIRef(f'{baseURI}/Editor')
    graph.add((Editor, RDF.type, RDFS.Class))


    #Creating subclasses
    ShortPaper = URIRef(f'{baseURI}/ShortPaper')
    graph.add((ShortPaper, RDFS.subClassOf, Paper))

    FullPaper = URIRef(f'{baseURI}/FullPaper')
    graph.add((FullPaper, RDFS.subClassOf, Paper))

    DemoPaper = URIRef(f'{baseURI}/DemoPaper')
    graph.add((DemoPaper, RDFS.subClassOf, Paper))

    Poster = URIRef(f'{baseURI}/Poster')
    graph.add((Poster, RDFS.subClassOf, Paper))

    Journal = URIRef(f'{baseURI}/Journal')
    graph.add((Journal, RDFS.subClassOf, Venue))

    Conference = URIRef(f'{baseURI}/Conference')
    graph.add((Conference, RDFS.subClassOf, Venue))

    Workshop = URIRef(f'{baseURI}/Workshop')
    graph.add((Workshop, RDFS.subClassOf, Conference))

    Symposium = URIRef(f'{baseURI}/Symposium')
    graph.add((Symposium, RDFS.subClassOf, Conference))

    ExpertGroup = URIRef(f'{baseURI}/ExpertGroup')
    graph.add((ExpertGroup, RDFS.subClassOf, Conference))

    RegularConference = URIRef(f'{baseURI}/RegularConference')
    graph.add((RegularConference, RDFS.subClassOf, Conference))


    #Creating properties
    relatedTo = URIRef(f'{baseURI}/relatedTo')
    graph.add((relatedTo, RDFS.domain, Paper))
    graph.add((relatedTo, RDFS.range, SubjectArea))

    citedBy = URIRef(f'{baseURI}/citedBy')
    graph.add((citedBy, RDFS.domain, Paper))
    graph.add((citedBy, RDFS.range, Paper))

    submitted = URIRef(f'{baseURI}/submitted')
    graph.add((submitted, RDFS.domain, Paper))
    graph.add((submitted, RDFS.range, Submission))

    contains = URIRef(f'{baseURI}/contains')
    graph.add((contains, RDFS.domain, Paper))
    graph.add((contains, RDFS.range, Keyword))

    participatedIn = URIRef(f'{baseURI}/participatedIn')
    graph.add((participatedIn, RDFS.domain, Author))
    graph.add((participatedIn, RDFS.range, Paper))

    relatedTo = URIRef(f'{baseURI}/relatedTo')
    graph.add((relatedTo, RDFS.domain, Conference))
    graph.add((relatedTo, RDFS.range, SubjectArea))

    relatedTo = URIRef(f'{baseURI}/relatedTo')
    graph.add((relatedTo, RDFS.domain, Journal))
    graph.add((relatedTo, RDFS.range, SubjectArea))

    publishedIn = URIRef(f'{baseURI}/publishedIn')
    graph.add((publishedIn, RDFS.domain, Submission))
    graph.add((publishedIn, RDFS.range, Venue))

    reviewed = URIRef(f'{baseURI}/reviewed')
    graph.add((reviewed, RDFS.domain, Author))
    graph.add((reviewed, RDFS.range, Submission))

    affiliatedTo = URIRef(f'{baseURI}/relatedTo')
    graph.add((affiliatedTo, RDFS.domain, Author))
    graph.add((affiliatedTo, RDFS.range, Organization))

    partOf = URIRef(f'{baseURI}/partOf')
    graph.add((partOf, RDFS.domain, Submission))
    graph.add((partOf, RDFS.range, Review))

    commented = URIRef(f'{baseURI}/commented')
    graph.add((commented, RDFS.domain, Review))
    graph.add((commented, RDFS.range, Feedback))

    decided = URIRef(f'{baseURI}/decided')
    graph.add((decided, RDFS.domain, Review))
    graph.add((decided, RDFS.range, Decision))

    when = URIRef(f'{baseURI}/when')
    graph.add((when, RDFS.domain, Submission))
    graph.add((when, RDFS.range, Year))

    chairs = URIRef(f'{baseURI}/chairs')
    graph.add((chairs, RDFS.domain, Chair))
    graph.add((chairs, RDFS.range, Conference))

    edits = URIRef(f'{baseURI}/edits')
    graph.add((edits, RDFS.domain, Editor))
    graph.add((edits, RDFS.range, Journal))


def output_graph_to_turtle(graph_name, filename):
    """
    Function will export the graph to a ".ttl" file and store it in data/processed directory.

    :param graph_name: RDFlib graph containing relations
    :param filename: desired output filename
    :return: None
    """
    graph_name.serialize(destination=f'../data/processed/{filename}.ttl')


baseURI = "http://example.org"
graph = Graph()
create_TBOX()
output_graph_to_turtle(graph, "TBOX")





