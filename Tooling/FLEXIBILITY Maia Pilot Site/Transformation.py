import csv
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, XSD


ETS = Namespace("https://w3id.org/omega-x/EventTimeSeriesOntology/")
PROP = Namespace("https://w3id.org/omega-x/PropertyOntology/")
MAIA = Namespace("https://w3id.org/omega-x/MaiaPTT/")
EX = Namespace("http://example.org/")

g = Graph()
g.bind("ets", ETS)
g.bind("prop", PROP)
g.bind("maia", MAIA)
g.bind("xsd", XSD)

time_series_uri = MAIA.TimeSeries

property_mapping = {
    "CurrL1_A": PROP.CurrentL1,
    "CurrL2_A": PROP.CurrentL2,
    "CurrL3_A": PROP.CurrentL3,
    "ActPow_kW": PROP.ActivePower,
    "AppPow_kVA": PROP.ApparentPower,
    "ReacPow_kvar": PROP.ReactivePower,
    "Energy_kWh": PROP.Energy,
    "VolL1_V": PROP.Voltage1,
    "VolL2_V": PROP.Voltage2,
    "VolL3_V": PROP.Voltage3,
    "THDUL1": PROP.THDUL1,
    "THDUL2": PROP.THDUL2,
    "THDUL3": PROP.THDUL3,
    "THDIL1": PROP.THDIL1,
    "THDIL2": PROP.THDIL2,
    "THDIL3": PROP.THDIL3,
    "cosphi": PROP.Cosphi
}

def to_iso_8601(timestamp):
    return timestamp.replace(" ", "T")

def csv_to_rdf(csv_file):
    incrementing_id = 1  

    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            timestamp_iso = to_iso_8601(row['tstamp'])

            data_collection_uri = URIRef(f"http://example.org/DataCollection/{incrementing_id}")

           
            g.add((data_collection_uri, RDF.type, ETS.DataCollection))
            g.add((data_collection_uri, ETS.collectionTime, Literal(timestamp_iso, datatype=XSD.dateTime)))
            g.add((data_collection_uri, ETS.isElementOf, time_series_uri))

        
            for column, property_uri in property_mapping.items():
                if column in row and row[column]:
                    data_point_uri = URIRef(f"http://example.org/DataPoint/{column}/{incrementing_id}")

                    g.add((data_point_uri, RDF.type, ETS.DataPoint))
                    g.add((data_point_uri, ETS.dataValue, Literal(float(row[column]), datatype=XSD.float)))
                    g.add((data_point_uri, ETS.belongsTo, data_collection_uri))
                    g.add((data_point_uri, ETS.hasProperty, property_uri))

            
            incrementing_id += 1

csv_file_path = "C:/Users/g28683/Documents/Omega-X/Omegax for w3id/Omega-X/Tooling/FLEXIBILITY Maia Pilot Site/TorreLidador_Full.csv"

csv_to_rdf(csv_file_path)

rdf_output = g.serialize(format="turtle")
print(rdf_output)

with open("TorreLidador_Full.ttl", "w") as f:
    f.write(rdf_output)
