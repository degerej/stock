# Joe Degere
# Stock project
# 3/26/2020


from stack import Stack
from queue import Queue
import random


stack = Stack()
queue = Queue()

beginning_balance = 500
balance = beginning_balance
choice = 0
# Stock value
current_value = 30


accounts = int(input('press 1 for FIFO:\n'
                     'press 2 for LIFO:'))

while choice != 4:
    print('Select from the MENU:\n'
          '1. Buy stock\n'
          '2. Sell stock\n'
          '3. Check current stock\n'
          '4. Check profit and losses')
    choice = int(input('>>>'))

    if choice == 1:
        stock_value = random.randint(10, 50)
        print('The stock price is: ' + str(stock_value))
        print('Your balance before purchase: ' + str(balance))
        stocks_bought = int(input('How many stocks would you like to purchase?'))
        cost_of_stock = stock_value
        total_cost = cost_of_stock * stocks_bought

        print('Your purchase: ' + str(total_cost))
        balance -= total_cost
        print('Your new balance: ' + str(balance))


        # FIFO
        if accounts == 1:
            stocks_bought = queue.push(stocks_bought)
            cost_of_stock = queue.push(cost_of_stock)

        # LIFO
        if accounts == 2:
            stocks_bought = stack.push(stocks_bought)
            cost_of_stock = stack.push(cost_of_stock)

    elif choice == 2:
        stock_value = random.randint(10, 50)
        stocks_to_sell = int(input('How many stocks would you like to sell?'))
        profit = stock_value * stocks_to_sell
        print('The total value of stocks sold: ' + str(profit))
        print('Balance before = ' + str(balance))
        balance += profit
        print('Current balance: ', + int(balance))

        if accounts == 1:
            queue.pop()
            queue.pop()

        if accounts == 2:
            stack.pop()
            stack.pop()

    elif choice == 3:
        print('Your balance at the start was: ' + str(beginning_balance))
        print('Your new and current balance is: ' + str(balance))

    elif choice == 4:
        if balance == beginning_balance:
            print('Your balance remains the same at: ' + str(beginning_balance))
        elif balance > beginning_balance:
            print('You have made a profit of: ' + str(beginning_balance + balance))
            print('Your current balance is now: ' + str(balance))
        elif balance < beginning_balance:
            print('Your losses add up to: ' + str(beginning_balance - balance))
            print('Your current balance is now: ' + str(balance))
