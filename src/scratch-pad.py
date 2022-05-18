
from rdflib import Graph
from rdflib.namespace import RDFS, RDF
from rdflib import Namespace
from rdflib import URIRef, Literal

# TODO: complete TBOX creation with all properties from lab scope


# TODO: create graph using existing turtle doc
def create_TBOX():
    """

    :return: returns a TBOX graph with schema created
    """
    g = Graph()
    Paper = URIRef("http://example.org/Paper")

    g.add((Paper, RDF.type, RDFS.Class))
    g.serialize(destination="../data/processed/tbl.ttl")

create_TBOX()

# TODO: create script to reformat existing CSV files into turtle format, export to turtle doc

# TODO: complete ABOX creation so that files can be imported to GraphDB

# TODO: create code that links ABOX and TBOX

# TODO: import turtle doc (ABOX and TBOX) into graphDB

# TODO: complete queries

# TODO: write SPARQL queries
# 1. Find all Authors.
# 2. Find all properties whose domain is Author.
# 3. Find all properties whose domain is either Conference or Journal.
# 4. Find all the papers written by a given author that where published in database confer- ences.
