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

    #################################################################
    #    Papers
    #################################################################

    graph.add((KG.Paper, RDF.type, RDFS.Class))
    graph.add((KG.Paper, RDFS.label, Literal("Paper")))
    graph.add((KG.Paper, RDFS.comment, Literal("To know if a paper is published or not, complete a query on the "
                                               "Decision of a paper. If Decision is True, the paper is published.")))

    # Creating subclasses of Paper - different types of Papers
    graph.add((KG.ShortPaper, RDFS.subClassOf, KG.Paper))
    graph.add((KG.ShortPaper, RDFS.label, Literal("ShortPaper")))

    graph.add((KG.FullPaper, RDFS.subClassOf, KG.Paper))
    graph.add((KG.FullPaper, RDFS.label, Literal("FullPaper")))

    graph.add((KG.DemoPaper, RDFS.subClassOf, KG.Paper))
    graph.add((KG.DemoPaper, RDFS.label, Literal("DemoPaper")))

    graph.add((KG.Poster, RDFS.subClassOf, KG.Paper))
    graph.add((KG.Poster, RDFS.label, Literal("Poster")))

    # Submission class is a named node that ties multiple things together
    graph.add((KG.Submission, RDF.type, RDFS.Class))
    graph.add((KG.Submission, RDFS.label, Literal("Submission")))

    graph.add((KG.submitted, RDFS.domain, KG.Paper))
    graph.add((KG.submitted, RDFS.range, KG.Submission))
    graph.add((KG.submitted, RDFS.label, Literal("submitted")))

    graph.add((KG.publishedIn, RDFS.domain, KG.Submission))
    graph.add((KG.publishedIn, RDFS.range, KG.Venue))
    graph.add((KG.publishedIn, RDFS.label, Literal("publishedIn")))


    #################################################################
    #    Venues
    #################################################################

    graph.add((KG.Venue, RDF.type, RDFS.Class))
    graph.add((KG.Venue, RDFS.label, Literal("Venue")))

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

    graph.add((KG.chairedBy, RDFS.domain, KG.Conference))
    graph.add((KG.chairedBy, RDFS.range, KG.Chair))
    graph.add((KG.chairedBy, RDFS.label, Literal("chairedBy")))

    graph.add((KG.editedBy, RDFS.domain, KG.Journal))
    graph.add((KG.editedBy, RDFS.range, KG.Editor))
    graph.add((KG.editedBy, RDFS.label, Literal("editedBy")))

    #################################################################
    #    People
    #################################################################

    graph.add((KG.Person, RDF.type, RDFS.Class))
    graph.add((KG.Person, RDFS.label, Literal("Person")))

    graph.add((KG.Author, RDFS.subClassOf, KG.Person))
    graph.add((KG.Author, RDFS.label, Literal("Author")))

    graph.add((KG.participatedIn, RDFS.domain, KG.Author))
    graph.add((KG.participatedIn, RDFS.range, KG.Paper))
    graph.add((KG.participatedIn, RDFS.label, Literal("participatedIn")))

    graph.add((KG.Reviewer, RDFS.subClassOf, KG.Person))
    graph.add((KG.Reviewer, RDFS.label, Literal("Reviewer")))

    # Create Leader superclass to remove redundancy in assigning reviewer property. It also makes it possible to query
    # and all the editors and chairs together.
    graph.add((KG.Leader, RDFS.subClassOf, KG.Person))
    graph.add((KG.Leader, RDFS.label, Literal("Leader")))

    graph.add((KG.Chair, RDFS.subClassOf, KG.Leader))
    graph.add((KG.Chair, RDFS.label, Literal("Chair")))

    graph.add((KG.Editor, RDFS.subClassOf, KG.Leader))
    graph.add((KG.Editor, RDFS.label, Literal("Editor")))

    graph.add((KG.chairs, RDFS.domain, KG.Chair))
    graph.add((KG.chairs, RDFS.range, KG.Conference))
    graph.add((KG.chairs, RDFS.label, Literal("chairs")))

    graph.add((KG.edits, RDFS.domain, KG.Editor))
    graph.add((KG.edits, RDFS.range, KG.Journal))
    graph.add((KG.edits, RDFS.label, Literal("edits")))

    # We made all the different types of people a subClassOf :Person so that we could associate the property :name
    # with only a single class instead of repeating it like we did with the SubjectArea
    graph.add((KG.name, RDF.type, RDF.Property))
    graph.add((KG.name, RDFS.domain, KG.Person))
    graph.add((KG.name, RDFS.range, XSD.string))
    graph.add((KG.name, RDFS.label, Literal("name")))
    graph.add((KG.name, RDFS.comment, Literal("The name of any person.")))


    #################################################################
    #    Publications
    #################################################################

    # Create a super class of Collection to simplify connections between a Venue and its publications. All Venues
    # will have some publication.
    graph.add((KG.Collection, RDF.type, RDFS.Class))
    graph.add((KG.Collection, RDFS.label, Literal("Collection")))

    graph.add((KG.published, RDFS.domain, KG.Venue))
    graph.add((KG.published, RDFS.range, KG.Collection))
    graph.add((KG.published, RDFS.label, Literal("published")))

    graph.add((KG.Proceeding, RDFS.subClassOf, KG.Collection))
    graph.add((KG.Proceeding, RDFS.label, Literal("Proceeding")))

    graph.add((KG.Volume, RDFS.subClassOf, KG.Collection))
    graph.add((KG.Volume, RDFS.label, Literal("Volume")))


    #################################################################
    #    Subject Area
    #################################################################

    graph.add((KG.SubjectArea, RDF.type, RDFS.Class))
    graph.add((KG.SubjectArea, RDFS.label, Literal("SubjectArea")))

    graph.add((KG.relatedTo, RDFS.range, KG.SubjectArea))
    graph.add((KG.relatedTo, RDFS.label, Literal("related to")))

    # Here we create properties that are all subProperties of relatedTo to make it possible to query all items related
    # to a certain topic, or query items from Paper, or collections independently.
    graph.add((KG.paperRelatedTo, RDF.type, RDF.Property))
    graph.add((KG.paperRelatedTo, RDFS.domain, KG.Paper))
    graph.add((KG.paperRelatedTo, RDFS.range, KG.SubjectArea))
    graph.add((KG.paperRelatedTo, RDFS.subPropertyOf, KG.relatedTo))
    graph.add((KG.paperRelatedTo, RDFS.label, Literal("Paper related to")))

    graph.add((KG.collectionRelatedTo, RDF.type, RDF.Property))
    graph.add((KG.collectionRelatedTo, RDFS.domain, KG.Collection))
    graph.add((KG.collectionRelatedTo, RDFS.range, KG.SubjectArea))
    graph.add((KG.collectionRelatedTo, RDFS.subPropertyOf, KG.relatedTo))
    graph.add((KG.collectionRelatedTo, RDFS.label, Literal("Collection related to")))

    graph.add((KG.title, RDF.type, RDF.Property))
    graph.add((KG.title, RDFS.label, Literal("title")))
    graph.add((KG.title, RDFS.comment, Literal("The title of any entity")))
    graph.add((KG.title, RDFS.range, XSD.string))

    # TODO: Potentially remove these subPropertyOf titles and just use KG.title for everything
    #   all title are sub-properties of KG:title, allowing for flexible querying.
    graph.add((KG.paperTitle, RDF.type, RDF.Property))
    graph.add((KG.paperTitle, RDFS.domain, KG.Paper))
    graph.add((KG.paperTitle, RDFS.range, XSD.string))
    graph.add((KG.paperTitle, RDFS.subPropertyOf, KG.title))
    graph.add((KG.paperTitle, RDFS.label, Literal("title of a Paper")))

    graph.add((KG.journalTitle, RDF.type, RDF.Property))
    graph.add((KG.journalTitle, RDFS.domain, KG.Journal))
    graph.add((KG.journalTitle, RDFS.range, XSD.string))
    graph.add((KG.journalTitle, RDFS.subPropertyOf, KG.title))
    graph.add((KG.journalTitle, RDFS.label, Literal("title of a Journal")))

    graph.add((KG.conferenceTitle, RDF.type, RDF.Property))
    graph.add((KG.conferenceTitle, RDFS.domain, KG.Conference))
    graph.add((KG.conferenceTitle, RDFS.range, XSD.string))
    graph.add((KG.conferenceTitle, RDFS.subPropertyOf, KG.title))
    graph.add((KG.conferenceTitle, RDFS.label, Literal("title of a Conference")))


    #################################################################
    #    Reviews
    #################################################################

    # Remember that the Leader class is a superclass of chair and editor
    graph.add((KG.assigned, RDFS.domain, KG.Leader))
    graph.add((KG.assigned, RDFS.range, KG.Reviewer))
    graph.add((KG.assigned, RDFS.label, Literal("assigned")))
    graph.add((KG.assigned, RDFS.comment, Literal("Each class assigning a reviewer should assign at least 2 "
                                                  "reviewers")))

    graph.add((KG.reviewed, RDFS.domain, KG.Reviewer))
    graph.add((KG.reviewed, RDFS.range, KG.Submission))
    graph.add((KG.reviewed, RDFS.label, Literal("reviewed")))

    graph.add((KG.commented, RDFS.domain, KG.Reviewer))
    graph.add((KG.commented, RDFS.range, XSD.string))
    graph.add((KG.commented, RDFS.label, Literal("commented")))
    graph.add((KG.commented, RDFS.comment, Literal("The string provides all the commentary available as part of the "
                                                   "review")))

    graph.add((KG.decided, RDFS.domain, KG.Reviewer))
    graph.add((KG.decided, RDFS.range, XSD.boolean))
    graph.add((KG.decided, RDFS.label, Literal("decided")))
    graph.add((KG.decided, RDFS.comment, Literal("The decision is a boolean where True means the paper is accepted "
                                                 "and False means the paper is rejected" )))


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
