# Emoji CRM

Dataset of emojis represented in [CIDOC-CRM](https://cidoc-crm.org/) as an [`rdflib.Graph`](https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.html#rdflib.Graph). It is based on [Emoji SKOS](https://github.com/edwardanderson/emoji-skos).

> [!WARNING]
> Emoji CRM is an on-going research project and is not yet ready for use in production.

## Quickstart

```bash
pip install git+https://github.com/edwardanderson/emoji-crm
```

## CLI

```bash
emoji-crm 👩🏽‍🚀
```

```bash
emoji-crm woman astronaut medium skin tone
```

## Module

```python
from emoji_crm.data import EMOJI_CRM

query = 'describe <👩🏽‍🚀>'
result = EMOJI_CRM.query(query)
print(result.serialize(format='longturtle').decode('utf-8'))
```

```turtle
PREFIX crm: <http://www.cidoc-crm.org/cidoc-crm/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

<👩🏽‍🚀>
    a crm:E37_Mark ;
    rdfs:label "👩🏽‍🚀 woman astronaut medium skin tone" ;
    crm:P106_is_composed_of
        <🏽> ,
        <👩> ,
        <🚀> ;
    crm:P130_shows_features_of
        <👩‍🚀> ,
        <👩🏽> ;
    crm:P148i_is_component_of <people-and-body> ;
    crm:P190_has_symbolic_content "👩🏽‍🚀" ;
    crm:P199_represents_instance_of_type <https://vocab.getty.edu/aat/300380152> ;
    crm:P1_is_identified_by
        [
            a crm:E33_E41_Linguistic_Appellation ;
            crm:P190_has_symbolic_content "antariksawan wanita warna kulit sedang" ;
            crm:P72_has_language <https://vocab.getty.edu/aat/300388460> ;
        ] ,
        [
            a crm:E33_E41_Linguistic_Appellation ;
            crm:P190_has_symbolic_content "astronautin mittlere hautfarbe" ;
            crm:P72_has_language <https://vocab.getty.edu/aat/300388344> ;
        ] ,
        [
            a crm:E33_E41_Linguistic_Appellation ;
            crm:P190_has_symbolic_content "رائدة فضاء بشرة بلون معتدل" ;
            crm:P72_has_language <https://vocab.getty.edu/aat/300387843> ;
        ] ,
        [
            a crm:E33_E41_Linguistic_Appellation ;
            crm:P190_has_symbolic_content "женщина космонавт средний тон кожи" ;
            crm:P72_has_language <https://vocab.getty.edu/aat/300389168> ;
        ] ,
        [
            a crm:E33_E41_Linguistic_Appellation ;
            crm:P190_has_symbolic_content "여자 우주비행사 갈색 피부" ;
            crm:P72_has_language <https://vocab.getty.edu/aat/300388633> ;
        ] ,
        [
            a crm:E33_E41_Linguistic_Appellation ;
            crm:P190_has_symbolic_content "astronauta mujer tono de piel medio" ;
            crm:P72_has_language <https://vocab.getty.edu/aat/300389311> ;
        ] ,
        [
            a crm:E33_E41_Linguistic_Appellation ;
            crm:P190_has_symbolic_content "woman astronaut medium skin tone" ;
            crm:P72_has_language <https://vocab.getty.edu/aat/300388277> ;
        ] ,
        [
            a crm:E33_E41_Linguistic_Appellation ;
            crm:P190_has_symbolic_content "kadın astronot orta cilt tonu" ;
            crm:P72_has_language <https://vocab.getty.edu/aat/300389470> ;
        ] ,
        [
            a crm:E33_E41_Linguistic_Appellation ;
            crm:P190_has_symbolic_content "astronaute femme peau légèrement mate" ;
            crm:P72_has_language <https://vocab.getty.edu/aat/300388306> ;
        ] ,
        [
            a crm:E33_E41_Linguistic_Appellation ;
            crm:P190_has_symbolic_content "女性宇宙飛行士 中間の肌色" ;
            crm:P72_has_language <https://vocab.getty.edu/aat/300388486> ;
        ] ,
        [
            a crm:E33_E41_Linguistic_Appellation ;
            crm:P190_has_symbolic_content "astronauta donna carnagione olivastra" ;
            crm:P72_has_language <https://vocab.getty.edu/aat/300388474> ;
        ] ,
        [
            a crm:E33_E41_Linguistic_Appellation ;
            crm:P190_has_symbolic_content "女宇航员 中等肤色" ;
            crm:P72_has_language <https://vocab.getty.edu/aat/300388113> ;
        ] ;
    crm:P2_has_type <http://vocab.getty.edu/aat/300412189> ;
.
```

## Acknowledgements

Unicode Data Files are distributed under the [Unicode License v3](https://www.unicode.org/license.txt) which is included in this repository at [docs/unicode_license_v3.txt](docs/unicode_license_v3.txt).
