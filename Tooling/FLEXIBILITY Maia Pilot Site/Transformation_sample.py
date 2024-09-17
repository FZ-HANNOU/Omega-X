import csv
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, XSD, TIME

# Define namespaces
ETS = Namespace("https://w3id.org/omega-x/Ontology/ets/")
PROP = Namespace("https://w3id.org/omega-x/Ontology/Property/")
MAIA = Namespace("https://w3id.org/omega-x/Maia/")
TIME = Namespace("http://www.w3.org/2006/time#")
EX = Namespace("http://example.org/")

# Create an RDF graph and bind the namespaces
g = Graph()
g.bind("ets", ETS)
g.bind("prop", PROP)
g.bind("maia", MAIA)
g.bind("time", TIME)
g.bind("xsd", XSD)

# Define URIs for the time series and property
time_series_uri = MAIA.TimeSeries
property_currL1 = PROP.CurrentL1

# Function to convert timestamp to ISO 8601 (adding 'T')
def to_iso_8601(timestamp):
    return timestamp.replace(" ", "T")

# Function to create RDF triples from CSV data
def csv_to_rdf(csv_file):
    incrementing_id = 1  # Initialize the counter for generating unique URIs

    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert the timestamp to ISO 8601 format for the collection time
            timestamp_iso = to_iso_8601(row['tstamp'])

            # Create a DataCollection URI using the incrementing integer
            data_collection_uri = URIRef(f"http://example.org/DataCollection/{incrementing_id}")

            # Add triples for the DataCollection
            g.add((data_collection_uri, RDF.type, ETS.DataCollection))
            g.add((data_collection_uri, ETS.collectionTime, Literal(timestamp_iso, datatype=XSD.dateTime)))
            g.add((data_collection_uri, ETS.isElementOf, time_series_uri))

            # Create a DataPoint URI using the incrementing integer
            data_point_uri = URIRef(f"http://example.org/DataPoint/CurrL1_A/{incrementing_id}")

            # Add triples for the DataPoint
            g.add((data_point_uri, RDF.type, ETS.DataPoint))
            g.add((data_point_uri, ETS.dataValue, Literal(float(row['CurrL1_A']), datatype=XSD.float)))
            g.add((data_point_uri, ETS.belongsTo, data_collection_uri))
            g.add((data_point_uri, ETS.hasProperty, property_currL1))

            # Increment the counter for the next row
            incrementing_id += 1

csv_file_path = "C:/Users/g28683/Documents/Omega-X/Omegax for w3id/Omega-X/Tooling/FLEXIBILITY Maia Pilot Site/TorreLidador.csv"

csv_to_rdf(csv_file_path)


rdf_output = g.serialize(format="turtle")
print(rdf_output)


with open("TorreLidador_sample.ttl", "w") as f:
    f.write(rdf_output)
