import json
def json_parsing(json_path):
    """
    to parse the json file of the Scene, and get the metadata of its objects.

    Args:
        json_path (str): the path of JSON_file

    Returns:
        dict: includes all objects in the desired catogories.
    """

    f = open(json_path)
    data = json.load(f)
    obj_names = {}
    accepted_categories = set(['bench', 'armchair','coffee_table',
                           'breakfast_table', 'console_table', 'ottoman', 'sofa', 'bar'])

    for key, value in data['objects_info']['init_info'].items():
        args = value['args']
        if (args['category'] in accepted_categories):
                      obj_names[key] = args['category']
    del obj_names["bench_kpeeai_0"]  #obj cannot be placed on bench_kpeeai_0 because unknown bugs

    return obj_names