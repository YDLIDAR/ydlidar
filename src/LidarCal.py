import roslaunch
import rospy
import subprocess
import pyautogui
import threading
from sensor_msgs.msg import LaserScan

def callback(msg):
    print("through")
    distances = msg.ranges
    a_min = msg.angle_min
    a_max = msg.angle_max
    d_min = msg.range_min
    d_max = msg.range_max
    extremes = [a_min, a_max, d_min, d_max]
    rospy.spin()
    return distances, extremes 
    

def scan():
    subprocess.call(["roslaunch", "ydlidar_ros", "G4.launch"])
    return

# node = threading.Thread(target=scan, args=())
# rospy.sleep(3)
rospy.init_node('CalibData')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.sleep(3)
# subprocess.call(["rosnode", "kill","ydlidar_node"])


# print(type(sub))
# print(dir(sub))
# print(id(sub))


print(sub.__str__)