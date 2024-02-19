import os
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
    TODO:get the coordinates of added obj to place it on furniture right
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
    Generates a BEHAVIOR Task environment in an online fashion.

    It steps the environment 100 times with random actions sampled from the action space,
    using the Gym interface, resetting it 10 times.
    """
    og.log.info(f"Demo {__file__}\n    " + "*" * 80 + "\n    Description:\n" + main.__doc__ + "*" * 80)

    """print("1.Loding with Task;")
    print("2.Loding without Task;")
    choose = input()
    if (choose == "1"):
        config_filename = "task_Dec.yaml"
    elif(choose == "2"):
        config_filename = "obj_LodeWithoutTask.yaml"
        """

    config_filename = "obj_LodeWithoutTask.yaml"
    cfg = yaml.load(open(config_filename, "r"), Loader=yaml.FullLoader)

    # Load the environment
    env = og.Environment(configs=cfg, action_timestep=1 / 60., physics_timestep=1 / 60.)

    furniture_obj = json_parsing()
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
            obj = env.scene.object_registry("name", furniture_name)
            extra_obj = env.scene.object_registry("name", obj_i["name"])
            print(f"the added object is {obj_i['name']}")
            position_x, position_y, position_z = object_place(obj, lbia_x, lbia_y, bia_z, rbia_x, rbia_y)
            extra_obj.set_position([position_x, position_y, position_z])
            extra_obj.keep_still()
            time.sleep(2)
            position_after_place = extra_obj.get_position()
            print(f"the z_positon of added obj after placing is: {position_after_place[2]}")
            TAG = success_fail_cal(position_z, position_after_place[2])
            if (TAG):
                success_count += 1
            else:
                fail_count += 1
            iter_ += 1
            iter_times += 1
    print(f"the total placement times is: {iter_times}, the success times is: {success_count}, the fail times: is {fail_count}")

    # <compute success and failure for furniture_name, object>

    # Reset the robot
    """robot = env.robots[0]
    robot.set_position([0, 0, 0])
    robot.reset()
    robot.keep_still()"""

    ## Choose robot controller to use
    # robot=env.robots[0]
    # robot.set_position([0, 0, 0])

    # Allow user to move camera more easily
    og.sim.enable_viewer_camera_teleoperation()

    ## Create teleop controller
    # action_generator = KeyboardRobotController(robot=robot)

    ##print out relevant keyboard info
    # action_generator.print_keyboard_teleop_info()

    # Other helpful user info
    print("Running demo.")
    print("Press ESC to quit")

    # Loop control until user quits
    """max_steps = -1 if not short_exec else 100
    step = 0
    while step != max_steps:
         #action = np.random.uniform(-1, 1, robot.action_dim)
         action = action_generator.get_teleop_action()
         for _ in range(10):

             env.step(action=action)
             step += 1
            # print("action changed")
"""
    # Step through the environment
    max_steps = 100 if short_exec else 10000
    for i in range(max_steps):
        env.step(np.array([]))
    # Always close the environment at the end
    env.close()


if __name__ == "__main__":
    main()
