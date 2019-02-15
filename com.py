keep_going = 'y'

while keep_going == 'y':
    sales = float(input('please enter sales'))
    comm_rate = float(input('please enter rate'))
    commission = sales * comm_rate
    print('commission is', commission)
    keep_going = input('another? (y for yes)')