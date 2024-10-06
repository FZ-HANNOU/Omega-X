# Domain Ontology: Property

## Description
`Property`, or `Prop`, is a domain level module of the Common Semantic Data Model (CSDM). It provides a taxonomy of energy domain properties. 
The scope of this module extends also to the definition of units and categories associated with properties, and used for values definition.

## Competency Questions
### Querying Questions
| ID | Question in natural language | Example
|---|---|---|
| cq-1 | What are possible values to be associated with a qualitative property ? | Possible values for a qualitative property include the set of values defined in the category in which it is evaluated. |
| cq-2 | What are possible properties that can be associated with a unit of measurement ? | EUR-PER-KiloW-HR is a unit of measurement that can be used for energySellingprice, EnergyBuyingPrice,... |
| cq-3 | What are possible units for measuring a property ? | Temperature property can be measured in Celsus Degrees,  Fahrenheit degrees,... |

## Glossary

## OWL Description

![Diagram](./Property.png)


## Recommendations
- A `prop:Property` is the upper class for the omega-X property taxonomy. It is further distinguished into `prop:QuantitativeProperty` for properties to which numerical values are assigned (`prop:Temperature` has as possible values `18`, `19`,..), and `prop:QualitativeProperty` for properties with values defined in a category (eg. `prop:OperatingStatus` has as possible values `On` and `Off`). 

- The evaluation of properties is described in `Event and Time Series` module, through the `ets:PropertyValue` class . For dyamic values (chaning over time), a `ets:ValueSet` is created with the entire set of values, following a `ets:TemporalContext`. For static values (stable in time), the object property `prop:hasPropertyValue` enables to indicate one value per property.

- Categorical individuals of type `prop:Category` are used as property values `ets:PropertyValue` in case of qualitative Datasets.