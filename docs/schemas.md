# Schemas


## Introduction
Data schemas are abstractions wrapping database model definitions which are used for
data _serialization_ and _deserialization_ across multiple software components. These operations
are the standard way of interchanging information between far-away components using the internet.


## Schema vs Model
There exists a relationship between this package _data schemas_ and [the core package][dialect-map-core]
_data models_, such that every schema depends on the data model defined columns to define their own fields.
Alternatively, there could be model-independent schemas whose only purpose would be to exchange compatible data,
without storing it. **That is not the case**.

When comparing the nature of a _data schema_ against a _data model_, consider:

### Data model
- It defines how information is stored in the persistent layer (databases).
- It defines storage properties such as indexes, relationships and constraints.
- It performs storage validation (i.e. unique within the table, foreign key exists...)

### Data schema
- It defines how data model _compliant_ records must be serialized / deserialized.
- It could populate / augment certain data fields from the context / other fields.
- If performs data quality validations (i.e. valid format, not null value...)


[dialect-map-core]: https://github.com/dialect-map/dialect-map-core
