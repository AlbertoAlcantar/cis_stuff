StartingNUM = int(input('starting number of organisms:'))
Average = float(input('average number increase:'))
Days = int(input('number of days to multiply:'))


print('Day Approximate \t Population')
print('---------------------------------')

for DAYS in range (1,Days+1):
    StartingNUM = StartingNUM + (Average * StartingNUM)
    print(DAYS, '\t \t \t \t \t' ,StartingNUM)
