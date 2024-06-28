# Flexibility Ontology

## Description
The flexibility ontology is a use case family ontology describing the flexibility family on three dimensions :
- Flexibility Operations, describes flexbility offer, request and order and their subsequent data. 
- Flexibility Infrastructure, describes infrastructure elements involved in the flexiblity use cases. This extends to the grid topology, building equipements, and imports specific electromobility and renewable infrastructures defined in their respective modules. 

## Competency Questions

### Querying Questions
| ID | Question in natural language | Example
|---|---|---|
| cq-1 | What price has been fixed in the flexibility order ? | The price is either a data point or a time series element of the time series describing the flexibility operation (order in this case)|
| cq-2 | What is the type of the flexibility offer ? | Capacity or flexibility are the properies assicated to the flexbility operation (offer in this case) |
| cq-3 | To which electricity phase is this appartment connected ? | Electricity phase can be L1.|
| cq-4 | What is the grid component providing this energy data ? | |
| cq-5 | What types of equipements are in the building ? | Equipements can be home appliances, such as HVAC, lighting system,... or other such as lifts,.. |

## Glossary
### Omega-X FLEX

![Diagram](./Flexibility.png)

## Recommendations
- The flexibility ontology covers both operations, services providing them and infrastructure components. 
- The flexbility ontology imports different UCs infrastructures such as those of electromobility (to consider charging stations), renewables (for renewable energy production among prosumres) and local energy communities. Carrefuly consider reviewing them. 

## Related Work 
### IEC 62746
- Grid component 
- Grid operations
- Smart Meter

### Interconnect Ontology
- Flexibility Request 
- Flexibility Offer
- Flexibility Instruction 
- Flexibility Profile

### Saref4BLDG
- Building 
- Building Device
- Building Space







