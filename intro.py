keep_going = 'y'

while keep_going == 'y':
    number_1 = int(input ('please enter number 1:'))
    number_2 = int(input ('please enter number 2:'))
    the_sum = number_1 + number_2
    print('the sum is',the_sum)
    keep_going = input('another? (y for yes)')

