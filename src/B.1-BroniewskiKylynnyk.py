# TBOX definition
from rdflib import Graph
from rdflib.namespace import RDFS, RDF, XSD
from rdflib import Namespace
from rdflib import Literal


def create_TBOX():
    """
    Creates all classes, subclasses and properties through domain and range definitions.
    Each class must be created explicitly regardless of RDFS inference rules due to limitations
    in RDFlib capabilities.
    :return: None
    """
    # Namespace means that we can just use "KG" as an "alias" for the URI
    KG = Namespace("http://KG-SDM-Lab3.org/")
    # binding is what adds the @prefix to the turtle file to make it easier to read in the output.
    graph.bind("kg", KG)

    # Creating superclasses
    graph.add((KG.Paper, RDF.type, RDFS.Class))
    graph.add((KG.Paper, RDFS.label, Literal("Paper")))
    graph.add((KG.Paper, RDFS.comment, Literal("To know if a paper is published or not, complete a query on the "
                                               "Decision of a paper. If Decision is True, the paper is published.")))

    graph.add((KG.SubjectArea, RDF.type, RDFS.Class))
    graph.add((KG.SubjectArea, RDFS.label, Literal("SubjectArea")))

    graph.add((KG.Submission, RDF.type, RDFS.Class))
    graph.add((KG.Submission, RDFS.label, Literal("Submission")))

    graph.add((KG.Venue, RDF.type, RDFS.Class))
    graph.add((KG.Venue, RDFS.label, Literal("Venue")))

    graph.add((KG.Author, RDF.type, RDFS.Class))
    graph.add((KG.Author, RDFS.label, Literal("Author")))

    graph.add((KG.Reviewer, RDF.type, RDFS.Class))
    graph.add((KG.Reviewer, RDFS.label, Literal("Reviewer")))

    graph.add((KG.Chair, RDF.type, RDFS.Class))
    graph.add((KG.Chair, RDFS.label, Literal("Chair")))

    graph.add((KG.Editor, RDF.type, RDFS.Class))
    graph.add((KG.Editor, RDFS.label, Literal("Editor")))

    graph.add((KG.Proceeding, RDF.type, RDFS.Class))
    graph.add((KG.Proceeding, RDFS.label, Literal("Proceeding")))

    graph.add((KG.Volume, RDF.type, RDFS.Class))
    graph.add((KG.Volume, RDFS.label, Literal("Volume")))

    #Creating subclasses
    graph.add((KG.ShortPaper, RDFS.subClassOf, KG.Paper))
    graph.add((KG.ShortPaper, RDFS.label, Literal("ShortPaper")))

    graph.add((KG.FullPaper, RDFS.subClassOf, KG.Paper))
    graph.add((KG.FullPaper, RDFS.label, Literal("FullPaper")))

    graph.add((KG.DemoPaper, RDFS.subClassOf, KG.Paper))
    graph.add((KG.DemoPaper, RDFS.label, Literal("DemoPaper")))

    graph.add((KG.Poster, RDFS.subClassOf, KG.Paper))
    graph.add((KG.Poster, RDFS.label, Literal("Poster")))

    graph.add((KG.Journal, RDFS.subClassOf, KG.Venue))
    graph.add((KG.Journal, RDFS.label, Literal("Journal")))

    graph.add((KG.Conference, RDFS.subClassOf, KG.Venue))
    graph.add((KG.Conference, RDFS.label, Literal("Conference")))

    graph.add((KG.Workshop, RDFS.subClassOf, KG.Conference))
    graph.add((KG.Workshop, RDFS.label, Literal("Workshop")))

    graph.add((KG.Symposium, RDFS.subClassOf, KG.Conference))
    graph.add((KG.Symposium, RDFS.label, Literal("Symposium")))

    graph.add((KG.ExpertGroup, RDFS.subClassOf, KG.Conference))
    graph.add((KG.ExpertGroup, RDFS.label, Literal("ExpertGroup")))

    graph.add((KG.RegularConference, RDFS.subClassOf, KG.Conference))
    graph.add((KG.RegularConference, RDFS.label, Literal("RegularConference")))


    #Creating properties
    #TODO: Should the "duplicate" properties be sub-properties instead? Because of the queries we are doing,
    # there does not look to be value in doing this.
    graph.add((KG.relatedTo, RDFS.domain, KG.Paper))
    graph.add((KG.relatedTo, RDFS.domain, KG.Conference))
    graph.add((KG.relatedTo, RDFS.domain, KG.Journal))
    graph.add((KG.relatedTo, RDFS.range, KG.SubjectArea))
    graph.add((KG.relatedTo, RDFS.label, Literal("relatedTo")))

    graph.add((KG.title, RDFS.domain, KG.Paper))
    graph.add((KG.title, RDFS.domain, KG.Journal))
    graph.add((KG.title, RDFS.domain, KG.Conference))

    graph.add((KG.title, RDF.type, RDF.Property))
    graph.add((KG.title, RDFS.label, Literal("title")))
    graph.add((KG.title, RDFS.range, XSD.string))

    graph.add((KG.submitted, RDFS.domain, KG.Paper))
    graph.add((KG.submitted, RDFS.range, KG.Submission))
    graph.add((KG.submitted, RDFS.label, Literal("submitted")))

    graph.add((KG.contains, RDFS.domain, KG.Paper))
    graph.add((KG.contains, RDFS.range, KG.Keyword))
    graph.add((KG.contains, RDFS.label, Literal("contains")))

    graph.add((KG.participatedIn, RDFS.domain, KG.Author))
    graph.add((KG.participatedIn, RDFS.range, KG.Paper))
    graph.add((KG.participatedIn, RDFS.label, Literal("participatedIn")))

    #TODO: If I have a repeating property like this, does it suggest I should have a super classe (Person?). Should I
    # be setting the domain for name like this at the schematic level, or should this be done when instantiating?
    graph.add((KG.name, RDFS.domain, KG.Author))
    graph.add((KG.name, RDFS.domain, KG.Reviewer))
    graph.add((KG.name, RDFS.domain, KG.Editor))
    graph.add((KG.name, RDFS.domain, KG.Chair))

    graph.add((KG.name, RDF.type, RDF.Property))
    graph.add((KG.name, RDFS.label, Literal("name")))
    graph.add((KG.name, RDFS.range, XSD.string))

    graph.add((KG.publishedIn, RDFS.domain, KG.Submission))
    graph.add((KG.publishedIn, RDFS.range, KG.Venue))
    graph.add((KG.publishedIn, RDFS.label, Literal("publishedIn")))

    graph.add((KG.published, RDFS.domain, KG.Conference))
    graph.add((KG.published, RDFS.range, KG.Proceeding))
    graph.add((KG.published, RDFS.domain, KG.Journal))
    graph.add((KG.published, RDFS.range, KG.Volume))
    graph.add((KG.published, RDFS.label, Literal("published")))

    graph.add((KG.handledBy, RDFS.domain, KG.Conference))
    graph.add((KG.handledBy, RDFS.range, KG.Chair))
    graph.add((KG.handledBy, RDFS.domain, KG.Journal))
    graph.add((KG.handledBy, RDFS.range, KG.Editor))
    graph.add((KG.handledBy, RDFS.label, Literal("handledBy")))

    graph.add((KG.assigned, RDFS.domain, KG.Editor))
    graph.add((KG.assigned, RDFS.domain, KG.Chair))
    graph.add((KG.assigned, RDFS.range, KG.Reviewer))
    graph.add((KG.assigned, RDFS.label, Literal("assigned")))
    graph.add((KG.assigned, RDFS.comment, Literal("Each class assigning a reviewer should assign at least 2 "
                                                  "reviewers")))

    graph.add((KG.reviewed, RDFS.domain, KG.Reviewer))
    graph.add((KG.reviewed, RDFS.range, KG.Submission))
    graph.add((KG.reviewed, RDFS.label, Literal("reviewed")))

    graph.add((KG.affiliatedTo, RDFS.domain, KG.Author))
    graph.add((KG.affiliatedTo, RDFS.range, KG.Organization))
    graph.add((KG.affiliatedTo, RDFS.label, Literal("affiliatedTo")))

    graph.add((KG.partOf, RDFS.domain, KG.Submission))
    graph.add((KG.partOf, RDFS.range, KG.Review))
    graph.add((KG.partOf, RDFS.label, Literal("partOf")))

    graph.add((KG.commented, RDFS.domain, KG.Review))
    graph.add((KG.commented, RDFS.range, XSD.string))
    graph.add((KG.commented, RDFS.label, Literal("commented")))
    graph.add((KG.commented, RDFS.comment, Literal("The string provides all the commentary available as part of the "
                                                   "review")))

    graph.add((KG.decided, RDFS.domain, KG.Review))
    graph.add((KG.decided, RDFS.range, XSD.boolean))
    graph.add((KG.decided, RDFS.label, Literal("decided")))
    graph.add((KG.decided, RDFS.comment, Literal("The decision is a boolean where True means the paper is accepted "
                                                 "and False means the paper is rejected" )))

    graph.add((KG.chairs, RDFS.domain, KG.Chair))
    graph.add((KG.chairs, RDFS.range, KG.Conference))
    graph.add((KG.chairs, RDFS.label, Literal("chairs")))

    graph.add((KG.edits, RDFS.domain, KG.Editor))
    graph.add((KG.edits, RDFS.range, KG.Journal))
    graph.add((KG.edits, RDFS.label, Literal("edits")))


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






