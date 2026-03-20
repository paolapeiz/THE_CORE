RPG_ALIASES = {
    "abyssinian": "Felino del desierto",
    "american_bulldog": "Guardián pesado",
    "bengal": "Cazador sigiloso",
    "boxer": "Luchador de arena",
    "chihuahua": "Explorador pequeño",
    "egyptian_mau": "Gato místico",
    "great_pyrenees": "Tanque sagrado",
    "maine_coon": "Bestia nevada",
    "pomeranian": "Familiar mágico",
    "saint_bernard": "Guardián alpino",
}

def get_rpg_alias(label_name):
    return RPG_ALIASES.get(label_name, f"Criatura {label_name}")