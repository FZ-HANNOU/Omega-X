# Energy Role Ontology

## Description
### Purpose
The Energy Role ontology is dedicated to business parties, their intended behaviour and relationships with other elements involved in energy market business processes. 
### Scope
The Energy Role ontology defines three generic concepts: business parties (participant), business roles (role) and their relationships (association). Roles are further refined in classifications specific to electromobility, flexibility and local energy communities domains.

## Competency Questions

| ID | Question in natural language | Example
|---|---|---|
| cq-1 | Get the list of Charge Point Operators. |
| cq-2 | Get the list of eMobility Service Providers. |
| cq-3 | Get the list of market participants that are altogether Charge Point Operators and eMobility Service Providers. |

## Glossary
* Market Participant: (source IEC 62325-351 Ed.3) The identification of the party participating in energy market business processes.
* Market Role: (source IEC 62325-351 Ed.3) The identification of the intended behaviour of a market participant played within a given business process.
* Association: (source The PROV Namespace) An instance of prov:Association provides additional descriptions about the binary prov:wasAssociatedWith relation from an prov:Activity to some prov:Agent that had some responsiblity for it.

## OWL Description
The Energy Role Ontology contains a generic model and specific classifications for electromobility, local energy community and flexibility:
- Generic model
![Diagram](./EnergyRoleOntologyV10-Energy_Role_Generic.png)
- Classification for Electromobility roles
![Diagram](./EnergyRoleOntologyV10-Energy_Role_EM.png)
- Classification for Local Energy Community roles
![Diagram](./EnergyRoleOntologyV10-Energy_Role_LEC.png)
- Classification for Flexibility roles
![Diagram](./EnergyRoleOntologyV10-Energy_Role_FLEX.png)

## Recommendations
- When used as datatype property of 'role:MarketParticipant', it is recommended to give to 'role:identifier' a value delivered by an authorized authority. 

- When used as datatype properties of 'role:MarketRole', it is recommended to give to 'role:identifier' and 'role:name' values recognised by a standard role model (https://eepublicdownloads.entsoe.eu/clean-documents/EDI/Library/HRM/Harmonised_Role_Model_2022-01.pdf, for instance). 

## See Also
### SEAS 1.1
* [**_seas:Player_**](https://w3id.org/seas/PlayerOntology-1.1): One of the important people, companies etc involved in a particular industry, market, situation etc. (source: the Longman Business Dictionary).

* [**_seas:ElectricityMarket_**](https://w3id.org/seas/PlayerOntology-1.1): The class of Electricity Market SEAS players.
