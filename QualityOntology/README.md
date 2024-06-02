# Quality Ontology

## Description
` Quality`, or `QUal`, is a domain ontology module of the Common Semantic Data Model (CSDM). It is a common ontology that enables to describe quality dimensions associated with data. It can be : 

- Aggregation Level: indicates the granularity of each data value, such as sum of values or average. Aggregation can be performed spatially, temporally or logically.
- Quality Metrics: indicates the quality metrics attributes associated with data according to data quality dimensions defined by ISO 25012.
- Measurement Procedure: indicates what procedure produced the data: measurement, prediction,...  

## Competency Questions
### Querying Questions
| ID | Question in natural language | Example
|---|---|---|
| cq-1 | How elements of time series are grouped temporally ? | Each element of a time series corresponds to either a value observed at the timestamp |

| cq-2 | Is the value set complete regarding the temporal coverage period ? | The completeness of a value set can be evaluated using the percentage of missing values. |

| cq-3 | How was data produced ? | Data production process can be indicated to distinguish service-computed datasets from metered data for example. |

| cq-3 | WHat is the list of device properties described with the dataset ? | Data can represent grouped electrical consumption of a set of home appliances for example. The aggregation context should list these elements. |

## Glossary

* [**_qual:QualityMetric_**](https://w3id.org/omega-x/QualityOntology/QualityMetric/): The class of quantifiable measures used to assess a quality attribute.

* [**_qual:QualityAttribute_**](https://w3id.org/omega-x/QualityOntology/QualityAttribute/): The class of attributes representing the degree to which data satisfy the requirements.

* [**_qual:Aggregation_**](https://w3id.org/omega-x/QualityOntology/Aggregation/): The class of functions applied to aggregate data such as sum of values or average

* [**_qual:MeasuringProcedure_**](https://w3id.org/omega-x/QualityOntology/MeasuringProcedure/): The class of procedures used to provide data
## OWL Description

![Diagram](./QualityDiagram.png)


## Recommendations
- A `qual:Aggregation` enables the definition of what aggregation level to be used while interpreting values in a value set. The aggreation can occur on a `TemporalContext` indicating a time interval on which the aggregaton has been applied, a `SpatialAggregationContext` indicating a spatial location on which the aggreation has been applied or a `LogicalAggregationContext` to cover other grouping types. 
If no aggregation indicated, the default interpretation can be to associate the exact value to the corresponding timestamp.

- According to usage, individuals are created for each (function, Aggregation contexte). For example, `qual:HourlySum` indicates an Aggregation of type `qual:Sum` with a `qual:TemporalAggregationContext` of 1 hour.

- The `qual:MeasuringProcedure` enables to indicate the procedure used to produce data. The use of hardware devices such as smart meters indicates a `qual:Metering` procedure, `qual:Observation` for sensors, while software simulators give `qual:Simulation`, scheduling services `qual:Scheduling` and `qual:Prediction` for other software predicting data. 

- A set of `qual:QualityMetric` can be associated with a `ets:ValueSet` to describe its quality. For each relevant quality metric, one individual should be created to indicate the `qual:value`. For example, to descrive the `qual:Completeness` of the electrical consumption time series `ElectricityTimeSeries`, a `ETSPercentOfMissingValues` individual of type `qual:PercentOfMissingValues` enables to provide a value of completeness. 

## Related Work

### ISO 25012

[ISO 25012](https://iso25000.com/index.php/en/iso-25000-standards/iso-25012)