#CTI-110
#P3HW2 - Salary
#Hayley Dove
#October 28, 2022
#
#Get name, hours worked, and pay rate from user
#Calculate overtime, overtime pay, regular hour pay, and gross pay
#Display hour and pay information based on input along with user's name
#
Name = input('Enter employee\'s name:')
Hours = float(input('Enter number of hours worked:'))
Pay = float(input('Enter employee\'s pay rate:'))
print('---------------------------------------')
print('Employee name:    ', Name)
print()
if Hours < 40:
    RegHourPay = Pay * Hours
    GrossPay = RegHourPay
    OverTime = 0
    OverTime_Pay = 0
else:
        RegHourPay = Pay * 40
        OverTime = Hours - 40
        OverTimeRate = Pay * 1.5
        OverTime_Pay = OverTime * OverTimeRate
        GrossPay = RegHourPay + OverTime_Pay
print('Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHourPay   Gross Pay')
print('------------------------------------------------------------------------------')
print(f'{Hours:<15.1f}{Pay:<13.2f}{OverTime:<13.1f}{OverTime_Pay:<12.2f}{RegHourPay:<13.2f}{GrossPay:.2f}')
