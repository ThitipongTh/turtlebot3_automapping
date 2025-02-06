# Turtlebot3 Auto Mapping
## Installation
```
cd ~/catkin_ws/src
git clone https://github.com/ThitipongTh/turtlebot3_automapping.git
cd ~/catkin_ws
catkin_make
source ~/catkin_ws/devel/setup.bash
```
## Requirement Package
```
sudo apt install -y ros-noetic-slam-gmapping ros-noetic-map-server ros-noetic-amcl \
                    ros-noetic-move-base ros-noetic-navigation
cd ~/catkin_ws/src
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
git clone -b https://github.com/hrnr/m-explore.git
cd ~/catkin_ws
catkin_make
```
## Reference Package
- [Turtlebot3](https://github.com/ROBOTIS-GIT/turtlebot3)
- [Turtlebot3 Simulation](https://github.com/ROBOTIS-GIT/turtlebot3_simulations)
- [Turtlebot3 Message](https://github.com/ROBOTIS-GIT/turtlebot3_msgs)
- [Exploration Lite](https://github.com/hrnr/m-explore)