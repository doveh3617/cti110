#This program will calculate and display travel expenses
#September 22, 2022
#CTI-110 P1HW2 - Travel Expense
#Hayley Dove
#
budget = int(input())
location = (input)
gas = int(input())
hotel = int(input())
food = int(input())
total = int(gas + hotel + food)
balance = int(budget - total)
print ('This program calculates and displays travel expenses\n')
print ('Enter Budget:', budget)
print ()
print ('Enter your travel destination:', location)
print ()
print ('How much do you think you will spend on gas?', gas)
print ()
print ('Approximately, how much will you need for acoomodation/hotel?', hotel)
print ()
print ('Last, how much do you need for food?', food)
print ()
print ('------------Travel Expenses------------')
print ('Location:', location)
print ('Initial Budget:', budget)
print ()
print ('Fuel:', gas)
print ('Accomodation:', hotel)
print ('Food:', food)
print ()
print ('Remaining Balance:', balance)


