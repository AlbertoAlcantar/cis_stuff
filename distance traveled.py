mph = int(input('please enter mph:'))
time = int (input('please enter time traveled:'))
print('hours\tmiles')
for hour in range (1,time+1):
   print(hour, '\t\t',  mph*hour )

