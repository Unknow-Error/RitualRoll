

CAMPO_MAP_WEREWOLF_OFICIAL = {
    # ATRIBUTOS
    "attrib1": "strength",
    "attrib2": "dexterity",
    "attrib3": "stamina",
    "attrib4": "charisma",
    "attrib5": "manipulation",
    "attrib6": "appearance",
    "attrib7": "perception",
    "attrib8": "intelligence",
    "attrib9": "wits",

    # TALENTS (Talentos)
    "abilities1": "alertness",
    "abilities2": "athletics",
    "abilities3": "brawl",
    "abilities4": "empathy",
    "abilities5": "expression",
    "abilities6": "intimidation",
    "abilities7": "leadership",
    "abilities8": "primal_urges",
    "abilities9": "streetwise",
    "abilities10": "subterfuge",
    "abilities31": "extra_talent",

    # SKILLS (Habilidades)
    "abilities11": "animal_ken",
    "abilities12": "crafts",
    "abilities13": "drive",
    "abilities14": "etiquette",
    "abilities15": "firearms",
    "abilities16": "larceny",
    "abilities17": "melee",
    "abilities18": "performance",
    "abilities19": "stealth",
    "abilities20": "survival",
    "abilities32": "extra_skill",

    # KNOWLEDGES (Conocimientos)
    "abilities21": "academics",
    "abilities22": "computer",
    "abilities23": "enigmas",
    "abilities24": "investigation",
    "abilities25": "law",
    "abilities26": "medicine",
    "abilities27": "occult",
    "abilities28": "rituals",
    "abilities29": "science",
    "abilities30": "technology",
    "abilities33": "extra_knowledge",

    # BACKGROUNDS
    "back1": "back1",
    "back2": "back2",
    "back3": "back3",
    "back4": "back4",
    "back5": "back5",

    # GIFTS
    **{f"gifts{i}": f"gifts{i}" for i in list(range(1, 11))},

    # CARACTERISTICAS DEL PERSONAJE

    "name": "name",
    "player": "player",
    "chronicle": "chronicle",
    "breed": "breed",
    "auspice": "auspice",
    "tribe": "tribe",
    "experience": "experience",
    "packname": "packname",
    "totem": "totem",
    "concept": "concept",
    "rank": "rank",

    # OT: Otros rasgos personalizados
    "OT1" : "othertraits1",
    "OT2" : "othertraits2",
    "OT3" : "othertraits3",
    "OT4" : "othertraits4",
    "OT5" : "othertraits5",
    "OT6" : "othertraits6",
    "OT7" : "othertraits7",
    "OT8" : "othertraits8",
    "OT9" : "othertraits9",
    "OT10" : "othertraits10",
    "OT11" : "othertraits11",
    "OT12" : "othertraits12",

    # Health:
    "health1": "health1",
    "health2": "health2",
    "health3": "health3",
    "health4": "health4",
    "health5": "health5",
    "health6": "health6",
    "health7": "health7",

    # Fetiches:

    **{f"fetishes{c + 4}": f"fetishes_item{c}" for c in range(1,7)},

    # Merits y Flaws
    **{f"Merit{i}": f"merit{i}" for i in range(1, 8)},
    **{f"Flaw{i}": f"flaw{i}" for i in range(1, 8)},
    **{f"type{i}": f"type{i}" for i in range(1, 15)},
    **{f"cost{i}": f"cost{i}" for i in range(1, 15)},

    # Expanded Backgrounds
    **{f"EBtitle{i}": f"EBtitle{i}" for i in range(1, 11)},
    **{f"EB{i}": f"EB{i}" for i in range(1, 32)}
}

