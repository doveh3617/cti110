#This program will calculate and display travel expenses
#October 8, 2022
#CTI-110 P2HW1 - Travel
#Hayley Dove
#
budget = float(input())
location = input()
gas = float(input())
hotel = float(input())
food = float(input())
total = float(gas + hotel + food)
balance = float(budget - total)
print ('This program calculates and displays travel expenses\n')
print (f'Enter Budget: {budget:.0f}')
print ()
print (f'Enter your travel destination: {location}')
print ()
print (f'How much do you think you will spend on gas? {gas:.0f}')
print ()
print (f'Approximately, how much will you need for acoomodation/hotel? {hotel:.0f}')
print ()
print (f'Last, how much do you need for food? {food:.0f}')
print ()
print ('------------Travel Expenses------------')
print (f'Location:            {location}')
print (f'Initial Budget:      ${budget}')
print (f'Fuel:                ${gas}')
print (f'Accomodation:        ${hotel}')
print (f'Food:                ${food}')
print ('----------------------------------------')
print ()
print (f'Remaining Balance:   ${balance}')
