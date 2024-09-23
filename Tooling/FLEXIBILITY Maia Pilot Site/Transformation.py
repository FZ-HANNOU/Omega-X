import csv
from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, XSD


ETS = Namespace("https://w3id.org/omega-x/EventTimeSeriesOntology/")
PROP = Namespace("https://w3id.org/omega-x/PropertyOntology/")
MAIA = Namespace("https://w3id.org/omega-x/MaiaPTT/")
EDS = Namespace("https://w3id.org/omega-x/EnergyDataset/")
EX = Namespace("http://example.org/")


g = Graph()
g.bind("ets", ETS)
g.bind("prop", PROP)
g.bind("maia", MAIA)
g.bind("eds", EDS)
g.bind("xsd", XSD)


time_series_uri = URIRef("https://w3id.org/omega-x/MaiaPTT/TorreLidadorTimeSeries")


g.add((time_series_uri, RDF.type, ETS.TimeSeries))
g.add((time_series_uri, RDF.type, EDS.EnergyDataset))
g.add((time_series_uri, ETS.hasStep, Literal(10, datatype=XSD.float)))

property_mapping = {
    "CurrL1_A": PROP.CurrentL1,
    "CurrL2_A": PROP.CurrentL2,
    "CurrL3_A": PROP.CurrentL3,
    "ActPow_kW": PROP.ActivePower,
    "AppPow_kVA": PROP.ApparentPower,
    "ReacPow_kvar": PROP.ReactivePower,
    "Energy_kWh": PROP.Energy,
    "VolL1_V": PROP.VoltageL1,
    "VolL2_V": PROP.VoltageL2,
    "VolL3_V": PROP.VoltageL3,
    "THDUL1": PROP.TotalHarmonicDistorsionUL1,
    "THDUL2": PROP.TotalHarmonicDistorsionUL2,
    "THDUL3": PROP.TotalHarmonicDistorsionUL3,
    "THDIL1": PROP.TotalHarmonicDistorsionIL1,
    "THDIL2": PROP.TotalHarmonicDistorsionIL2,
    "THDIL3": PROP.TotalHarmonicDistorsionIL3,
    "cosphi": PROP.CosinusPhi
}


def to_iso_8601(timestamp):
    return timestamp.replace(" ", "T")


def csv_to_rdf(csv_file):
    incrementing_id = 1 

    with open(csv_file, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            timestamp_iso = to_iso_8601(row['tstamp'])

            data_collection_uri = URIRef(f"https://w3id.org/omega-x/MaiaPTT/DataCollection/{incrementing_id}")

            g.add((data_collection_uri, RDF.type, ETS.DataCollection))
            g.add((data_collection_uri, ETS.collectionTime, Literal(timestamp_iso, datatype=XSD.dateTime)))
            g.add((data_collection_uri, ETS.isElementOf, time_series_uri))

            for column, property_uri in property_mapping.items():
                if column in row and row[column]:
                    data_point_uri = URIRef(f"https://w3id.org/omega-x/MaiaPTT/DataPoint/{column}/{incrementing_id}")

                    g.add((data_point_uri, RDF.type, ETS.DataPoint))
                    g.add((data_point_uri, ETS.dataValue, Literal(float(row[column]), datatype=XSD.float)))
                    g.add((data_point_uri, ETS.belongsTo, data_collection_uri))
                    g.add((data_point_uri, ETS.hasProperty, property_uri))

            incrementing_id += 1


csv_file_path = "C:/Users/g28683/Documents/Omega-X/Omegax for w3id/Omega-X/Tooling/FLEXIBILITY Maia Pilot Site/TorreLidador.csv" 

csv_to_rdf(csv_file_path)

rdf_output = g.serialize(format="json-ld")
print(rdf_output)

with open("TorreLidador_example.json", "w") as f:
    f.write(rdf_output)
