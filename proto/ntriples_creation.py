import rdflib
import csv

# Create an RDF graph
g = rdflib.Graph()
g.bind("ex", rdflib.Namespace("http://example.org/"))

# open the csv file
data = csv.reader(open("data.csv", "r"), delimiter=";")

for row in data:
    # Create a new triple
    s = rdflib.URIRef("http://example.org/" + row[0])
    p = rdflib.URIRef("http://example.org/" + row[1])
    o = rdflib.URIRef("http://example.org/" + row[2])
    g.add((s, p, o))

# Serialize the graph to an N-Triples file
g.serialize(destination="data.nt", format="nt")
