from pyshacl import validate
import rdflib


data_graph = rdflib.Graph()
with open("index.ttl", "r") as file:
    data_graph.parse(file=file, format="turtle")

shapes_graph = rdflib.Graph()
with open("PowerUnit.shacl", "r") as file:
    shapes_graph.parse(file=file, format="turtle")


conforms, results_graph, results = validate(
    data_graph, shacl_graph=shapes_graph,
    data_graph_format='turtle', shacl_graph_format='turtle'
)

if conforms:
    print("Data are conform!")
else:
    print("Data are not conform to the shapes.")
    print(results)
    
    turtle_results = results_graph.serialize(format="turtle")
    
    with open("./Output/Validation_report.ttl", "w") as f:
        f.write(turtle_results)
