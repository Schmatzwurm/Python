import os

# Variablen
language = "en"

# Dictionary
texts = {
    "de": {
        "menu_title": "SCHMATZTANK BATTLE",
        "play": "SPIELEN",
        "options": "OPTIONEN",
        "quit": "BEENDEN",
        "music": "MUSIK:",
        "fullscreen": "VOLLBILD:",
        "language": "SPRACHE:",
        "back": "ZURÜCK",
        "mainmenu": "HAUPTMENÜ",
        "on": "AN",
        "off": "AUS",
        # ... weitere Texte ...
    },
    "en": {
        "menu_title": "SCHMATZTANK BATTLE",
        "play": "PLAY",
        "options": "OPTIONS",
        "quit": "QUIT",
        "music": "MUSIC:",
        "fullscreen": "FULLSCREEN:",
        "language": "LANGUAGE:",
        "back": "BACK",
        "mainmenu": "MAINMENU",
        "on": "ON",
        "off": "OFF",
        # ... weitere Texte ...
    }
}


def get_res_file_path(file_name):
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    file_path = os.path.join(script_dir, '..', '..', 'resources', file_name)

    return file_path