#  Here comes the code!
#  May the force be with you, young padawan!
import os

def money_input():
    money = 0
    value = input("Mennyi pénzzel szeretnéd kezdeni? \n 1. 1000 \n 2. 5000 \n 3. 10000 \n")

    if value == '1':
        money = 1000
    if value == '2':
        money = 5000
    if value == '3':
        money = 10000
   
    return money


def pocket(money):
    print(money)

    


def bet_input():  # $$
    pass


def place_bet():
    pass


def roll_number():
    pass


def check_number():
    pass


def is_winner():
    pass


def main():
    money = money_input()
    os.system('clear')
    print('Money in your pocket: ')
    pocket(money)
    


if __name__ == "__main__":
    main()
