# Diccionarios para mapear los PDFs de Mage : The ascension - 20th Aniversario. 

CAMPO_MAP_MAGO_OFICIAL = {
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

    # BACKGROUNDS
    "backgrounds1": "backgrounds1",
    "backgrounds2": "backgrounds2",
    "backgrounds3": "backgrounds3",
    "backgrounds4": "backgrounds4",
    "backgrounds5": "backgrounds5",
    "backgrounds6": "backgrounds6",

    # CARACTERISTICAS DEL PERSONAJE

    "name": "name",
    "player": "player",
    "chronicle": "chronicle",
    "nature": "nature",
    "demeanor": "demeanor",
    "experience": "experience",
    "essence": "essence",
    "affiliation": "affiliation",
    "sect": "sect",
    "concept": "concept",

    # OT: Otros rasgos personalizados
    "othertraits1" : "othertraits1",
    "othertraits2" : "othertraits2",
    "othertraits3" : "othertraits3",
    "othertraits4" : "othertraits4",
    "othertraits5" : "othertraits5",
    "othertraits6" : "othertraits6",
    "OT1" : "othertraits7",
    "OT2" : "othertraits8",
    "OT3" : "othertraits9",
    "OT4" : "othertraits10",
    "OT5" : "othertraits11",
    "OT6" : "othertraits12",
    "OT7" : "othertraits13",
    "OT8" : "othertraits14",
    "OT9" : "othertraits15",

    # Health:
    "health1": "health1",
    "health2": "health2",
    "health3": "health3",
    "health4": "health4",
    "health5": "health5",
    "health6": "health6",
    "health7": "health7",

    # Magic:

    # Wonders personalizados
    **{f"magic{i}": f"wonder{i}" for i in list(range(1, 7))},

    # Rotes personalizados
    **{f"magic{i}" : f"rote{i}" for i in list(range(7, 17))},

    # Paradigma personalizados
    **{f"magic{i}" : f"paradigm{i}" for i in list(range(18, 21))},

    # Paradigma personalizados
    **{f"magic{i}" : f"practice{i}" for i in list(range(22, 26))},

    # Paradigma personalizados
    **{f"magic{i}" : f"instrument{i}" for i in list(range(27, 35))},

    # Combat: Armas/ataques (6 columnas x 7 filas)
    **{f"combat{c}": f"combat_row{((c - 1) % 6) + 1}_col{((c - 1) // 6) + 1}" for c in range(1, 43)},

    # Armor: piezas de armadura
    "armor1" : "class",
    "armor2" : "rating",
    "armor3" : "penalty",
    **{f"armor{i}": f"armor_description{i}" for i in range(4, 7)},

    # Possessions

    # Gear
    **{f"possessions{i}" : f"gear{i}" for i in range(1, 7)},

    # Equipment
    **{f"possessions{i}" : f"equipment{i}" for i in range(11, 17)},

    # Familiar
    **{f"possessions{i}" : f"familiar{i}" for i in range(7, 11)},

    # Grimoires
    **{f"possessions{i}" : f"grimoires{i}" for i in range(17, 21)},

    # Chantry

    # Location
    **{f"chantry{i}": f"location{i}" for i in range(1, 7)},

    # Location_description
    **{f"chantry{i}": f"location_description{i}" for i in range(7, 13)},

    # History

    # Awakening
    **{f"history{i}" : f"awakening{i}" for i in range(1, 6)},

    # Goals
    **{f"history{i}" : f"goals{i}" for i in range(6, 10)},

    # Seekings
    **{f"history{i}" : f"seekings{i}" for i in range(10, 14)},

    # Quiets
    **{f"history{i}" : f"quiets{i}" for i in range(10, 18)},

    # Description
    "description1" : "age",
    "description2" : "apparent_age",
    "description3" : "date_birth",
    "description4" : "awakening_age",
    "description5" : "hair",
    "description6" : "eyes",
    "description7" : "ethnicity",
    "description8" : "nationality",
    "description9" : "height",
    "description10" : "weight",
    "description11" : "gender",

    **{f"description{i}": f"description{i}" for i in range(12, 20)},

    "description20" : "avatar",

    **{f"description{i}": f"description{i}" for i in range(21, 23)},

    # Merits y Flaws
    **{f"Merit{i}": f"merit{i}" for i in range(1, 8)},
    **{f"Flaw{i}": f"flaw{i}" for i in range(1, 8)},
    **{f"type{i}": f"type{i}" for i in range(1, 15)},
    **{f"cost{i}": f"cost{i}" for i in range(1, 15)},
    
    # Expanded Backgrounds
    **{f"EBtitle{i}": f"EBtitle{i}" for i in range(1, 11)},
    **{f"EB{i}": f"EB{i}" for i in range(1, 32)}
}

