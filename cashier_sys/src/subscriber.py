import rospy
from cashier_sys.msg import bill
from cashier_sys.srv import update

inventory_param = '/inventory'
income_param = '/income'

inventory = 1000
income = 0
initial_inventory = 1000
initial_income = 0

def bill_callback(bill):
    quantity = bill.quantity
    price = bill.price

    rospy.wait_for_service('/update')
    update_proxy = rospy.ServiceProxy('/update',update)
    response = update_proxy(quantity, price)
    if response.success:
        rospy.loginfo("Parameters updated.")

def update_param(request):
    inventory = rospy.get_param(inventory_param, 1000)  
    income = rospy.get_param(income_param, 0)
    change_in_inventory = request.quantity
    change_in_income = request.quantity * request.price
    rospy.set_param(inventory_param, inventory - change_in_inventory)
    rospy.set_param(income_param, income + change_in_income)
    return 'updated'


def subscriber():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('bill_topic', bill, bill_callback)
    rospy.Service('update', update, update_param)
    rospy.spin()


if __name__ == '__main__':
    try:
        rospy.set_param('/inventory', initial_inventory)
        rospy.set_param('/income', initial_income)
        subscriber()
    except rospy.ROSInterruptException:
        pass
     