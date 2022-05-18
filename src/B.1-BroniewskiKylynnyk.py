# TBOX definition
from rdflib import Graph
from rdflib.namespace import RDFS, RDF
from rdflib import Namespace
from rdflib import URIRef, Literal

# TODO: complete TBOX creation with all properties from lab scope


# TODO: create graph using existing turtle doc
def create_TBOX(graph, list_of_classes):
    for item in list_of_classes:
        new_class = URIRef(f'http://example.org/{item}')
        graph.add((new_class, RDF.type, RDFS.Class))


def output_graph_to_turtle(graph, filename):
    graph.serialize(destination=f'../data/processed/{filename}.ttl')


classes_to_create = ["Paper", "SubjectArea"]
g = Graph()
create_TBOX(g, classes_to_create)


