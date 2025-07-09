# Diccionarios para mapear los PDFs de Mage : The ascension - 20th Aniversario. 
CAMPO_MAP_MAGO = {
    # ATRIBUTOS
    "attributes1": "strength",
    "attributes2": "dexterity",
    "attributes3": "stamina",
    "attributes4": "charisma",
    "attributes5": "manipulation",
    "attributes6": "appearance",
    "attributes7": "perception",
    "attributes8": "intelligence",
    "attributes9": "wits",

    # TALENTS (Talentos)
    "skills1": "alertness",
    "skills2": "art",
    "skills3": "athletics",
    "skills4": "awareness",
    "skills5": "brawl",
    "skills6": "empathy",
    "skills7": "expression",
    "skills8": "intimidation",
    "skills9": "leadership",
    "skills10": "streetwise",
    "skills11": "subterfuge",
    "skillsex1": "extra_talent",

    # SKILLS (Habilidades)
    "skills12": "crafts",
    "skills13": "drive",
    "skills14": "etiquette",
    "skills15": "firearms",
    "skills16": "martial_arts",
    "skills17": "meditation",
    "skills18": "melee",
    "skills19": "research",
    "skills20": "stealth",
    "skills21": "survival",
    "skills22": "technology",
    "skillsex2": "extra_skill",

    # KNOWLEDGES (Conocimientos)
    "skills23": "academics",
    "skills24": "computer",
    "skills25": "cosmology",
    "skills26": "enigmas",
    "skills27": "esoterica",
    "skills28": "investigation",
    "skills29": "law",
    "skills30": "medicine",
    "skills31": "occult",
    "skills32": "politics",
    "skills33": "science",
    "skillsex3": "extra_knowledge",


    # ESFERAS
    "spheres1": "correspondence",
    "spheres2": "entropy",
    "spheres3": "forces",
    "spheres4": "life",
    "spheres5": "matter",
    "spheres6": "mind",
    "spheres7": "prime",
    "spheres8": "spirit",
    "spheres9": "time",

    # OTROS CAMPOS ÚTILES
    "name": "name",
    "player": "player",
    "chronicle": "chronicle",
    "nature": "nature",
    "demeanor": "demeanor",
    "essence": "essence",
    "affiliation": "affiliation",
    "sect": "sect",
    "concept": "concept",

    # BACKGROUNDS
    "backgrounds1": "background_1",
    "backgrounds2": "background_2",
    "backgrounds3": "background_3",
    "backgrounds4": "background_4",
    "backgrounds5": "background_5",
    "backgrounds6": "background_6",

    # VOLUNTAD, ARETE, PARADOJA, QUINTESSENCIA, EXPERIENCIA (pueden necesitar mapeo de dots/checkboxes también)
    "experience": "experience",
    "willpower": "willpower",
    "willpower_check": "willpower_check",    

     # OT: Otros rasgos personalizados
    "OT1": "other_trait_1",
    "OT2": "other_trait_2",
    "OT3": "other_trait_3",
    "OT4": "other_trait_4",
    "OT5": "other_trait_5",
    "OT6": "other_trait_6",
    "OT7": "other_trait_7",
    "OT8": "other_trait_8",
    "OT9": "other_trait_9",

    # Magic: Rotes personalizados
    **{f"magic{i}": f"rote_{i}" for i in list(range(1, 17)) + [18, 19, 20, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34]},

    # Combat: Armas/ataques (6 columnas x 7 filas)
    **{f"combat{c}": f"combat_row{((c - 1) % 6) + 1}_col{((c - 1) // 6) + 1}" for c in range(1, 43)},

    # Armor: piezas de armadura
    **{f"armor{i}": f"armor_piece_{i}" for i in range(1, 7)},

    # Possessions
    **{f"possessions{i}": f"possession_{i}" for i in range(1, 21)},

    # Chantry
    **{f"chantry{i}": f"chantry_{i}" for i in range(1, 13)},

    # History
    **{f"history{i}": f"history_{i}" for i in range(1, 18)},

    # Description
    **{f"description{i}": f"description_{i}" for i in range(1, 23)},

    # Merits y Flaws
    **{f"Merit{i}": f"merit_{i}" for i in range(1, 8)},
    **{f"Flaw{i}": f"flaw_{i}" for i in range(1, 8)},
    **{f"type{i}": f"meritflaw_type_{i}" for i in range(1, 15)},
    **{f"cost{i}": f"meritflaw_cost_{i}" for i in range(1, 15)},
}

DOT_YE_VALUES = {"Ye", "Yes", "On"}  # valores activados para dots

