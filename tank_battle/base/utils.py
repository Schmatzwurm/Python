import os

def get_base_dir():
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)

    return script_dir