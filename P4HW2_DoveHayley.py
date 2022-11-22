# CTI-110
# P4HW2-Salary Calculator
# Hayley Dove
# November 13, 2022
#
#
# Program takes employee name, hours worked, and pay rate as input
# Program calculates overtime and total pay
# Program displays employee pay information in a table and displays all employee pay information once loop is completed
#
numOfEmp = 0               # holds total employees entered
totalOverTimePay = 0       # holds total over time pay for all employees
totalRegPay = 0            # holds total regular pay for all employees
totalGrossPay = 0          # holds total gross pay for all employees

# loop until user opts to exit
while True:
    
    # enter employee's name, hours worked, and pay rate
    name = input("Enter employee's name or \"None\" to terminate: ")
    
    # if name is "None", break the loop without any further input
    if name == "None":
        break
    else:
        
        # if employee name is entered then increase employee count by 1
        numOfEmp += 1
    
    hours = float(input("How many hours did " + name + " worked? "))
    rate = float(input("What did " + name + "\' pay rate? "))
    
    # now set variables to calculate values for employee
    overtime = 0
    overtimePay = 0
    regularPay = 0
    grossPay = 0
    
    # now, check if number of worked hours are greater than 40
    if hours > 40:
        
        # then calculate overtime
        overtime = hours - 40
        
        # calculate over time Pay(50% more)
        overtimePay = overtime * rate * 1.5
        
        # calculate regular pay
        regularPay = 40*rate
        
        # calculate gross Pay
        grossPay = regularPay + overtimePay
    else:
        
        # otherwise, simply calculate regular Pay and gross pay
        regularPay = hours*rate
        grossPay = regularPay
    
    # add over time pay to total over time pay
    totalOverTimePay += overtimePay
    
    # add regular pay to total regular pay
    totalRegPay += regularPay
    
    # add gross pay to total gross pay
    totalGrossPay += grossPay
    
    # print employee name
    print("\nEmployee name: " + name + "\n")
    
    # print all the above calculated values in a table
    print(f"{'Hours Worked':<20}{'Pay Rate':<20}{'Overtime':<20}{'Overtime Pay':<20}{'RegHour Pay':<20}{'Gross Pay':<20}")
    print('-------------------------------------------------------------------------------------------------------------')
    print(f'{hours:<20.1f}{rate:<20.1f}{overtime:<20.1f}${overtimePay:<20.2f}${regularPay:<19.2f}${grossPay:<20.2f}')
    print()

# once the loop terminates, print number of employees entered, total over time pay, total regular pay, and total gross pay
print()
print('Total number of employees entered:', numOfEmp)
print(f'Total amount payed for over time: ${totalOverTimePay:.2f}')
print(f'Total amount payed for regular hours: ${totalRegPay:.2f}')
print(f'Total amount payed in gross: ${totalGrossPay:.2f}')
