<a name="ds-structuredatasetmetadatajson"> </a>

# StructureDataset D-PLACE dataset derived from Binford 2001 'Constructing Frames of Reference'

**CLDF Metadata**: [StructureDataset-metadata.json](./StructureDataset-metadata.json)

**Sources**: [sources.bib](./sources.bib)

The Binford Hunter-Gatherer dataset describes cultural practices for 339 hunter-gatherer groups. Approximately two-thirds of the societies described by Binford are also described in the Ethnographic Atlas. However, the Binford database includes a number of societies not in the Ethnographic Atlas, including many in Australia and northern North America.

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Binford, L. 2001. Constructing Frames of Reference: An Analytical Method for Archaeological Theory Building Using Hunter-gatherer and Environmental Data Sets. University of California Press
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF StructureDataset](http://cldf.clld.org/v1.0/terms.rdf#StructureDataset)
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by-nc/4.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/D-PLACE/dplace-dataset-binford
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/D-PLACE/dplace-dataset-binford/tree/v3.0.1">D-PLACE/dplace-dataset-binford v3.0.1</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v5.0">Glottolog v5.0</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.10.12</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | dplace-dataset-binford
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-datacsv"></a>Table [data.csv](./data.csv)

Values are coded datapoints, i.e. measurements of a variable for a society.

**Note:** Missing data is signaled by an empty Value column.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ValueTable](http://cldf.clld.org/v1.0/terms.rdf#ValueTable)
[dc:extent](http://purl.org/dc/terms/extent) | 13957


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Soc_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [societies.csv::ID](#table-societiescsv)
[Var_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | References [variables.csv::ID](#table-variablescsv)
[Value](http://cldf.clld.org/v1.0/terms.rdf#value) | `string` | Values for categorical and ordinal variables reference the corresponding code via the Code_ID column. Values for continuous variables have the measured number in the Value column and an empty Code_ID.
[Code_ID](http://cldf.clld.org/v1.0/terms.rdf#codeReference) | `string` | References [codes.csv::ID](#table-codescsv)
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
`sub_case` | `string` | More specific description of the population the data refer to in terms of society or area.
`year` | `string`<br>Regex: `-?[0-9]{1,4}(-[0-9]{4})?` | Focal year, i.e. the time period to which the data refer.
`source_coded_data` | `string` | The source of the coded data, which was aggregated in this dataset.
`admin_comment` | `string` | 

## <a name="table-societiescsv"></a>Table [societies.csv](./societies.csv)

We use the term “society” to refer to cultural groups. In most cases, a society can be understood to represent a group of people at a focal location with a shared language that differs from that of their neighbors. However, in some cases multiple societies share a language.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 339


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal`<br>&ge; -90<br>&le; 90 | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal`<br>&ge; -180<br>&le; 180 | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string`<br>Regex: `[a-z0-9]{4}[1-9][0-9]{3}` | 
`Name_and_ID_in_source` | `string` | Society names identified as pejorative have been replaced with a preferred, English-language ethnonym. The name (and ID) as given in the source dataset is kept in this field.
`xd_id` | `string` | “cross-data-set” identifier, used to link societies present in different datasets, if they share a focal location. Note: If this field is empty, other fields such as Name, Glottocode, focal year and location may be used to identify societies across datasets if appropriate.
`alt_names_by_society` | list of `string` (separated by `; `) | A list of ‘alternate’ names for the society; includes, where available, one or more autonyms in the society’s own language, as well as other commonly encountered ethnonyms.
`main_focal_year` | `integer` | Focal year specifying the time period to which the data refer, given as number of years BCE - if negative - or CE.
`HRAF_name_ID` | `string` | Name(s) and ID(s) of the corresponding society in HRAF (the Human Relations Area Files)
`HRAF_ID` | `string` | ID of the corresponding society in HRAF
`origLat` | `decimal`<br>&ge; -90<br>&le; 90 | Uncorrected latitude as given in the source.
`origLong` | `decimal`<br>&ge; -270<br>&le; 180 | Uncorrected longitude as given in the source.
[comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
`glottocode_comment` | `string` | Comment on the Glottocode assignment.
`region` | `string` | World Geographical Scheme for Recording Plant Distributions level2 region

## <a name="table-variablescsv"></a>Table [variables.csv](./variables.csv)

Variables are cultural features or practices, or environmental descriptors.

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ParameterTable](http://cldf.clld.org/v1.0/terms.rdf#ParameterTable)
[dc:extent](http://purl.org/dc/terms/extent) | 40


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[A-Za-z.0-9_]+([0-9]+)?` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[ColumnSpec](http://cldf.clld.org/v1.0/terms.rdf#columnSpec) | `json` | 
`category` | list of `string` (separated by `, `) | 
`type` | `string`<br>Valid choices:<br> `Continuous` `Categorical` `Ordinal` | Variables may be categorical (and then must be accompanied by a list of possible ‘codes’, i.e. rows in Codetable. Variables can also be continuous (e.g. Population size) or ordinal. Ordinal variables are accompanied by a list of codes (like categorical variables). The order of codes is encoded as `ord` column in CodeTable.
`unit` | `string` | The unit of measurement
`source_comment` | `string` | A note about the source of this variable.
`changes` | `string` | Notes about how a variable may have been derived from the source.
[comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 

## <a name="table-codescsv"></a>Table [codes.csv](./codes.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF CodeTable](http://cldf.clld.org/v1.0/terms.rdf#CodeTable)
[dc:extent](http://purl.org/dc/terms/extent) | 83


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string`<br>Regex: `[a-zA-Z0-9_\-]+` | Primary key
[Var_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | The parameter or variable the code belongs to.<br>References [variables.csv::ID](#table-variablescsv)
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
`ord` | `integer` | 

