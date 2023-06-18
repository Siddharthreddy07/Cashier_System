import rospy
from cashier_sys.msg import bill

def main():
    pub = rospy.Publisher('bill_topic', bill, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(10)
    bill_number = 1
    while not rospy.is_shutdown():
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        bill_msg = bill()
        bill_msg.bill_number = bill_number
        bill_number += 1
        bill_msg.timestamp = rospy.get_time()
        bill_msg.quantity = quantity
        bill_msg.price = price
        bill_msg.total = bill_msg.quantity * bill_msg.price
        pub.publish(bill_msg)
        rate.sleep()

            
if __name__ == '__main__':
    initial_inventory = 1000
    initial_income = 0
    try:
        rospy.set_param('/inventory', initial_inventory)
        rospy.set_param('/income', initial_income)
        main()
    except rospy.ROSInterruptException:
        pass