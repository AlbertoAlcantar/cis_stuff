budget = float(input('enter budget for this month: $'))
keep_going = 'y'
expenses= 0
while keep_going == 'y':
    expense= float(input('enter expense: $'))
    expenses += expense
    keep_going=input('more expenses?:yes or no?')
if budget >expenses:
     under_budget= budget -all_expenses
     print('you are under budget.')
     print('$',format(under_budget, '.2f'))
if budget == expenses:
         print('you are in the budget.')



if  expenses > budget:
    over_budget = expenses-budget
    print('you are over your budget.')
    print('-$',format(over_budget, '.2f'))