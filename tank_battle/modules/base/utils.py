import os

def get_res_file_path(file_name):
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    file_path = os.path.join(script_dir, '..', '..', 'resources', file_name)

    return file_path