# Infrastructure Ontology

## Description
### Purpose
In energy domain, a simplified infrastructure topology of the system should be described in order to deliver intelligent services. The infrastructure topology facilitates the description of an infrastructure in a flexible way by allowing to describe the infrastructure’s components and its relations. 
### Scope
Infrastructure ontology provides OWL classes and properties to allow infrastructure of an energy system to be described.
### Description
This Infrastructure Ontology helps to define the infrastructure system of OMEGA-X use cases. The main class is the system which can be a physical system, a virtual system, an equipment or a site.
A system can be a System of interest that represents specific systems within the infrastructure, or a system kind that provides a taxonomy for the categorization of infrastructure equipment and sites.
The system of interest has a system kind and a system configuration encompassing different properties, in general defined from the data sheet or from an initial configuration of the system. New module can be created to define the infrastructure of a specific use case family. This new module should be aligned with the general infrastructure ontology.

## Competency Questions

### Querying Questions
| ID | Question in natural language | Example
|---|---|---|
| cq-1 |What is the identifier of specific system? | the id of a specific system |
| cq-2 |What is the system connected to a specific system? | A weather station  is connected to meter  |
| cq-3 |What is the location of a specific site? | the  geolocation of a solar plant|
| cq-4 |What is the system configuratin of a specific equipment? | the configuration  of a specific battery includig the nominal charge voltage|
| cq-5 |What are the systems of a specific system kind, e.g pv plants? |the systems of interest that have a system kinf pv plants|

### Inference Questions
| ID | Question in natural language | Example
|---|---|---|
| iq-1 | What are the systems connected to another system?| the list of systems connected via connected to target and connected to source relations|
| iq-2 | What are the systems having a specific system configuration?| the list of batteries having the same configuration|

## Glossary
### OMEGA-X Infrastructure
* [**infra:_System_**](https://w3id.org/omega-x/InfrastructureOntology/System/)
A system is an abstract class that can be a system of interest or a system kind. A system can consist f another system and can be connected to another system. 
* [**infra:_SystemOfInterest_**](https://w3id.org/omega-x/InfrastructureOntology/SystemOfInterest/)
A system of intrest represents specific systems within the infrastructure. If an exchanges dataset is attached to the system of interest, it will be considered as an evaluation point.
* [**infra:_SystemKind_**](https://w3id.org/omega-x/InfrastructureOntology/SystemKind/)
The system kind class provides a taxonomy for the categorization of infrastructure equipment and sites, enabling better organization and classification of components within the infrastructure. A system kind may be an equipment, a site, or any other physical or virtual system. A system kind that is neither an equipment nor a site may be, for instance, an electric grid or a data analytics service available on a Dataspace.
* [**infra:Equipment**](https://w3id.org/omega-x/InfrastructureOntology/Equipment/)
An equipement is a physical system kind which is part of the infrastructure.An equipment may be, for instance, an inverter or an electric vehicle charging station.
* [**infra:Site**](https://w3id.org/omega-x/InfrastructureOntology/Site/)
A site is a part of the physical world or a virtual world that is inherently both located in this world and having a 3D spatial extent. It can include more than one equipment. A site may be, for instance, a solar plant or an electric vehicle charging station pool.
* [**infra:SystemConfiguration**](https://w3id.org/omega-x/InfrastructureOntology/SystemConfiguration/)
A system configuration is a set of properties characterizing its structure and behavior. In case of an equipment, it may reflect its datasheet.
## OWL Description
![Diagram](./InfraModule-v1.1.png)
# Recommendations
- A `infra:SystemOfInterest` can be an `eds:EvaluationPoint` (see [_EvaluationPoint_](../Energy Data Set Ontology) once an energy data set is attached to it. 
- The static attributes of an `infra:SystemOfInterest` can be defined in `infra:SystemConfiguration`. 
- A `infra:SystemOfInterest` can have a location. 
- A `infra:System` can consist of an another  `infra:System` or many  `infra:System`.
- A An `infra:System` can be connected to another An `infra:System`. To precise the direction of the connection the object properties `infra:isConnectedTo` and An `infra:isConnectedFrom`
- For each specific use case family, a detailed infrastructure is defined to create the taxonomy of sites, equipements and static attributes, in addition to the relations between different systems.

## Related Work
### SEAS
* [**_seas:System_**]( https://w3id.org/seas/System): The class of systems, i.e., systems virtually isolated from the environment, whose behaviour and interactions with the environment are modeled.

* [**_seas:connectedTo_**]( https://w3id.org/seas/connectedTo): Links a system to a system it is connected to. Connected systems interact in some way. The exact meaning of interact is defined by sub properties of [**_seas:connectedTo_**]. 
