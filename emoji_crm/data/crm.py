from emoji_skos.data import EMOJI_SKOS
from pathlib import Path
from rdflib import Namespace, URIRef
from rdflib.namespace import RDF, SKOS


path = Path(__file__).parent / 'skos_to_crm.rq'
construct = path.read_text()

# This SPARQL query is very slow.
result = EMOJI_SKOS.query(construct)

EMOJI_CRM = result.graph
EMOJI_CRM.bind('crm', 'http://www.cidoc-crm.org/cidoc-crm/')
CRM = Namespace('http://www.cidoc-crm.org/cidoc-crm/')

# # crm:P106_is_composed_of
for emoji in EMOJI_SKOS.subjects(RDF.type, SKOS.Concept, unique=True):
    if len(emoji) == 1:
        continue

    for character in emoji:
        if character == '\u200c':
            # Ignore zero-width joiner.
            continue

        part = URIRef(character)
        EMOJI_CRM.add((emoji, CRM.P106_is_composed_of, part))
        EMOJI_CRM.add((part, CRM.P106_forms_part_of, emoji))


if __name__ == '__main__':
    print(EMOJI_CRM.serialize(format='longturtle'))
