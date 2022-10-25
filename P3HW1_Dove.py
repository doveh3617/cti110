#CTI-110
#P3HW1 - Debugging
#Hayley Dove
#October 24, 2022
#
#Get grades from each module from user
#This program takes a number grade, determines average and letter grade for average.
#Presents lowest grade, highest grade, sum of grades, average, and letter grade.
#
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]
# TO DO: determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
avg = sum(grades) / len(grades)

# determine letter grade for average

print()
print('------------Results------------')
print(f'Lowest Grade:      {low:.1f}')
print(f'Highest Grade:     {high:.1f}')
print(f'Sum of Grades:     {total:.1f}')
print(f'Average:           {avg:.2f}')
print('---------------------------------------')

if avg >= 90:
    print('Your grade is: A')
else:
    
    if avg >= 80:
        print('Your grade is: B')
    else:
    
        if avg >= 70:
            print('Your grade is: C')
        else:
    
            if avg >= 60:
                print('Your grade is: D')
            else:
                print('Your grade is: F')
