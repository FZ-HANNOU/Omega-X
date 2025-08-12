# Local Energy Communities Ontology

## Description
### Purpose
Optimizing self consuption, losses detection and gamification for eletric saving requires some knoweldge on LEC equipments.
### Scope
Local energy communities ontology provides OWL classes and properties to allow local energy equipments and their static parameters to be described.
### Description
This Local Energy Communities ontology helps to define the equipments of OMEGA-X Local energy communities use cases. It includes the battery, transformer, bus, smart meter and Intelligent Distribution Power Router. 

## Competency Questions

### Querying Questions
| ID | Question in natural language | Example
|---|---|---|
| cq-1 |What are the batteries used? | The list of batteries.|
| cq-2 |What are the equipments? | The  list of equipment. |
| cq-3 |What is the location of specific bus? | the  geolocation of a specific bus|

### Inference Questions
| ID | Question in natural language | Example
|---|---|---|
| iq-1 |To which batteries a specific solar inverter is connected to?| The list of batteries connected to a specific solar inverter|

## Glossary
### Omega-X LEC
* [**lec:_Battery_**](https://w3id.org/omega-x/ontology/LocalEnergyCommunities/Battery)
Battery electric power storage systems.
* [**lec:_PowerElectronicDevice_**](https://w3id.org/omega-x/s/ontology/LocalEnergyCommunities/PowerElectronicDevice)
Power electronic device that takes power from the battery/grid to balance the difference phases.
* [**lec:_IntelligentDistributionPowerRouter_**](https://w3id.org/omega-x/ontology/LocalEnergyCommunities/IntelligentDistributionPowerRouter)
Intelligent Distribution Power Router.
* [**lec:_PointOfCommonCoupling_**](https://w3id.org/omega-x/ontology/LocalEnergyCommunities/PointOfCommonCoupling)
The exchange point of the grid.
* [**lec:_Transformer_**](https://w3id.org/omega-x/ontology/LocalEnergyCommunities/Transformer)
A static piece of apparatus with two or more windings which, by electromagnetic induction, transforms a system of alternating voltage and current into another system of voltage and current usually of different values and at the same frequency for the purpose of transmitting electrical power.
* [**lec:_HomeManagementSystem_**](https://w3id.org/omega-x/ontology/LocalEnergyCommunities/HomeManagementSystem)
Smart, often automated system that monitors, manages, and optimizes energy usage within an individual household or building.

## OWL Description

![Diagram](./LocalEnergyCommunities.png)

## Related Work

### SEAS
* [**_seas:Battery_**]( https://w3id.org/seas/Battery): The class of batteries, which are electric power storage systems.

* [**_seas:stateOfChargeRatio_**]( https://w3id.org/seas/stateOfChargeRatio):The state of charge of a battery, quantified by unitless values.

* [**_seas:ElectricPowerSystem_**]( https://w3id.org/seas/ElectricPowerSystem):The class of electric power systems, i.e., systems that exchange electricity (i.e., electric power) with other systems.

### PLATOON
* [**_plt:Transformer_**]( <https://w3id.org/platoon/Transformer): An electric power transformer is an electric power system that is capable of transforming electricity within a power network, between a primary connection point and a secondary connection point.
