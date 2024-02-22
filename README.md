# Hiwi task besed on Omnigibson_Plattform

## installation
[OmniGibson Documentation](https://behavior.stanford.edu/omnigibson/) 

[GitHub code source](https://github.com/StanfordVL/OmniGibson)

## tasks introduction
- main tasks
  - task_scene_robot_obj: Generates a BEHAVIOR Task environment，also include one restaurant_brunch scene, robot and extra obj. 
  - obj_load_placement: Generates a restaurant_brunch scene and load extra objects, place them on the desired furnitures.
    - json_parser: to parse the json file of the Scene, and get the metadata of its objects.
    - place_obj_data: Generate the coordinate data to have fine-tuning on the coordinate range of obj to be placed.
- restaurant_brunch_best: json file which contain metadatas of all the prebuild objs in this restaurant_brunch scene.
- yaml files:
  - task_Dec: yaml file includes Task, scene, Robot, objects to load.
  - obj_LodeWithoutTask: yaml files include only scene and objs for simpler version to load.
  
## pointers
- Remind：launch the shell script (sudo ./run_docker.sh -h <ABS_DATA_PATH>) first when open the terminal.
- pre-built data-location
  - defined-activities location: /home/Administrator/OmniGibson/venv/lib/python3.7/site-packages/bddl/activity_definitions
  - defined-scenes location: /home/Administrator/datasets/datasets/og_dataset/scenes
  - objects Location: /home/Administrator/datasets/datasets/og_dataset/objects
- Notice: when there is no corresponding json file would occur  ” NO File/ Dictionary”  error.
  (eg. /home/Administrator/datasets/datasets/og_dataset/scenes/restaurant_brunch/json)
