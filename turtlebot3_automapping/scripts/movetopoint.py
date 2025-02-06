import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
import tf.transformations as tf_trans
import math
import time


def publish_goal():
    rospy.init_node('move_robot_goal_node', anonymous=True)
    goal_publisher = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
    rospy.sleep(1)

    goal_msg = PoseStamped()
    goal_msg.header.frame_id = "map"
    goal_msg.header.stamp = rospy.Time.now()
    goal_msg.pose.position.x = 0.0
    goal_msg.pose.position.y = -3.8
    goal_msg.pose.position.z = 0.0

    quaternion = tf_trans.quaternion_from_euler(0.0, 0.0, -1.0 * math.pi / 2)
    goal_msg.pose.orientation.x = quaternion[0]
    goal_msg.pose.orientation.y = quaternion[1]
    goal_msg.pose.orientation.z = quaternion[2]
    goal_msg.pose.orientation.w = quaternion[3]

    rospy.loginfo("Move to position")
    start_time = time.time()
    goal_publisher.publish(goal_msg)

    rospy.Subscriber('/odom', Odometry, odom_callback, callback_args=start_time)

    rospy.spin()


def odom_callback(data, start_time):
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    # rospy.loginfo("Current Position -> x: %.2f, y: %.2f", x, y)

    if abs(x - 0.0) < 0.1 and abs(y - -3.8) < 0.1:
        end_time = time.time()
        duration = end_time - start_time
        rospy.loginfo("Process completed. Duration: %.2f seconds", duration)
        rospy.signal_shutdown("Goal reached")

if __name__ == '__main__':
    try:
        publish_goal()
    except rospy.ROSInterruptException:
        pass
