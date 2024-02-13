import os
import random

import numpy as np
import yaml
from place_obj_data import config_obj_Matadata
import omnigibson as og
from omnigibson.macros import gm
from omnigibson.utils.ui_utils import choose_from_options, KeyboardRobotController
from json_parser import json_parsing
# Make sure object states are enabled
gm.ENABLE_OBJECT_STATES = True
gm.USE_GPU_DYNAMICS = True
gm.ENABLE_FLATCACHE = True



def main(random_selection=False, headless=False, short_exec=False):
    """
    Generates a BEHAVIOR Task environment in an online fashion.

    It steps the environment 100 times with random actions sampled from the action space,
    using the Gym interface, resetting it 10 times.
    """
    og.log.info(f"Demo {__file__}\n    " + "*" * 80 + "\n    Description:\n" + main.__doc__ + "*" * 80)

    # Ask the user whether they want online object sampling or not
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
    env = og.Environment(configs=cfg, action_timestep=1/60., physics_timestep=1/60.)

    key, lbia_x, lbia_y, bia_z, rbia_x, rbia_y = config_obj_Matadata()
    obj = env.scene.object_registry("name", key)
    # Get reference to objects in the scene
    aabb_center = obj.aabb_center
    aabb_extent = obj.aabb_extent

    position_x = random.uniform(aabb_center[0] - aabb_extent[0] + lbia_x, aabb_center[0] + aabb_extent[0] - rbia_x)
    position_y = random.uniform(aabb_center[1] - aabb_extent[1] + lbia_y, aabb_center[1] + aabb_extent[1] - rbia_y)
    position_z = aabb_center[2] + aabb_extent[2] - bia_z

    print("*************************************************************")
    print(f"the coordinate of obj is {[position_x,position_y,position_z]}")
    print("*************************************************************")

    extra_obj = env.scene.object_registry("name", "beer_bottle")
    extra_obj.set_position([position_x, position_y, position_z])
    extra_obj.keep_still()


    # Reset the robot
    """robot = env.robots[0]
    robot.set_position([0, 0, 0])
    robot.reset()
    robot.keep_still()"""

    # Take a few steps to let objects settle


    # Choose robot controller to use
    #robot=env.robots[0]
    #robot.set_position([0, 0, 0])

    # Allow user to move camera more easily
    og.sim.enable_viewer_camera_teleoperation()


    # Create teleop controller
    #action_generator = KeyboardRobotController(robot=robot)

    #print out relevant keyboard info
    #action_generator.print_keyboard_teleop_info()

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

