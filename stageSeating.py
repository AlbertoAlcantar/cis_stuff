def main ():
    classA= float(input('how many seats were sold for class A?:'))
    classB= float(input('how many seats were sold for class B?:'))
    classC= float(input('how many seats were sold for class C?:'))
    totalA(classA)
    totalB(classB)
    totalC(classC)

def totalA(classA):
    profitA=classA*20
    print('class A profit $', format(profitA, '.2f'))

def totalB(classB):
    profitB= classB*15
    print('class B profit $', format(profitB, '.2f'))

def totalC(classC):
    profitC= classC*10
    print('class C profit $', format(profitC, '.2f'))




main()







