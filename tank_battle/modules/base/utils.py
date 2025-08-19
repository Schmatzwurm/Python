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
        "speech": "DEUTSCH",
        "choose language": "SPRACHE WÄHLEN",

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
        "speech": "ENGLISH",
        "choose language": "CHOOSE LANGUAGE",
        # ... weitere Texte ...
    },
    "es": {
        "menu_title": "SCHMATZTANK BATTLE",
        "play": "JUGAR",
        "options": "OPCIONES",
        "quit": "SALIR",
        "music": "MÚSICA:",
        "fullscreen": "PANTALLA COMPLETA:",
        "language": "IDIOMA:",
        "back": "ATRÁS",
        "mainmenu": "MENÚ PRINCIPAL",
        "speech": "ESPAÑOL",
        "choose language": "elegir idioma",
        # ... más textos ...
    },
    "fr": {
        "menu_title": "SCHMATZTANK BATTLE",
        "play": "JOUER",
        "options": "OPTIONS",
        "quit": "QUITTER",
        "music": "MUSIQUE:",
        "fullscreen": "PLEIN ÉCRAN:",
        "language": "LANGUE:",
        "back": "RETOUR",
        "mainmenu": "MENU PRINCIPAL",
        "speech": "FRANÇAIS",
        "choose language": "choisir la langue",
        # ... plus de textes ...
    }
}


def get_res_file_path(file_name):
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    file_path = os.path.join(script_dir, '..', '..', 'resources', file_name)

    return file_path