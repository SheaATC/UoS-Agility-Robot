# INSTALL THESE VERSIONS
gazebo11
Ros2-Foxy 
Python 3.8.10
C++14
# Required packages alongside the base installations
gazebo_ros_pkgs
https://github.com/ros-simulation/gazebo_ros_pkgs
https://github.com/ros-simulation/gazebo_ros_pkgs/wiki


# CLONE THE GITHUB REPOSITORY ONTO YOUR SYSTEM 

# SETUP SIMULATION
# Source the ros2 environment. 
source /opt/ros/foxy/setup.bash

# Move to the Workspace.
cd robot_description_ws

# Ensure the absolute path to CAD models are correct in the robot SDF (sdf/upgradedrobot) and world file (worlds/robot_track.world).
/home/"username"/CAD/upgradedrobot/"part name".dae
# The username depends on your personal system so it may need to be changed for all paths. Search for instances of "shea" and change it accordingly.
# The part name will be correct and doesnt need to be changed, they correspond to a .dae file located in the "CAD" directory.

# Build the agilityrobot_description package for the first time.
colcon build

# Open a new terminal, source ros2 and the package in the workspace.
cd robot_description_ws
source /opt/ros/foxy/setup.bash
. install/local_setup.bash

# Launch the simulation
ros2 launch agilityrobot_description agilityrobot.launch.py

# Un-pause gazebo

# CONTROLLNG THE SIMULATION

# run this command in another terminal to control the robot with the keyboard in tandem with the differential drive plugin.
source /opt/ros/foxy/setup.bash

ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=agilityrobot/cmd_vel
# Now the front wheels can be drive using the keyboard on the agillityrobot/cmd_vel topic
# The terminal used to control the robot needs to be the selected window when controlling the robot. Move the gazebo screen such that its seen but not the primary window on your desktop.





# EXTRA TIPS

For WSL2 Users. NOT APPLICABLE FOR LINUX USERS.
# Make sure to have a connected GUI interface sourced in every terminal
Xlaunch
export DISPLAY="`grep nameserver /etc/resolv.conf | sed 's/nameserver //'`:0"
