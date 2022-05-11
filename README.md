# UoS-Agility-Robot
The ROS2 and Gazebo project for the Agility Robot. Developed by the University of Surrey. <br />
<br />
Create a new directory/workspace called "robot_description_ws". 

# INSTALL THESE VERSIONS
gazebo11 <br />
Ros2-Foxy <br />
Python 3.8.10 <br />
C++14 <br />
# Required packages alongside the base installations
gazebo_ros_pkgs <br />
https://github.com/ros-simulation/gazebo_ros_pkgs <br />
<br />
Wiki for the packages if required <br />
https://github.com/ros-simulation/gazebo_ros_pkgs/wiki <br />


# CLONE THE GITHUB REPOSITORY ONTO YOUR SYSTEM 
Navigate to "robot_description_ws" and clone the repository. <br />
# Ensure the absolute paths to CAD models are correct.
These files need to be updated:  <br /> Robot SDF (sdf/upgradedrobot) <br /> World file (worlds/robot_track.world). <br />
<br />
/home/"username"/CAD/upgradedrobot/"part name".dae <br />
The "username" depends on your personal system and where you have cloned the repository. It needs to be changed for all paths inside the specified files. Search for instances of "shea" and change it to the new abolute path. <br />
The part name will be correct and doesnt need to be changed, they correspond to a .dae file located in the "CAD" directory. <br />
<br />
<br />
Example : /home/Saber/robot_description_ws/CAD/upgradedrobot/chassisbox.dae

# New Terminal:SIMULATION SETUP AND BUILDING
source /opt/ros/foxy/setup.bash <br />
<br />
cd robot_description_ws <br />
<br />
colcon build <br />

# New Terminal: SOURCE ROS2 AND THE PACKAGE FROM THE WORKSPACE
cd robot_description_ws <br />
<br />
source /opt/ros/foxy/setup.bash <br />
<br />
. install/local_setup.bash <br />

# LAUNCH THE SIMULATION
ros2 launch agilityrobot_description agilityrobot.launch.py <br />
<br />
Unpause the Gazebo Simulator.



# New Terminal : CONTROL THE SIMULATION WITH "teleop_keyboard"

source /opt/ros/foxy/setup.bash <br />
<br />
ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=agilityrobot/cmd_vel <br />
<br />

Now the front wheels can be drive using the keyboard on the agillityrobot/cmd_vel topic. <br />
<br />
The terminal is used to control the robot needs to be the selected window when controlling the robot. Move the gazebo screen such that its seen but not the primary selected window on your desktop. <br />





# EXTRA TIPS
<br />
My disseratation has an in-depth account of the progress made for the project's first year of development. It also reports on the improvements intended for the project. <br />
<br />
For WSL2 Users. NOT APPLICABLE FOR LINUX USERS. <br />
Make sure to have a connected GUI interface sourced in every terminal <br />
Xlaunch <br />
<br />
export DISPLAY="`grep nameserver /etc/resolv.conf | sed 's/nameserver //'`:0" <br />

