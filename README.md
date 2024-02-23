# Robot Simulation besed on Omnigibson_Plattform

## installation & tutorial
[OmniGibson Documentation](https://behavior.stanford.edu/omnigibson/) 

[GitHub code source](https://github.com/StanfordVL/OmniGibson)

## tasks introduction
- main tasks
  - task_scene_robot_obj.py: generates a BEHAVIOR Task environment, also include one restaurant_brunch scene, robot and extra obj. 
  - obj_load_placement.py: generates a restaurant_brunch scene and load extra objects, place them on the desired furnitures.
    - json_parser.py: to parse the json file of the scene, and get the metadata of its objects.
    - place_obj_data.py: generate the coordinate data to have fine-tuning on the coordinate range of obj to be placed.
- restaurant_brunch_best.json: json file which contain metadatas of all the prebuild objs in this restaurant_brunch scene.
- yaml files:
  - task_Dec.yaml: yaml file includes Task, Scene, Robot, Objects to load.
  - obj_LodeWithoutTask.yaml: yaml files include only Scene and Objs for simpler version to load.
  
## pointers
- Remind：launch the shell script (sudo ./run_docker.sh -h <ABS_DATA_PATH>) first after opening the terminal.
- pre-built data-location
  - defined-activities location: /home/Administrator/OmniGibson/venv/lib/python3.7/site-packages/bddl/activity_definitions
  - defined-scenes location: /home/Administrator/datasets/datasets/og_dataset/scenes
  - objects Location: /home/Administrator/datasets/datasets/og_dataset/objects
- Notice: when there is no corresponding json file would occur  ” NO File/ Dictionary”  error.
  (eg. /home/Administrator/datasets/datasets/og_dataset/scenes/restaurant_brunch/json)
