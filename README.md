# Omega-X Ontology Repository

Welcome to the Omega-X Ontology repository! 

## Repository Structure

The repository structure is built to fit multi-level modular ontologies.
It hosts also relevant alignements to external resources (ontologies/standards). 

The tooling section includes automation scripts for various tasks: ontology building, documentation release, semantic validation, data semantization...

The omega-X ontology is defined by two modules: a core ontology for Events and Time Series (ETS) and a domain ontology for Energy Data Set (EDS). 
```
📂 Omega-X Ontology 
│
├─ 📁 Top Level-ETS Ontology
│   ├── 📄 onto.ttl                  /* T-box
│   ├── 📄 dataset.ttl              /* A-box
│   ├── 🖼️ diagram.<imgFormat>     /* eg. CHOWLK diagram
│   ├── ❓ cq-Q.rq                 /* A set of Competency questions translated as Sparql queries.
│   └── 📄 README.md
│
├─ 📁 Domain Ontologies
│   ├── 📄 onto.ttl               /* T-box
│   ├── 📄 dataset.ttl           /* A-box
│   ├── 🖼️ diagram.<imgFormat>  /* eg. CHOWLK diagram
│   ├── ❓ cq-Q.rq              /* A set of Competency questions translated as Sparql queries.
│   └── 📄 README.md
│
├─ 📁 Application-UC Ontology      /* One folder per application ontology (Renewable, Electromobility, LEC, Flexibility)
│   ├── 📄 onto.ttl               /* T-box
│   ├── 📄 dataset.ttl           /* A-box
│   ├── 🖼️ diagram.<imgFormat>  /* eg. CHOWLK diagram
│   ├── ❓ cq-Q.rq              /* A set of Competency questions translated as Sparql queries.
│   └── 📄 README.md
│
├─ 📁 Tooling
│   ├── 📁 AO-generator            /* Application-oriented Ontology refinement 
│   ├── 📁 SHACL                  /* Shacl constraints and validation 
│   ├── 📁 doc                   /* Doc generations scripts
│   ├── 📁 tests                /* Validation tests (structure, syntax, querying) 
│   ├── 📁 Best Practices      /* Ontology development best practices recommendations 
│   ├── 📁 AO-generator            /* Application-oriented Ontology refinement 
│   ├── 📁 SHACL                  /* Shacl constraints and validation 
│   ├── 📁 doc                   /* Doc generations scripts
│   ├── 📁 tests                /* Validation tests (structure, syntax, querying) 
│   ├── 📁 Best Practices      /* Ontology development best practices recommendations 
│   └── 📄 README.md
│
├─ 📁 External Resources
│   ├── 📁 EUMED Metering
│   ├── 📄 onto.ttl              /* T-box
│   │   ├── 📁 Alignements      /* Alignements of EUMED with Omega-X.
│   └── 📄 README.md
│
├─ 📄 README.md
```

## List of modules 
Group Name| Module | Scope |State
|---|---|---|---|
|Top Level | Events and Time Series (ETS) | ETS ontology provides classes and properties to allow commonly used data structures to be described. | V 1.0
|Domain | Energy Data Set (EDS) | EDS ontology extends ETS definitions with specefic energy domain context (both technical and business). | V 1.0
|Domain | Eumed Metering (EME) | EME ontology is a semantisation of the Eumed metering profile of the CIM standard. | v1.0
|Domain | Property (PROP) | PROP ontology provides a taxonomy of properties used in the energy domain. | v1.0
|Domain | Infrastructure (INFRA) | INFRA ontology provides a common description for systems infrastructures in the energy domain, to be further specialiazed in UC ontologies. | v1.0
|Domain | Actor role (ROLE) | ROLE ontology provides a description of business entities roles in the dataspace and in their business activities. | v1.0
|Domain | Quality (QUAL) | QUAL ontology provides a taxonomy of quality indicators associated with datasets. | v1.0
|Domain | Scheduling (SCHE) | SCHE ontology provides a common description of schedules. | v1.0
|Use Case Family | Renewable (REN) | REN is the use case ontology for the renewables use case family. | V0.1 (in progress)
|Use Case Family | Flexibility (FLEX) | FLEX is the use case ontology for the flexibility use case family. | V0.1 (in progress)
|Use Case Family | Local Energy Communities (LEC) | LEC is the use case ontology for the lec use case family. | V0.1 (in progress)
|Use Case Family | Electromobility (EM) | EM is the use case ontology for the electromobility use case family. | V0.1 (in progress)

## Overview of common modules

The figure below illustrates common modules (Top level and domain modules). The online diagram version is available here : 
[Common Modules Diagram](https://app.diagrams.net/#G1q05sxDvyCEwQj_UCIHW11u9iUm4L0wDy#%7B%22pageId%22%3A%22oPHg0NIDeMugmmmMHvXY%22%7D)

![Common Modules](./CommonModules.png)

## Utils

- Ontology diagrams can be defined using CHOWLK [diagram.net](https://app.diagrams.net/). A library for specific ontology conceptualisation is available here [CHOWLK Ontology library](https://chowlk.linkeddata.es/). To learn more about visual notation specification, see: [CHOWLK Documentation](https://chowlk.linkeddata.es/notation.html). 

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Credit
This work has been conducted by [Electricité De France (EDF)](https://www.edf.fr/) team and partners ([Ecole des mines de Saint-Etienne](https://www.mines-stetienne.fr/) and [Trialog](https://www.trialog.com/fr/accueil/)), in the frame of the European projetc Omega-X [Omega-X website](https://omega-x.eu/), 

![alt text](EU.png)
