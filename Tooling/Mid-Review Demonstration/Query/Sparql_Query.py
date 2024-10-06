from  rdflib import Graph, BNode, URIRef, Literal, XSD, Namespace

#decalre the graph
g1 = Graph()
g2 = Graph()

#Open the graph from an existing file
g1.parse("Tooling/Mid-Review Demonstration/Knowledge Graph/energyToyExample.ttl", format="turtle")
g2.parse("Tooling/Mid-Review Demonstration/Knowledge Graph/meteoToyExample.ttl", format="turtle")
g = g1 + g2

#Open the query to execute
with open("Tooling/Mid-Review Demonstration/Query/Q1.rq", "r") as file:
    query = file.read()
#execute the query
results = g.query(query)

#store the results inoutput graph
output_graph = Graph()
output_graph.bind("demo", Namespace("https://w3id.org/omega-x/demo/"))

for row in results:
    subject = BNode()
    time, energyValue, temperatureValue, irradianceValue = row
    output_graph.add((subject, URIRef("https://w3id.org/omega-x/demo/time"), Literal(time, datatype=XSD.dateTime)))
    output_graph.add((subject, URIRef("https://w3id.org/omega-x/demo/energyValue"), Literal(energyValue)))
    output_graph.add((subject, URIRef("https://w3id.org/omega-x/demo/temperatureValue"), Literal(temperatureValue)))
    output_graph.add((subject, URIRef("https://w3id.org/omega-x/demo/irradianceValue"), Literal(irradianceValue)))


output_graph.serialize(destination="Tooling/Mid-Review Demonstration/Query/output_graph.ttl", format="turtle")