DOT_GRUPOS_WEREWOLF_OFICIAL = {
    # ATRIBUTOS
    "strength_dots": ['dot1', 'dot2', 'dot3', 'dot4', 'dot5'],
    "dexterity_dots": ['dot9', 'dot10', 'dot11', 'dot12', 'dot13'],
    "stamina_dots": ['dot17', 'dot18', 'dot19', 'dot20', 'dot21'],
    "charisma_dots": ['dot25', 'dot26', 'dot27', 'dot28', 'dot29'],
    "manipulation_dots": ['dot33', 'dot34', 'dot35', 'dot36', 'dot37'],
    "appearance_dots": ['dot41', 'dot42', 'dot43', 'dot44', 'dot45'],
    "perception_dots": ['dot49', 'dot50', 'dot51', 'dot52', 'dot53'],
    "intelligence_dots": ['dot57', 'dot58', 'dot59', 'dot60', 'dot61'],
    "wits_dots": ['dot65', 'dot66', 'dot67', 'dot68', 'dot69'],

    #TALENTS

    "alertness_dots":   ['dot73', 'dot74', 'dot75', 'dot76', 'dot77'],
    "athletics_dots":         ['dot81', 'dot82', 'dot83', 'dot84', 'dot85'],
    "brawl_dots":   ['dot89', 'dot90', 'dot91', 'dot92', 'dot93'],
    "empathy_dots":   ['dot97', 'dot98', 'dot99', 'dot100', 'dot101'],
    "expression_dots":       ['dot105', 'dot106', 'dot107', 'dot108', 'dot109'],
    "intimidation_dots":     ['dot113', 'dot114', 'dot115', 'dot116', 'dot117'],
    "leadership_dots":  ['dot121', 'dot122', 'dot123', 'dot124', 'dot125'],
    "primal_urges_dots":['dot129', 'dot130', 'dot131', 'dot132', 'dot133'],
    "streetwise_dots":  ['dot137', 'dot138', 'dot139', 'dot140', 'dot141'],
    "subterfuge_dots":  ['dot145', 'dot146', 'dot147', 'dot148', 'dot149'],
    "extra_talent_dots":   ['dot145qw', 'dot146qw', 'dot147qw', 'dot148qw', 'dot149qw'],

    #SKILLS

    "animal_ken_dots":        ['dot153', 'dot154', 'dot155', 'dot156', 'dot157'],
    "crafts_dots":         ['dot161', 'dot162', 'dot163', 'dot164', 'dot165'],
    "drive_dots":     ['dot169', 'dot170', 'dot171', 'dot172', 'dot173'],
    "etiquette_dots":      ['dot177', 'dot178', 'dot179', 'dot180', 'dot181'],
    "firearms_dots":  ['dot185', 'dot186', 'dot187', 'dot188', 'dot189'],
    "larceny_dots":    ['dot193', 'dot194', 'dot195', 'dot196', 'dot197'],
    "melee_dots":         ['dot201', 'dot202', 'dot203', 'dot204', 'dot205'],
    "performance_dots":      ['dot209', 'dot210', 'dot211', 'dot212', 'dot213'],
    "stealth_dots":       ['dot217', 'dot218', 'dot219', 'dot220', 'dot221'],
    "survival_dots":      ['dot225', 'dot226', 'dot227', 'dot228', 'dot229'],
    "extra_skill_dots":   ['dot225qw', 'dot226qw', 'dot227qw', 'dot228qw', 'dot229qw'],

    # KNOWLEDGES

    "academics_dots":      ['dot233', 'dot234', 'dot235', 'dot236', 'dot237'],
    "computer_dots":       ['dot241', 'dot242', 'dot243', 'dot244', 'dot245'],
    "enigmas_dots":      ['dot249', 'dot250', 'dot251', 'dot252', 'dot253'],
    "investigation_dots":        ['dot257', 'dot258', 'dot259', 'dot260', 'dot261'],
    "law_dots":      ['dot265', 'dot266', 'dot267', 'dot268', 'dot269'],
    "medicine_dots":  ['dot273', 'dot274', 'dot275', 'dot276', 'dot277'],
    "occult_dots":            ['dot281', 'dot282', 'dot283', 'dot284', 'dot285'],
    "rituals_dots":       ['dot289', 'dot290', 'dot291', 'dot292', 'dot293'],
    "science_dots":         ['dot297', 'dot298', 'dot299', 'dot300', 'dot301'],
    "technology_dots":       ['dot305', 'dot306', 'dot307', 'dot308', 'dot309'],
    "extra_knowledge_dots":   ['dot305qw', 'dot306qw', 'dot307qw', 'dot308qw', 'dot309qw'],

    # RENOWN
    
    "glory_dots" : ['renowndot1', 'renowndot2', 'renowndot3', 'renowndot4', 'renowndot5',
                    'renowndot6', 'renowndot7', 'renowndot8', 'renowndot9', 'renowndot10'],

    "glory_check" : ['check1', 'check2', 'check3','check4', 'check5',
                        'check6', 'check7', 'check8', 'check9', 'check10'],
    
    'honor_dots' : ['renowndot11', 'renowndot12', 'renowndot13', 'renowndot14', 'renowndot15',
                    'renowndot16', 'renowndot17', 'renowndot18', 'renowndot19', 'renowndot20'],
    
    'honor_check' : ['check11', 'check12', 'check13','check14', 'check15',
                        'check16', 'check17', 'check18', 'check19', 'check20'],
    
    'widsom_dots' : ['renowndot21', 'renowndot22', 'renowndot23', 'renowndot24', 'renowndot25',
                     'renowndot26', 'renowndot27', 'renowndot28', 'renowndot29', 'renowndot30'],
    
    'widsom_check' : ['check21', 'check22', 'check23','check24', 'check25',
                        'check26', 'check27', 'check28', 'check29', 'check30'],

    # RAGE, GNOSIS, WILLPOWER

    "rage_dots": ['ragedot1', 'ragedot2', 'ragedot3', 'ragedot4', 'ragedot5',
                  'ragedot6', 'ragedot7', 'ragedot8', 'ragedot9', 'ragedot10'],
    
    "rage_check": ['check31', 'check32', 'check33','check34', 'check35',
                  'check36', 'check37', 'check38', 'check39', 'check40'],

    "gnosis_dots": ['gnosisdot1', 'gnosisdot2', 'gnosisdot3', 'gnosisdot4', 'gnosisdot5',
                  'gnosisdot6', 'gnosisdot7', 'gnosisdot8', 'gnosisdot9', 'gnosisdot10'],
    
    "gnosis_check": ['check41', 'check42', 'check43','check44', 'check45',
                  'check46', 'check47', 'check48', 'check49', 'check50'],
    
    "willpower_dots": ['willdot1', 'willdot2', 'willdot3', 'willdot4', 'willdot5',
                       'willdot6', 'willdot7', 'willdot8', 'willdot9', 'willdot10'],
    
    "willpower_check": ['check51', 'check52', 'check53','check54', 'check55',
                        'check56', 'check57', 'check58', 'check59', 'check60'],

}