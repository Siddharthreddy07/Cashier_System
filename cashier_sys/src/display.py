import rospy
from cashier_sys.msg import bill

def bill_callback(data):
    inventory=rospy.get_param('/inventory')
    income=rospy.get_param('/income')
    rospy.loginfo(data)
    rospy.loginfo("Inventory: %d",inventory)
    rospy.loginfo("Income: %d",income)
    
def display():
    rospy.init_node('display', anonymous=True)  
    rospy.Subscriber("bill_topic", bill, bill_callback)

    rospy.spin()

if __name__ == '__main__':
    initial_inventory = 1000
    initial_income = 0
    try:
        rospy.set_param('/inventory', initial_inventory)
        rospy.set_param('/income', initial_income)
        display()
    except rospy.ROSInterruptException:
        pass