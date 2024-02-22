import random
import time

from json_parser import json_parsing
import numpy as np
import yaml
from place_obj_data import config_obj_Matadata
import omnigibson as og
from omnigibson.macros import gm
from omnigibson.utils.ui_utils import choose_from_options, KeyboardRobotController

# Make sure object states are enabled
gm.ENABLE_OBJECT_STATES = True
gm.USE_GPU_DYNAMICS = False
gm.ENABLE_FLATCACHE = True


def object_place(obj, lbia_x, lbia_y, bia_z, rbia_x, rbia_y):
    """
    get the coordinates of added obj to place it on furniture right

    Args:
        obj(None):furniture in the object_registry
        lbia_x, lbia_y, bia_z, rbia_x, rbia_y (float): tolerance of the bounding_box on each direction of its border

     Returns:
         float:
         random appropriate x,y,z place_coordinate of intended obj
    """
    # Get reference to objects in the scene
    aabb_center = obj.aabb_center
    aabb_extent = obj.aabb_extent

    position_x = random.uniform(aabb_center[0] - aabb_extent[0] + lbia_x, aabb_center[0] + aabb_extent[0] - rbia_x)
    position_y = random.uniform(aabb_center[1] - aabb_extent[1] + lbia_y, aabb_center[1] + aabb_extent[1] - rbia_y)
    position_z = aabb_center[2] + aabb_extent[2] - bia_z

    print(f"the coordinate of obj is {[position_x, position_y, position_z]}")
    return position_x, position_y, position_z


def success_fail_cal(position_z, param):
    """
    calculate the success or fail of the task

    Args:
        position_z(float): desired obj coordinate by z_axis
        param(float): real obj coordinate by z_axis after placing

    Return:
        (bool): success or fail
    """
    if (abs(position_z - param) < 0.10):
        print("success!")
        return True
    else:
        print("-------")
        print("|fail!|")
        print("-------")
        return False


def main(random_selection=False, headless=False, short_exec=False):
    """
    Generates a restaurant_brunch scene and load extra objects,
    place them on the desired furnitures.
    """
    og.log.info(f"Demo {__file__}\n    " + "*" * 80 + "\n    Description:\n" + main.__doc__ + "*" * 80)

    config_filename = "obj_LodeWithoutTask.yaml"
    cfg = yaml.load(open(config_filename, "r"), Loader=yaml.FullLoader)

    # Load the environment
    env = og.Environment(configs=cfg, action_timestep=1 / 60., physics_timestep=1 / 60.)

    json_path = "restaurant_brunch_best.json"
    furniture_obj = json_parsing(json_path)

    obj_list = cfg["objects"]
    print("1:choose furniture rondomly")
    print("2:furniture traverse ")
    mode_i = input()
    if (mode_i == "1"):
        flag = True
    elif (mode_i == "2"):
        flag = False

    iter_times = 0
    success_count = fail_count = 0
    for obj_i in obj_list:
        iter_ = 0
        for f_i in range(len(furniture_obj)):
            furniture_name, lbia_x, lbia_y, bia_z, rbia_x, rbia_y = config_obj_Matadata(iter_, flag)
            # import pdb; pdb.set_trace()
            # Grab the object references
            obj = env.scene.object_registry("name", furniture_name)
            extra_obj = env.scene.object_registry("name", obj_i["name"])
            print(f"the added object is {obj_i['name']}")
            position_x, position_y, position_z = object_place(obj, lbia_x, lbia_y, bia_z, rbia_x, rbia_y)
            # Place the object
            extra_obj.set_position([position_x, position_y, position_z])
            extra_obj.keep_still()
            time.sleep(2)
            # Get the coordinate of object after placing
            position_after_place = extra_obj.get_position()
            print(f"the z_positon of added obj after placing is: {position_after_place[2]}")
            # compute success and failure times
            TAG = success_fail_cal(position_z, position_after_place[2])
            if (TAG):
                success_count += 1
            else:
                fail_count += 1
            iter_ += 1
            iter_times += 1
    print(f"the total placement times is: {iter_times}, the success times is: {success_count}, the fail times: is {fail_count}")


    # Allow user to move camera more easily
    og.sim.enable_viewer_camera_teleoperation()

    # Other helpful user info
    print("Running demo.")
    print("Press ESC to quit")

    # Step through the environment
    max_steps = 100 if short_exec else 10000
    for i in range(max_steps):
        env.step(np.array([]))
    # Always close the environment at the end
    env.close()


if __name__ == "__main__":
    main()
