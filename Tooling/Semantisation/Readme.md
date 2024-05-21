
# Dataset Semantisation
Dataset semantisation aims to create knowledge graphs from raw data. This operation is also called rdfization. The transformation into knowledge graphs is led by an ontology that enables to capture the schema of the ouput result. 

Many approaches exist to enable data semantisation. For example, a declarative approach enables to specify how data in source schemas should be mapped to target RDF graph, conforming to a semantic model (ontology). RDF Mapping Language is a generic mapping language extending R2RML, a W3C specification. RML enables expressing mapping rules from heterogenous data structures to RDF graphs. 

## The SDM RDFIZER Tool
Multiple tools are available to use RML mappings for semantisation. In the Omega-X project, we use the SDM RDFIZER tool, [SDM RDFIZER](https://github.com/SDM-TIB/SDM-RDFizer/tree/master/rdfizer). 