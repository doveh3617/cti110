# Program generates random math problems, user must enter their guess
# If the answer is wrong, program tells user if it is too high or low
# If the answer is correct, program congratulates user and returns to main menu
# November 27, 2022
# CTI-110 P5HW2-Math Quiz
# Hayley Dove
#
import random


def addRandom():
        a=random.randint(0,1000)
        b=random.randint(0,1000)
        print(f' {a}')
        print(f'+{b}')
        print('Enter answer')
        ans=int(input())
        total = 1
        while ans!=(a+b):
        
                
                if ans<(a+b):
                        print('Sorry, guess is too low.')
                        total = total + 1
                else:
                        print('Sorry, guess is too high.')
                        total = total + 1

                ans=int(input('try again : '))
        print('Congratulations!!!! your answer is correct..')
        print('Number of guesses:', total)
        print()

def subRandom():
        a=random.randint(0,1000)
        b=random.randint(0,1000)
        print(f' {a}')
        print(f'-{b}')
        print('Enter answer')
        ans=int(input())
        total = 1
        while ans!=(a-b):
        
                
                if ans<(a-b):
                        print('Sorry, guess is too low.')
                        total = total + 1
                else:
                        print('Sorry, guess is too high.')
                        total = total + 1
                        
                ans=int(input('try again : '))
        print('Congratulations!!!! your answer is correct..')
        print('Number of guesses:', total)
        print()
        
def main():
    print('Welcome to Math Quiz\n')

    while True:

        print('MAIN MENU')
        print('----------------------')
        print('1) Add Random Numbers ')
        print('2) Subtract Random Numbers')
        print('3) Exit\n')
        num=int(input('Please choose one of the menu options: '))
                
        if num == 1:
            addRandom()
        elif num == 2:
            subRandom()
        elif num == 3:
            print('Thank you for playing...')
            print('Bye!!')
            break
main()
