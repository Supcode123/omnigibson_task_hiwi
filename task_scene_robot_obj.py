import yaml
import omnigibson as og
from omnigibson.macros import gm
from omnigibson.utils.ui_utils import choose_from_options, KeyboardRobotController

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

    config_filename = "task_Dec.yaml"
    cfg = yaml.load(open(config_filename, "r"), Loader=yaml.FullLoader)

    # Load the environment
    env = og.Environment(configs=cfg, action_timestep=1 / 60., physics_timestep=1 / 60.)

    # Reset the robot
    robot = env.robots[0]
    robot.set_position([0, 0, 0])
    robot.reset()
    robot.keep_still()

    # Choose robot controller to use
    robot=env.robots[0]
    robot.set_position([0, 0, 0])

    # Allow user to move camera more easily
    og.sim.enable_viewer_camera_teleoperation()

    # Create teleop controller
    action_generator = KeyboardRobotController(robot=robot)

    #print out relevant keyboard info
    action_generator.print_keyboard_teleop_info()

    # Other helpful user info
    print("Running demo.")
    print("Press ESC to quit")

    # Loop control until user quits
    max_steps = -1 if not short_exec else 100
    step = 0
    while step != max_steps:
         #action = np.random.uniform(-1, 1, robot.action_dim)
         action = action_generator.get_teleop_action()
         for _ in range(10):

             env.step(action=action)
             step += 1
            # print("action changed")

    # Always close the environment at the end
    env.close()


if __name__ == "__main__":
    main()
