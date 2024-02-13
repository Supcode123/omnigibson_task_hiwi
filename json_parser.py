import json
def json_parsing():
    json_path = "restaurant_brunch_best.json"
    f = open(json_path)
    data = json.load(f)
    #print(data.keys())
    # print(data['state']['object_registry'].keys())
    # print(data['objects_info']['init_info'].keys())
    obj_names = {}
    accepted_categories = set(['bench', 'armchair','coffee_table',
                           'breakfast_table', 'console_table', 'ottoman', 'sofa', 'bar'])
    #categories0 = set(['bench', 'breakfast_table', 'console_table', 'ottoman', 'bar'])

    #'wall_mounted_shelf',
    #'armchair',
    #'sofa'
    for key, value in data['objects_info']['init_info'].items():
        args = value['args']
        if (args['category'] in accepted_categories):
                      obj_names[key] = args['category']
    #print(obj_names)
    return obj_names