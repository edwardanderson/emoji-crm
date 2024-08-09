from rdflib.namespace import Namespace


AAT = Namespace('https://vocab.getty.edu/aat/')
WD = Namespace('http://www.wikidata.org/entity/')

ALIGNMENTS = {
    'professions': {
        'pattern': r'^[🧑👨👩][🏻🏼🏽🏾🏿]?\u200D(.)$',
        'alignments': {
            '⚕️':  (WD['Q87285943'], 'health professional'),
            '⚖️':  (AAT['300025625'], 'judges'),
            '✈️':  (AAT['300236293'], 'pilots'),
            '🌾': (AAT['300025607'], 'farmers'),
            '🍳': (AAT['300248012'], 'cooks'),
            '🎓': (AAT['300025909'], 'students'),
            '🎤': (AAT['300025684'], 'singers'),
            '🎨': (AAT['300025103'], 'artists (visual artists)'),
            '🏫': (AAT['300025529'], 'teachers'),
            '🏭': (WD['Q87285943'], 'factory worker'),
            '💻': (AAT['300237760'], 'technologists'),
            '💼': (AAT['300137140'], 'clerical workers'),
            '🔧': (AAT['300025272'], 'mechanics'),
            '🔬': (AAT['300025788'], 'scientists'),
            '🚀': (AAT['300380152'], 'astronauts'),
            '🚒': (AAT['300025862'], 'firefighters')
        }
    },
    'gender_alternates': {
        'pattern': r'^(.)(?=\uFE0F\u200D[♀️♂️]\uFE0F)?',
        'alignments': {
            '🕵️': (AAT['300136450'], 'detectives'),
            '👷': (AAT['300025001'], 'construction workers'),
            '👮': (AAT['300025867'], 'police officers'),
            '💂': (AAT['300185678'], 'soldiers')
        }
    },
    'gendered_professions': {
        'pattern': r'^(.)$',
        'alignments': {
            '🤴': (AAT['300025482'], 'princes (rulers)'),
            '👸': (AAT['300155241'], 'princesses'),
            '🫅': (AAT['300025475'], 'rulers')
        }
    }
}
