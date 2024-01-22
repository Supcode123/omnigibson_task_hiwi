import json

json_path = "/home/kunzhi/datasets/datasets/og_dataset/scenes/restaurant_brunch/json/restaurant_brunch_best.json"

f = open(json_path)
data = json.load(f)
print(data.keys())
# print(data['state']['object_registry'].keys())
# print(data['objects_info']['init_info'].keys())
accepted_categories = set(['bench', 'wall_mounted_shelf', 'armchair',
                       'breakfast_table', 'console_table', 'ottoman', 'sofa', 'bar'])
for key, value in data['objects_info']['init_info'].items():
    args = value['args']
    if (args['category'] in accepted_categories):
        print(key, args['category'])