DOT_GROUPS_MAGO = {
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
    "art_dots":         ['dot81', 'dot82', 'dot83', 'dot84', 'dot85'],
    "athletics_dots":   ['dot89', 'dot90', 'dot91', 'dot92', 'dot93'],
    "awareness_dots":   ['dot97', 'dot98', 'dot99', 'dot100', 'dot101'],
    "brawl_dots":       ['dot105', 'dot106', 'dot107', 'dot108', 'dot109'],
    "empathy_dots":     ['dot113', 'dot114', 'dot115', 'dot116', 'dot117'],
    "expression_dots":  ['dot121', 'dot122', 'dot123', 'dot124', 'dot125'],
    "intimidation_dots":['dot129', 'dot130', 'dot131', 'dot132', 'dot133'],
    "leadership_dots":  ['dot153', 'dot154', 'dot155', 'dot156', 'dot157'],
    "streetwise_dots":  ['dot161', 'dot162', 'dot163', 'dot164', 'dot165'],
    "subterfuge_dots":  ['dot169', 'dot170', 'dot171', 'dot172', 'dot173'],
    "extra_talent_dots":   ['dot169e', 'dot170e', 'dot171e', 'dot172e', 'dot173e'],

    #SKILLS

    "crafts_dots":        ['dot177', 'dot178', 'dot179', 'dot180', 'dot181'],
    "drive_dots":         ['dot185', 'dot186', 'dot187', 'dot188', 'dot189'],
    "etiquette_dots":     ['dot193', 'dot194', 'dot195', 'dot196', 'dot197'],
    "firearms_dots":      ['dot201', 'dot202', 'dot203', 'dot204', 'dot205'],
    "martial_arts_dots":  ['dot209', 'dot210', 'dot211', 'dot212', 'dot213'],
    "meditation_dots":    ['dot233', 'dot234', 'dot235', 'dot236', 'dot237'],
    "melee_dots":         ['dot241', 'dot242', 'dot243', 'dot244', 'dot245'],
    "research_dots":      ['dot249', 'dot250', 'dot251', 'dot252', 'dot253'],
    "stealth_dots":       ['dot257', 'dot258', 'dot259', 'dot260', 'dot261'],
    "survival_dots":      ['dot265', 'dot266', 'dot267', 'dot268', 'dot269'],
    "technology_dots":    ['dot273', 'dot274', 'dot275', 'dot276', 'dot277'],
    "extra_skill_dots":   ['dot273e', 'dot274e', 'dot275e', 'dot276e', 'dot277e'],

    # KNOWLEDGES

    "academics_dots":      ['dot281', 'dot282', 'dot283', 'dot284', 'dot285'],
    "computer_dots":       ['dot289', 'dot290', 'dot291', 'dot292', 'dot293'],
    "cosmology_dots":      ['dot329', 'dot330', 'dot331', 'dot332', 'dot333'],
    "enigmas_dots":        ['dot337', 'dot338', 'dot339', 'dot340', 'dot341'],
    "esoterica_dots":      ['dot345', 'dot346', 'dot347', 'dot348', 'dot349'],
    "investigation_dots":  ['xdot1', 'xdot2', 'xdot3', 'xdot4', 'xdot5'],
    "law_dots":            ['xdot11', 'xdot12', 'xdot13', 'xdot14', 'xdot15'],
    "medicine_dots":       ['xdot16', 'xdot17', 'xdot18', 'xdot19', 'xdot20'],
    "occult_dots":         ['xdotm1', 'xdotm2', 'xdotm3', 'xdotm4', 'xdotm5'],
    "politics_dots":       ['xdotm6', 'xdotm7', 'xdotm8', 'xdotm9', 'xdotm10'],
    "science_dots":        ['xdotm11', 'xdotm12', 'xdotm13', 'xdotm14', 'xdotm15'],
    "extra_knowledge_dots":   ['xdotm11e', 'xdotm12e', 'xdotm13e', 'xdotm14e', 'xdotm15e'],


    # VOLUNTAD
    "willpower_dots": ['willdot1', 'willdot2', 'willdot3', 'willdot4', 'willdot5',
                       'willdot6', 'willdot7', 'willdot8', 'willdot9', 'willdot10'],
    
    "willpower_check": ['check1b', 'check2b', 'check3b','check4b', 'check5b',
                        'check6b', 'check7b', 'check8b', 'check9b', 'check10b'],

    # ARETE
    "arete_dots": ['bpdot1', 'bpdot2', 'bpdot3', 'bpdot4', 'bpdot5',
                   'bpdot6', 'bpdot7', 'bpdot8', 'bpdot9', 'bpdot10'],

    # QUINTESSENCIA
    "quintessence_dots": ['qpcheck1', 'qpcheck2', 'qpcheck3', 'qpcheck4',
                          'qpcheck5', 'qpcheck6', 'qpcheck7', 'qpcheck8',
                          'qpcheck9', 'qpcheck10', 'qpcheck11', 'qpcheck12',
                          'qpcheck13', 'qpcheck14', 'qpcheck15', 'qpcheck16',
                          'qpcheck17', 'qpcheck18', 'qpcheck19', 'qpcheck20'],

    # ESFERAS
    "correspondence_dots": ['sdot1', 'sdot2', 'sdot3', 'sdot4', 'sdot5'],
    "entropy_dots":        ['sdot6', 'sdot7', 'sdot8', 'sdot9', 'sdot10'],
    "forces_dots":         ['sdot11', 'sdot12', 'sdot13', 'sdot14', 'sdot15'],
    "life_dots":           ['sdot16', 'sdot17', 'sdot18', 'sdot19', 'sdot20'],
    "matter_dots":         ['sdot21', 'sdot22', 'sdot23', 'sdot24', 'sdot25'],
    "mind_dots":           ['sdot26', 'sdot27', 'sdot28', 'sdot29', 'sdot30'],
    "prime_dots":          ['sdot31', 'sdot32', 'sdot33', 'sdot34', 'sdot35'],
    "spirit_dots":         ['sdot36', 'sdot37', 'sdot38', 'sdot39', 'sdot40'],
    "time_dots":           ['sdot41', 'sdot42', 'sdot43', 'sdot44', 'sdot45'],

    # SALUD
    "health_status": ['health1', 'health2', 'health3', 'health4', 'health5', 'health6', 'health7'],

    # OTRAS TRAZAS (custom dots)
    "custom_dots_1": ['dot137', 'dot138', 'dot139', 'dot140', 'dot141'],
    "custom_dots_2": ['dot145', 'dot146', 'dot147', 'dot148', 'dot149'],
    "custom_dots_3": ['dot217', 'dot218', 'dot219', 'dot220', 'dot221'],
    "custom_dots_4": ['dot297', 'dot298', 'dot299', 'dot300', 'dot301'],
}