DOT_GRUPOS_MAGO_OFICIAL = {
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

    # BACKGROUNDS

    "backgrounds1_dots" : ['xdotm16', 'xdotm17', 'xdotm18', 'xdotm19', 'xdotm20'],
    "backgrounds2_dots" : ['dot137', 'dot138', 'dot139', 'dot140', 'dot141'],
    "backgrounds3_dots" : ['dot145', 'dot146', 'dot147', 'dot148', 'dot149'],
    "backgrounds4_dots" : ['dot217', 'dot218', 'dot219', 'dot220', 'dot221'],
    "backgrounds5_dots" : ['dot225', 'dot226', 'dot227', 'dot228', 'dot229'],
    "backgrounds6_dots" : ['dot297', 'dot298', 'dot299', 'dot300', 'dot301'],

    # OTHER_TRAITS

    "other_trait_1_dots": ['dot305', 'dot306', 'dot307', 'dot308', 'dot309'],
    "other_trait_2_dots": ['dot393', 'dot394', 'dot395', 'dot396', 'dot397'],
    "other_trait_3_dots": ['dot401', 'dot402', 'dot403', 'dot404', 'dot405'],
    "other_trait_4_dots": ['dot313', 'dot314', 'dot315', 'dot316', 'dot317'],
    "other_trait_5_dots": ['dot321', 'dot322', 'dot323', 'dot324', 'dot325'],
    "other_trait_6_dots": ['OTdot1', 'OTdot2', 'OTdot3', 'OTdot4', 'OTdot5'],
    "other_trait_7_dots": ['dot497', 'dot498', 'dot499', 'dot500', 'dot501'],
    "other_trait_8_dots": ['dot505', 'dot506', 'dot507', 'dot508', 'dot509'],
    "other_trait_9_dots": ['dot513', 'dot514', 'dot515', 'dot516', 'dot517'],
    "other_trait_10_dots": ['dot521', 'dot522', 'dot523', 'dot524', 'dot525'],
    "other_trait_11_dots": ['dot529', 'dot530', 'dot531', 'dot532', 'dot533'],
    "other_trait_12_dots": ['dot537', 'dot538', 'dot539', 'dot540', 'dot541'],
    "other_trait_13_dots": ['dot545', 'dot546', 'dot547', 'dot548', 'dot549'],
    "other_trait_14_dots": ['dot553', 'dot554', 'dot555', 'dot556', 'dot557'],
    "other_trait_15_dots": ['dot561', 'dot562', 'dot563', 'dot564', 'dot566'],

    # VOLUNTAD
    "willpower_dots": ['willdot1', 'willdot2', 'willdot3', 'willdot4', 'willdot5',
                       'willdot6', 'willdot7', 'willdot8', 'willdot9', 'willdot10'],
    
    "willpower_check": ['check1b', 'check2b', 'check3b','check4b', 'check5b',
                        'check6b', 'check7b', 'check8b', 'check9b', 'check10b'],

    # ARETE
    "arete_dots": ['bpdot1', 'bpdot2', 'bpdot3', 'bpdot4', 'bpdot5',
                   'bpdot6', 'bpdot7', 'bpdot8', 'bpdot9', 'bpdot10'],

    # ESFERAS
    "correspondence_dots": ['sdot1', 'sdot2', 'sdot3', 'sdot4', 'sdot5'],
    "entropy_dots":        ['sdot6', 'sdot7', 'sdot8', 'sdot9', 'sdot10'],
    "forces_dots":         ['sdot11', 'sdot12', 'sdot13', 'sdot14', 'sdot15'],
    "life_dots":           ['sdot16', 'sdot17', 'sdot18', 'sdot19', 'sdot20'],
    "matter_dots":         ['sdot21', 'sdot22', 'sdot23', 'sdot24', 'sdot25'],
    "mind_dots":           ['sdot26', 'sdot27', 'sdot28', 'sdot29', 'sdot30'],
    "prime_dots":          ['sdot31', 'sdot32', 'sdot33', 'sdot34', 'sdot35'],
    "spirit_dots":         ['sdot36', 'sdot37', 'sdot38', 'sdot39', 'sdot40'],
    "time_dots":           ['sdot41', 'sdot42', 'sdot43', 'sdot44', 'sdot45']
}

def contar_quintaesencia_y_paradoja(campos):
    """
        Función que cuenta los qpcheck points o dots de quintaescencia o paradoja según su uso en la planilla PDF.
    """
    quintaesencia = 0
    paradoja = 0

    checks = [f"qpcheck{i}" for i in range(1, 21)]
    valores = [campos.get(check, {}).get("valor_actual", "") in {"Ye", "Yes", "On"} for check in checks]

    # Quintessence: cuenta del inicio
    for valor in valores:
        if valor:
            quintaesencia += 1
        else:
            break  # solo cuenta los "Yes" consecutivos desde el principio

    # Paradox: cuenta desde el final
    for valor in reversed(valores):
        if valor:
            paradoja += 1
        else:
            break  # solo cuenta los "Yes" consecutivos desde el final

    return {
        "quintessence_dots": quintaesencia,
        "paradox_dots": paradoja
    }