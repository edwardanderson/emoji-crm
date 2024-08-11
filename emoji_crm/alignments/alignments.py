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
        'pattern': r'^(.)[🏻🏼🏽🏾🏿]?\uFE0F?\u200D?[♀️♂️]?',
        'alignments': {
            '🕵': (AAT['300136450'], 'detectives'),
            '👷': (AAT['300025001'], 'construction workers'),
            '👮': (AAT['300025867'], 'police officers'),
            '💂': (AAT['300185678'], 'soldiers'),
            '🤴': (AAT['300025482'], 'princes (rulers)'),
            '👸': (AAT['300155241'], 'princesses'),
            '🫅':  (AAT['300025475'], 'rulers'),
            '👰': (AAT['300404297'], 'wedding veils')
        }
    },
    'fruits_and_vegetables': {
        'pattern': r'^(.\u200D?[🟩🟫]?)?$',
        'alignments': {
            '🍇': (AAT['300379338'], 'grapes (berry fruit)'),
            '🍈': (AAT['300266444'], 'melon (fruit)'),
            '🍉': (WD['Q38645'], 'watermelon'),
            '🍊': (WD['Q104030498'], 'tangerine'),
            '🍋': (AAT['300266423'], 'lemons (fruits)'),
            '🍋‍🟩': (AAT['300266424'], 'limes (fruits)'),
            '🍌': (AAT['300266434'], 'bananas (fruits)'),
            '🍍': (AAT['300375583'], 'pineapple (fruit)'),
            '🥭': (AAT['300266436'], 'mangoes (fruits)'),
            '🍎': (AAT['300266417'], 'apples (fruits)'),
            '🍏': (AAT['300266417'], 'apples (fruits)'),
            '🍐': (AAT['300435353'], 'pears'),
            '🍑': (AAT['300266272'], 'peaches (fruits)'),
            '🍒': (AAT['300440730'], 'cherries (fruits)'),
            '🍓': (AAT['300375414'], 'strawberries (fruits)'),
            '🫐': (AAT['300375417'], 'blueberries (fruit)'),
            '🥝': (WD['Q13194'], 'kiwifruit'),
            '🍅': (AAT['300266435'], 'tomato'),
            '🫒': (AAT['300266440'], 'olives (fruits)'),
            '🥑': (WD['Q961769'], 'avocado'),
            '🍆': (WD['Q12533094'], 'eggplant'),
            '🥔': (AAT['300435305'], 'potato'),
            '🥕': (AAT['300435295'], 'carrots'),
            '🌽': (WD['Q1885918'], 'corncob'),
            '🌶️': (WD['Q1885918'], 'chili pepper'),
            '🫑': (WD['Q1548030'], 'bell pepper'),
            '🥒': (WD['Q2735883'], 'cucumber'),
            '🥬': (WD['Q20134'], 'leaf vegetable'),
            '🥦': (WD['Q47722'], 'broccoli'),
            '🧄': (WD['Q21546392'], 'garlic'),
            '🧅': (AAT['onion'], 'onions (bulbs)'),
            '🥜': (WD['Q37383'], 'peanut'),
            '🫘': (WD['Q379813'], 'bean'),
            '🌰': (AAT['300266428'], 'chestnuts (nuts)'),
            '': (WD['Q15046077'], 'ginger'),
            '🫛': (WD['Q29472543'], 'pea'),
            '🍄‍🟫': (AAT['300417849'], 'mushrooms (fungi)'),
            '🍄': (AAT['300417849'], 'mushrooms (fungi)')
        }
    },
    'man_or_woman_or_boy_or_girl': {
        'pattern': r'([👨👩👦👧])',
        'alignments': {
            '👨': (AAT['300025928'], 'men (male humans)'),
            '👩': (AAT['300025943'], 'woman (female humans)'),
            '👦': (AAT['300247598'], 'boys'),
            '👧': (AAT['300247581'], 'girls')

        }
    },
    'male_or_female': {
        'pattern': r'.+([♀️♂️]\uFE0F?)',
        'alignments': {
            '♂️': (AAT['300025928'], 'men (male humans)'),
            '♀️': (AAT['300025943'], 'woman (female humans)')
        }
    },
    'kiss': {
        'pattern': r'.+(💋).+',
        'alignments': {
            '💋': (WD['Q7307'], 'kiss')
        }
    },
    'couple': {
        'pattern': r'(?:[👨👩].*)(❤️)(?:.*[👨👩])',
        'alignments': {
            '❤️': (AAT['300379217'], 'couples'),
        }
    }
}
