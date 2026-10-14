"""
acb_teams.py - Comprehensive team dictionary, franchise lineages, home arenas,
and city/region mappings for Spanish Basketball (Liga ACB, Liga Nacional, Copa del Rey, Supercopa).
"""

ACB_FRANCHISE_MAP = {
    # Real Madrid
    "real madrid": {
        "canonical": "Real Madrid",
        "full_name": "Real Madrid Baloncesto",
        "short_name": "RMB",
        "arena": "WiZink Center",
        "city": "Madrid",
        "region": "Community of Madrid",
        "capacity": 15000,
        "aliases": ["real madrid", "real madrid baloncesto", "rmb"]
    },
    # FC Barcelona
    "barcelona": {
        "canonical": "FC Barcelona",
        "full_name": "FC Barcelona Bàsquet",
        "short_name": "BAR",
        "arena": "Palau Blaugrana",
        "city": "Barcelona",
        "region": "Catalonia",
        "capacity": 7585,
        "aliases": ["barça", "barca", "fc barcelona", "fc barcelona bàsquet", "winterthur fcb", "regal fc barcelona", "fc barcelona lassa", "barcelona"]
    },
    # Saski Baskonia
    "baskonia": {
        "canonical": "Baskonia",
        "full_name": "Saski Baskonia",
        "short_name": "BKN",
        "arena": "Fernando Buesa Arena",
        "city": "Vitoria-Gasteiz",
        "region": "Basque Country",
        "capacity": 15716,
        "aliases": ["baskonia", "saski baskonia", "taugrés", "taugres", "tau cerámica", "tau ceramica", "caja laboral", "laboral kutxa", "kirolbet baskonia", "bitci baskonia", "cazoo baskonia", "kosner baskonia", "basconia"]
    },
    # Club Joventut Badalona
    "joventut": {
        "canonical": "Joventut Badalona",
        "full_name": "Club Joventut Badalona",
        "short_name": "JOV",
        "arena": "Palau Municipal d'Esports de Badalona",
        "city": "Badalona",
        "region": "Catalonia",
        "capacity": 12760,
        "aliases": ["joventut", "joventut badalona", "club joventut badalona", "ron negrita joventut", "ram joventut", "montigalà joventut", "7up joventut", "festina joventut", "dkv joventut", "fiatc joventut", "divina seguros joventut", "asisa joventut"]
    },
    # Baloncesto Málaga (Unicaja)
    "unicaja": {
        "canonical": "Unicaja",
        "full_name": "Club Baloncesto Málaga",
        "short_name": "UNI",
        "arena": "Palacio de Deportes José María Martín Carpena",
        "city": "Málaga",
        "region": "Andalusia",
        "capacity": 11300,
        "aliases": ["unicaja", "unicaja málaga", "unicaja de málaga", "baloncesto málaga", "caja de ronda", "mayoral maristas", "unicaja mayoral"]
    },
    # Valencia Basket
    "valencia": {
        "canonical": "Valencia Basket",
        "full_name": "Valencia Basket Club",
        "short_name": "VBC",
        "arena": "Pabellón Municipal Fuente de San Luis",
        "city": "Valencia",
        "region": "Valencian Community",
        "capacity": 9000,
        "aliases": ["valencia basket", "valencia", "valencia basket club", "pamesa valencia", "power electronics valencia", "vbc"]
    },
    # CB Gran Canaria
    "gran canaria": {
        "canonical": "Gran Canaria",
        "full_name": "Club Baloncesto Gran Canaria",
        "short_name": "DGC",
        "arena": "Gran Canaria Arena",
        "city": "Las Palmas de Gran Canaria",
        "region": "Canary Islands",
        "capacity": 11500,
        "aliases": ["gran canaria", "cb gran canaria", "claret las palmas", "coren gran canaria", "auna gran canaria", "kalise gran canaria", "herbalife gran canaria", "dreamland gran canaria"]
    },
    # CB Canarias (Tenerife)
    "tenerife": {
        "canonical": "Lenovo Tenerife",
        "full_name": "Club Baloncesto 1939 Canarias",
        "short_name": "LNT",
        "arena": "Pabellón de Deportes de Tenerife Santiago Martín",
        "city": "San Cristóbal de La Laguna",
        "region": "Canary Islands",
        "capacity": 5100,
        "aliases": ["tenerife", "cb canarias", "lenovo tenerife", "iberostar tenerife", "la laguna tenerife", "cajacanarias"]
    },
    # CB Estudiantes
    "estudiantes": {
        "canonical": "Estudiantes",
        "full_name": "Club Baloncesto Estudiantes",
        "short_name": "EST",
        "arena": "WiZink Center",
        "city": "Madrid",
        "region": "Community of Madrid",
        "capacity": 15000,
        "aliases": ["estudiantes", "cb estudiantes", "estudiantes monteverde", "estudiantes caja postal", "adecco estudiantes", "mmt estudiantes", "asefa estudiantes", "movistar estudiantes"]
    },
    # Bàsquet Manresa
    "manresa": {
        "canonical": "BAXI Manresa",
        "full_name": "Bàsquet Manresa",
        "short_name": "BAX",
        "arena": "Pavelló Nou Congost",
        "city": "Manresa",
        "region": "Catalonia",
        "capacity": 5000,
        "aliases": ["manresa", "bàsquet manresa", "tdk manresa", "ricoh manresa", "assignia manresa", "la bruixa d'or manresa", "icl manresa", "baxi manresa", "kidsandus manresa"]
    },
    # Basket Zaragoza
    "zaragoza": {
        "canonical": "Casademont Zaragoza",
        "full_name": "Basket Zaragoza 2002",
        "short_name": "CAZ",
        "arena": "Pabellón Príncipe Felipe",
        "city": "Zaragoza",
        "region": "Aragon",
        "capacity": 10744,
        "aliases": ["zaragoza", "basket zaragoza", "cai zaragoza", "casademont zaragoza", "cb zaragoza"]
    },
    # Bilbao Basket
    "bilbao": {
        "canonical": "Bilbao Basket",
        "full_name": "Club Basket Bilbao Berri",
        "short_name": "SBB",
        "arena": "Bilbao Arena",
        "city": "Bilbao",
        "region": "Basque Country",
        "capacity": 10014,
        "aliases": ["bilbao basket", "bilbao", "lagun aro bilbao", "bizkaia bilbao", "dominion bilbao", "retabet bilbao basket", "surne bilbao basket", "surne bilbao"]
    },
    # UCAM Murcia
    "murcia": {
        "canonical": "UCAM Murcia",
        "full_name": "Club Baloncesto Murcia",
        "short_name": "UCM",
        "arena": "Palacio de Deportes de Murcia",
        "city": "Murcia",
        "region": "Region of Murcia",
        "capacity": 7454,
        "aliases": ["murcia", "ucam murcia", "cb murcia", "juver murcia", "polaris world murcia", "ucam murcia cb"]
    },
    # CB Breogán
    "breogan": {
        "canonical": "CB Breogán",
        "full_name": "Club Baloncesto Breogán",
        "short_name": "BRE",
        "arena": "Pazo dos Deportes",
        "city": "Lugo",
        "region": "Galicia",
        "capacity": 5310,
        "aliases": ["breogán", "breogan", "cb breogán", "cb breogan", "leche río breogán", "leche rio breogan", "cafés candelas breogán", "río breogán", "rio breogan"]
    },
    # Obradoiro CAB
    "obradoiro": {
        "canonical": "Obradoiro CAB",
        "full_name": "Obradoiro Clube de Amigos do Baloncesto",
        "short_name": "MOB",
        "arena": "Multiusos Fontes do Sar",
        "city": "Santiago de Compostela",
        "region": "Galicia",
        "capacity": 5060,
        "aliases": ["obradoiro", "obradoiro cab", "xacobeo blu:sens", "blusens monbus", "rio natura monbus obradoiro", "monbus obradoiro"]
    },
    # BC Andorra
    "andorra": {
        "canonical": "MoraBanc Andorra",
        "full_name": "Bàsquet Club Andorra",
        "short_name": "MBA",
        "arena": "Poliesportiu d'Andorra",
        "city": "Andorra la Vella",
        "region": "Andorra",
        "capacity": 5005,
        "aliases": ["andorra", "bc andorra", "festina andorra", "morabanc andorra"]
    },
    # Baloncesto Fuenlabrada
    "fuenlabrada": {
        "canonical": "Baloncesto Fuenlabrada",
        "full_name": "Baloncesto Fuenlabrada",
        "short_name": "FUE",
        "arena": "Pabellón Fernando Martín",
        "city": "Fuenlabrada",
        "region": "Community of Madrid",
        "capacity": 5700,
        "aliases": ["fuenlabrada", "baloncesto fuenlabrada", "jabones pardo fuenlabrada", "alta gestión fuenlabrada", "mad-croc fuenlabrada", "montakit fuenlabrada", "urbas fuenlabrada", "carplus fuenlabrada"]
    },
    # Real Betis / CB Sevilla
    "sevilla": {
        "canonical": "Real Betis Baloncesto",
        "full_name": "Real Betis Baloncesto",
        "short_name": "BET",
        "arena": "Palacio Municipal de Deportes San Pablo",
        "city": "Seville",
        "region": "Andalusia",
        "capacity": 7626,
        "aliases": ["sevilla", "cb sevilla", "caja san fernando", "cajasol", "baloncesto sevilla", "coosur real betis", "real betis", "real betis baloncesto"]
    },
    # CB Valladolid
    "valladolid": {
        "canonical": "CB Valladolid",
        "full_name": "Club Baloncesto Valladolid",
        "short_name": "VLL",
        "arena": "Pabellón Polideportivo Pisuerga",
        "city": "Valladolid",
        "region": "Castile and León",
        "capacity": 6800,
        "aliases": ["valladolid", "cb valladolid", "miñón valladolid", "fórum filatélico valladolid", "forum valladolid", "blancos de rueda valladolid"]
    },
    # Bàsquet Girona
    "girona": {
        "canonical": "Bàsquet Girona",
        "full_name": "Bàsquet Girona",
        "short_name": "GIR",
        "arena": "Pavelló Municipal Girona-Fontajau",
        "city": "Girona",
        "region": "Catalonia",
        "capacity": 5500,
        "aliases": ["girona", "bàsquet girona", "valvi girona", "casademont girona", "akasvayu girona", "fiatc girona"]
    },
    # Fundación CB Granada
    "granada": {
        "canonical": "Covirán Granada",
        "full_name": "Fundación Club Baloncesto Granada",
        "short_name": "COV",
        "arena": "Palacio Municipal de Deportes de Granada",
        "city": "Granada",
        "region": "Andalusia",
        "capacity": 9507,
        "aliases": ["granada", "cb granada", "coviran granada", "covirán granada", "oximesa granada"]
    },
    # Gipuzkoa Basket
    "gipuzkoa": {
        "canonical": "Gipuzkoa Basket",
        "full_name": "Donosti Basket Kluba",
        "short_name": "GBC",
        "arena": "Donostia Arena 2016",
        "city": "San Sebastián",
        "region": "Basque Country",
        "capacity": 11000,
        "aliases": ["gipuzkoa", "gipuzkoa basket", "bruesa gbc", "lagun aro gbc", "delteco gbc", "retabet.es gbc"]
    },
    # Palencia Baloncesto
    "palencia": {
        "canonical": "Palencia Baloncesto",
        "full_name": "Palencia Baloncesto",
        "short_name": "ZPA",
        "arena": "Pabellón Municipal de Palencia",
        "city": "Palencia",
        "region": "Castile and León",
        "capacity": 5016,
        "aliases": ["palencia", "palencia baloncesto", "zunder palencia"]
    },
    # Bàsquet Coruña
    "coruna": {
        "canonical": "Básquet Coruña",
        "full_name": "Club Básquet Coruña",
        "short_name": "COR",
        "arena": "Coliseum da Coruña",
        "city": "A Coruña",
        "region": "Galicia",
        "capacity": 9300,
        "aliases": ["coruña", "coruna", "básquet coruña", "leyma coruña", "leyma basquet coruña"]
    },
    # Força Lleida
    "lleida": {
        "canonical": "Força Lleida",
        "full_name": "Força Lleida Club Esportiu",
        "short_name": "LLE",
        "arena": "Pavelló Barris Nord",
        "city": "Lleida",
        "region": "Catalonia",
        "capacity": 6100,
        "aliases": ["lleida", "força lleida", "caprabo lleida", "hiopos lleida", "ce lleida basquetbol", "ilerna lleida", "plus pujol lleida"]
    },
    # CB L'Hospitalet
    "hospitalet": {
        "canonical": "CB L'Hospitalet",
        "full_name": "Club Bàsquet L'Hospitalet",
        "short_name": "HOS",
        "arena": "Complex Esportiu Municipal L'Hospitalet Nord",
        "city": "L'Hospitalet de Llobregat",
        "region": "Catalonia",
        "capacity": 2000,
        "aliases": ["hospitalet", "cb hospitalet", "cb l'hospitalet", "la casera hospitalet"]
    },
    # Cotonificio Badalona / Círcol Catòlic
    "cotonificio": {
        "canonical": "Círcol Catòlic Badalona",
        "full_name": "Círcol Catòlic de Badalona",
        "short_name": "COT",
        "arena": "Pavelló de la Plana",
        "city": "Badalona",
        "region": "Catalonia",
        "capacity": 2500,
        "aliases": ["cotonificio", "cotonificio badalona", "círcol catòlic", "circol catolic", "licor 43"]
    },
    # OAR Ferrol
    "ferrol": {
        "canonical": "OAR Ferrol",
        "full_name": "Club OAR Ferrol",
        "short_name": "FER",
        "arena": "Pavillón Polideportivo A Malata",
        "city": "Ferrol",
        "region": "Galicia",
        "capacity": 5000,
        "aliases": ["ferrol", "oar ferrol", "clesa ferrol", "pescanova ferrol"]
    },
    # Peñas Huesca
    "huesca": {
        "canonical": "CB Peñas Huesca",
        "full_name": "Club Baloncesto Peñas Huesca",
        "short_name": "HUE",
        "arena": "Palacio Municipal de Deportes de Huesca",
        "city": "Huesca",
        "region": "Aragon",
        "capacity": 4900,
        "aliases": ["huesca", "peñas huesca", "magia de huesca", "argal huesca", "somontano huesca"]
    },
    # CB León
    "leon": {
        "canonical": "CB León",
        "full_name": "Club Baloncesto León",
        "short_name": "LEO",
        "arena": "Palacio Municipal de Deportes de León",
        "city": "León",
        "region": "Castile and León",
        "capacity": 5100,
        "aliases": ["león", "leon", "cb león", "cb leon", "elmar león", "baloncesto león"]
    },
    # CB Lucentum Alicante
    "alicante": {
        "canonical": "Lucentum Alicante",
        "full_name": "Club Baloncesto Lucentum Alicante",
        "short_name": "ALI",
        "arena": "Centro de Tecnificación de Alicante",
        "city": "Alicante",
        "region": "Valencian Community",
        "capacity": 5400,
        "aliases": ["alicante", "lucentum alicante", "cb alicante", "etosa alicante", "meridiano alicante"]
    },
    # Menorca Bàsquet
    "menorca": {
        "canonical": "Menorca Bàsquet",
        "full_name": "Menorca Bàsquet",
        "short_name": "MEN",
        "arena": "Pavelló Menorca",
        "city": "Mahón",
        "region": "Balearic Islands",
        "capacity": 5115,
        "aliases": ["menorca", "menorca bàsquet", "iveco menorca", "vivemenorca"]
    },
    # Cantabria Baloncesto
    "cantabria": {
        "canonical": "Cantabria Baloncesto",
        "full_name": "Cantabria Baloncesto",
        "short_name": "CAN",
        "arena": "Palacio de Deportes de Santander",
        "city": "Santander",
        "region": "Cantabria",
        "capacity": 6000,
        "aliases": ["cantabria", "cantabria baloncesto", "lobos cantabria", "cantabria lobos"]
    },
    # Cáceres CB
    "caceres": {
        "canonical": "Cáceres CB",
        "full_name": "Cáceres Club Baloncesto",
        "short_name": "CAC",
        "arena": "Pabellón Multiusos Ciudad de Cáceres",
        "city": "Cáceres",
        "region": "Extremadura",
        "capacity": 6500,
        "aliases": ["cáceres", "caceres", "cáceres cb", "caceres cb"]
    },
    # Club Baloncesto Ourense
    "ourense": {
        "canonical": "Club Ourense Baloncesto",
        "full_name": "Club Ourense Baloncesto",
        "short_name": "OUR",
        "arena": "Pazo dos Deportes Paco Paz",
        "city": "Ourense",
        "region": "Galicia",
        "capacity": 5500,
        "aliases": ["ourense", "orense", "cb ourense", "club ourense baloncesto", "caja ourense"]
    },
    # Gijón Baloncesto
    "gijon": {
        "canonical": "Gijón Baloncesto",
        "full_name": "Gijón Baloncesto",
        "short_name": "GIJ",
        "arena": "Palacio de Deportes de La Guía",
        "city": "Gijón",
        "region": "Asturias",
        "capacity": 5197,
        "aliases": ["gijón", "gijon", "gijón baloncesto", "cabitel gijón"]
    },
    # Collado Villalba
    "villalba": {
        "canonical": "CB Collado Villalba",
        "full_name": "Club Baloncesto Collado Villalba",
        "short_name": "VLB",
        "arena": "Pabellón Municipal de Villalba",
        "city": "Collado Villalba",
        "region": "Community of Madrid",
        "capacity": 4500,
        "aliases": ["villalba", "collado villalba", "cb collado villalba", "atlético madrid villalba", "bancobao villalba"]
    },
    # Askatuak
    "askatuak": {
        "canonical": "Askatuak SBT",
        "full_name": "Askatuak Saski-Baloi Taldea",
        "short_name": "ASK",
        "arena": "Polideportivo José Antonio Gasca",
        "city": "San Sebastián",
        "region": "Basque Country",
        "capacity": 2500,
        "aliases": ["askatuak", "askatuak sbt", "dico's askatuak"]
    },
    # CB Pineda
    "pineda": {
        "canonical": "UDR Pineda",
        "full_name": "Unió Deportiva Recreativa Pineda",
        "short_name": "PIN",
        "arena": "Pavelló Municipal Nino Buscató",
        "city": "Pineda de Mar",
        "region": "Catalonia",
        "capacity": 2000,
        "aliases": ["pineda", "udr pineda", "cb pineda"]
    },
    # CB Mollet
    "mollet": {
        "canonical": "CB Mollet",
        "full_name": "Club Bàsquet Mollet",
        "short_name": "MOL",
        "arena": "Pavelló Municipal Plana Lledó",
        "city": "Mollet del Vallès",
        "region": "Catalonia",
        "capacity": 1500,
        "aliases": ["mollet", "cb mollet"]
    },
    # RC Náutico Tenerife
    "nautico": {
        "canonical": "RC Náutico Tenerife",
        "full_name": "Real Club Náutico de Tenerife",
        "short_name": "NAU",
        "arena": "Pabellón R.C.N.T.",
        "city": "Santa Cruz de Tenerife",
        "region": "Canary Islands",
        "capacity": 2000,
        "aliases": ["náutico", "nautico", "rc náutico", "rc nautico"]
    },
    # Inmobanco / Tempus
    "inmobanco": {
        "canonical": "CB Inmobanco",
        "full_name": "Club Baloncesto Inmobanco",
        "short_name": "INM",
        "arena": "Polideportivo Antonio Magariños",
        "city": "Madrid",
        "region": "Community of Madrid",
        "capacity": 2500,
        "aliases": ["inmobanco", "cb inmobanco", "tempus", "club tempus"]
    },
    # Real Canoe NC
    "canoe": {
        "canonical": "Real Canoe NC",
        "full_name": "Real Canoe Natación Club",
        "short_name": "CAN",
        "arena": "Polideportivo Real Canoe",
        "city": "Madrid",
        "region": "Community of Madrid",
        "capacity": 1500,
        "aliases": ["canoe", "real canoe", "real canoe nc"]
    },
    # CB Llíria
    "lliria": {
        "canonical": "CB Llíria",
        "full_name": "Club Bàsquet Llíria",
        "short_name": "LLI",
        "arena": "Pavelló Pla de l'Arc",
        "city": "Llíria",
        "region": "Valencian Community",
        "capacity": 3500,
        "aliases": ["llíria", "lliria", "cb llíria", "cb lliria", "choleck llíria"]
    },
    # RCD Espanyol
    "espanyol": {
        "canonical": "RCD Espanyol",
        "full_name": "RCD Espanyol Bàsquet",
        "short_name": "ESP",
        "arena": "Palau dels Esports de Barcelona",
        "city": "Barcelona",
        "region": "Catalonia",
        "capacity": 8000,
        "aliases": ["espanyol", "rcd espanyol", "español", "rcd español"]
    },
    # CB Granollers
    "granollers": {
        "canonical": "CB Granollers",
        "full_name": "Club Bàsquet Granollers",
        "short_name": "GRN",
        "arena": "Pavelló Municipal El Tub",
        "city": "Granollers",
        "region": "Catalonia",
        "capacity": 3000,
        "aliases": ["granollers", "cb granollers", "areslux granollers", "grupo ifa granollers", "cacaolat granollers"]
    },
    # CB Santa Coloma
    "santa coloma": {
        "canonical": "CB Santa Coloma",
        "full_name": "Club Bàsquet Santa Coloma",
        "short_name": "SCO",
        "arena": "Pavelló Juan del Moral",
        "city": "Santa Coloma de Gramenet",
        "region": "Catalonia",
        "capacity": 2000,
        "aliases": ["santa coloma", "cb santa coloma", "licor 43 santa coloma"]
    },
    # CB Salamanca
    "salamanca": {
        "canonical": "CB Salamanca",
        "full_name": "Club Baloncesto Salamanca",
        "short_name": "SAL",
        "arena": "Pabellón de Würzburg",
        "city": "Salamanca",
        "region": "Castile and León",
        "capacity": 4000,
        "aliases": ["salamanca", "cb salamanca", "baloncesto salamanca"]
    },
    # CB Ciudad de Huelva
    "huelva": {
        "canonical": "CB Ciudad de Huelva",
        "full_name": "Club Baloncesto Ciudad de Huelva",
        "short_name": "HUE",
        "arena": "Palacio de Deportes de Huelva",
        "city": "Huelva",
        "region": "Andalusia",
        "capacity": 5500,
        "aliases": ["huelva", "ciudad de huelva", "cb ciudad de huelva"]
    },
    # Tenerife CB
    "tenerife cb": {
        "canonical": "Tenerife CB",
        "full_name": "Tenerife Club de Baloncesto",
        "short_name": "TCB",
        "arena": "Pabellón Municipal Pancho Camurria",
        "city": "Santa Cruz de Tenerife",
        "region": "Canary Islands",
        "capacity": 4500,
        "aliases": ["tenerife cb", "unelco tenerife"]
    }
}

def resolve_acb_team(name):
    if not name:
        return "Unknown Team", "Unknown Arena", "Unknown City", "Unknown Region"
    name_clean = name.strip().lower()
    for key, data in ACB_FRANCHISE_MAP.items():
        if name_clean == key or any(alias in name_clean for alias in data["aliases"]):
            return data["canonical"], data["arena"], data["city"], data["region"]
    return name.strip(), "Pabellón Polideportivo", "Spain", "Spain"
