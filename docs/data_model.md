# Data Model

- [Data Model](#data-model)
  - [URIs](#uris)
  - [Vocabulary](#vocabulary)
  - [`crm:E37_Mark`](#crme37_mark)

## URIs

- Relative pure-emoji URIs, with disambiguating class atributes in the path where necessary.
- kebab-case

## Vocabulary

- Getty Art & Architecture Thesaurus

## `crm:E37_Mark`

```turtle
prefix crm: <http://www.cidoc-crm.org/cidoc-crm/>
prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>

<👩🏿‍🚒>
    a crm:E37_Mark ;
    rdfs:label "👩🏿‍🚒 woman firefighter dark skin tone" ;
    crm:P1_is_identified_by
        [
            a crm:E33_E41_Appellation ;
            crm:P190_has_symbolic_content "woman firefighter dark skin tone" ;
            crm:P72_has_language <https://vocab.getty.edu/aat/300388277>
        ] ;
    crm:P2_has_type <http://vocab.getty.edu/aat/300412189> ;
    crm:P106_is_composed_of
        <👩> , # woman
        <🏿> ,  # dark skin tone
        <‍> ,   # zero width joiner
        <🚒> ; # fire engine
    crm:P130_shows_features_of
        <👩🏿> ,    # woman dark skin tone
        <👩‍🚒> ,    # woman firefighter
        <🧑‍🚒> ;  # firefighter
    crm:P148i_is_component_of <people-and-body> ;
    crm:P190_has_symbolic_content "👩🏿‍🚒" ;
    crm:P199_represents_instance_of_type <https://vocab.getty.edu/aat/300025862> ;
.

<http://vocab.getty.edu/aat/300412189>
    a crm:E55_Type ;
    rdfs:label "emoji" ;
.

<people-and-body>
    a crm:E73_Information_Object ;
    rdfs:label "People & Body" ;
    crm:P148_has_component <👩🏿‍🚒> ;
    crm:P129_is_about
        <https://vocab.getty.edu/aat/300024979> ,
        <https://vocab.getty.edu/aat/300404640> ;
.

<https://vocab.getty.edu/aat/300388277>
    a crm:E56_Language ;
    rdfs:label "English (language)" ;
.

<https://vocab.getty.edu/aat/300025862>
    a crm:E55_Type ;
    rdfs:label "firefighters" ;
.

<https://vocab.getty.edu/aat/300024979>
    a crm:E55_Type ;
    rdfs:label "people (agents)"
.

<https://vocab.getty.edu/aat/300404640>
    a crm:E55_Type ;
    rdfs:label "bodies (animal components)"
.
```
