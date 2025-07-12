Make it an executable:
"chmod +x my_gripper_control/gripper_control.py" 
Then run this:
colcon build --symlink-install
source install/setup.bash
ros2 run my_gripper_control gripper_control
