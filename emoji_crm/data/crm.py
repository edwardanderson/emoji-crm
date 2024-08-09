import re

from emoji_skos.data import EMOJI_SKOS
from emoji_crm.alignments import ALIGNMENTS
from pathlib import Path
from rdflib import Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS


path = Path(__file__).parent / 'skos_to_crm.rq'
construct = path.read_text()

# This SPARQL transformation is very slow.
result = EMOJI_SKOS.query(construct)

EMOJI_CRM = result.graph
CRM = Namespace('http://www.cidoc-crm.org/cidoc-crm/')
EMOJI_CRM.bind('crm', CRM)

for emoji in EMOJI_CRM.subjects(RDF.type, CRM.E37_Mark, unique=True):
    if len(emoji) == 1:
        continue

    # :emoji crm:P106_is_composed_of :unicode-part.
    for character in emoji:
        # Ignore zero-width joiner.
        if character == '\u200D':
            continue

        part = URIRef(character)
        EMOJI_CRM.add((emoji, CRM.P106_is_composed_of, part))
        EMOJI_CRM.add((part, CRM.P106_forms_part_of, emoji))

    # :skin-tone-modified-profession crm:P130_shows_features_of :(un)gendered-person.
    pattern = r'^(.[🏻🏼🏽🏾🏿])\u200D.$'
    for group in re.findall(pattern, emoji, flags=re.UNICODE):
        person = URIRef(group)
        if emoji != person:
            EMOJI_CRM.add((emoji, CRM.P130_shows_features_of, person))
            # inverse.
            EMOJI_CRM.add((person, CRM.P130i_features_are_also_found_on, emoji))

    # :skin-tone-modified-profession crm:P130_shows_features_of :(un)gendered-profession.
    pattern = r'^(.)[🏻🏼🏽🏾🏿]\u200D(.)$'
    for group in re.findall(pattern, emoji, flags=re.UNICODE):
        profession = group[0] + '\u200D' + group[1]
        profession = URIRef(profession)
        if emoji != profession:
            EMOJI_CRM.add((emoji, CRM.P130_shows_features_of, profession))
            # inverse.
            EMOJI_CRM.add((profession, CRM.P130i_features_are_also_found_on, emoji))

    # :gendered-profession crm:P130_shows_features_of :ungendered-profession.
    pattern = r'^[👨👩]\u200D(.)$'
    for group in re.findall(pattern, emoji, flags=re.UNICODE):
        profession = '🧑' + '\u200D' + group[0]
        profession = URIRef(profession)
        if emoji != profession:
            EMOJI_CRM.add((emoji, CRM.P130_shows_features_of, profession))
            # inverse.
            EMOJI_CRM.add((profession, CRM.P130i_features_are_also_found_on, emoji))

    # crm:P199_represents_instance_of_type
    for name, data in ALIGNMENTS.items():
        pattern = data['pattern']
        for group in re.findall(pattern, emoji, flags=re.UNICODE):
            represented = data['alignments'].get(group)
            if represented:
                profession, label = represented
                EMOJI_CRM.add((emoji, CRM.P199_represents_instance_of_type, profession))
                EMOJI_CRM.add((profession, RDF.type, CRM.E55_Type))
                EMOJI_CRM.add((profession, RDFS.label, Literal(label)))

if __name__ == '__main__':
    print(EMOJI_CRM.serialize(format='longturtle'))
