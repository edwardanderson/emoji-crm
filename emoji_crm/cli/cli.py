import emoji
import pickle

from argparse import ArgumentParser
from pathlib import Path


def main():
    parser = ArgumentParser()
    parser.add_argument(
        'emoji',
        nargs='+',
        type=str
    )
    parser.add_argument(
        '--no-cache',
        action='store_false'
    )
    args = parser.parse_args()
    character = ' '.join(args.emoji)

    if emoji.is_emoji(character):
        query = f'describe <{character}>'
    else:
        query = f'''
        prefix crm: <http://www.cidoc-crm.org/cidoc-crm/>

        describe ?emoji where {{
            ?emoji a crm:E37_Mark ;
                crm:P1_is_identified_by ?name ;
                crm:P2_has_type <http://vocab.getty.edu/aat/300412189> .
            
            ?name a crm:E33_E41_Linguistic_Appellation ;
                crm:P72_has_language <https://vocab.getty.edu/aat/300388277> ;
                crm:P190_has_symbolic_content "{character}" .

            ?language a crm:E56_Language .
        }}
        '''

    path = Path(__file__).parent / 'emoji_crm.pkl'
    if path.is_file() and args.no_cache:
        with open(path, 'rb') as file:
            EMOJI_CRM = pickle.load(file)
    else:
        from emoji_crm.data import EMOJI_CRM

        with open(path, 'wb') as file:
            pickle.dump(EMOJI_CRM, file)

    description = EMOJI_CRM.query(query)
    print(description.serialize(format='longturtle').decode('utf-8'))


if __name__ == '__main__':
    main()
