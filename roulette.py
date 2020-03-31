from termcolor import colored, cprint


def money_input():
    pass


def pocket():
    pass


def bet_input(pocket):
    minimum = 5
    available_money = pocket
    betting = True
    while betting:
        print(available_money)
        try:
            if pocket >= minimum:
                print('Minimum bet is 5€')
                amount = int(input('\nPlace your bets: '))
                if amount < minimum:
                    print('The minimum is 5€')
                else:
                    available_money -= amount
                    return amount
            else:
                print('You don\'t have enough money!')
                betting = False
        except ValueError:
            print('Please enter valid amount!')


def bet_again(pocket):
    while True:
        new_bet = input('Do you want to place a new bet?(Y/N) ').lower()
        if new_bet == 'y' or new_bet == 'yes':
            bet_input(pocket)
        elif new_bet == 'n' or new_bet == 'no':
            place_bet()
        else:
            print('Invalid input!')


def place_bet(bet_amount, options, number_colors):
    cprint('Options: ', attrs=['bold'])
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nWhat do you want to place your bet on?', attrs=['bold'])
    while True:
        try:
            bet_type = input().lower()
            if bet_type == '1' or bet_type == 'numbers':
                bet_on_numbers(number_colors)
            elif bet_type == '2' or bet_type == 'dozens':
                bet_on_dozens()
            elif bet_type == '3' or bet_type == 'rows':
                bet_on_rows()
            elif bet_type == '4' or bet_type == 'red or black':
                bet_on_color()
            elif bet_type == '5' or bet_type == 'odd or even':
                bet_on_odd_even()
            elif bet_type == '6' or bet_type == 'low or high':
                bet_on_low_high()
            else:
                print('Wrong input! Choose from the options!')
        except ValueError:
            print('Wrong input! Choose from the options!')


def bet_on_numbers(number_colors):
    valid_numbers = {}
    for i, color in enumerate(number_colors):
        valid_numbers[i] = color
    while True:
        try:
            number = int(input('Choose a number between 0 - 36: '))
            if number not in valid_numbers:
                print('Enter a valid number!')
            else:
                return number
        except ValueError:
            print('Please enter valid number!')


def bet_on_dozens():
    length = 12
    options = ['1st12', '2nd12', '3rd12']
    cprint('Choose from below: ', attrs=['bold'])
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nChoose the dozen you want to bet on!', attrs=['bold'])
    while True:
        try:
            bet_type = input()
            if bet_type == '1' or bet_type == '1st12':
                first_twelve = [i for i in range(1, length+1)]
                return first_twelve
            elif bet_type == '2' or bet_type == '2nd12':
                second_twelve = [i for i in range(length, (length*2)+1)]
                return second_twelve
            elif bet_type == '3' or bet_type == '3rd12':
                third_twelve = [nums for nums in range((length*2), (length*3)+1)]
                return third_twelve
            else:
                print('Wrong input! Choose from the options!')
        except ValueError:
            print('Wrong input! Choose from the options!')


def bet_on_rows():
    options = ['Upper', 'Middle', 'Lower']
    cprint('Choose from below: ', attrs=['bold'])
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nChoose the row you want to bet on!', attrs=['bold'])
    while True:
        try:
            bet_type = input().lower()
            if bet_type == '1' or bet_type == 'Upper':
                dernier = [i for i in range(1, 37) if i % 3 == 0]
                return dernier
            elif bet_type == '2' or bet_type == 'Middle':
                moyen = [i for i in range(1, 37) if i % 3 == 2]
                return moyen
            elif bet_type == '3' or bet_type == 'Lower':
                premier = [i for i in range(1, 37) if i % 3 == 1]
                return premier
            else:
                print('Wrong input! Choose from the options!')
        except ValueError:
            print('Wrong input! Choose from the options!')


def bet_on_color():
    options = ['Red', 'Black']
    cprint('Choose from below: ', attrs=['bold'])
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nChoose the color you want to bet on!', attrs=['bold'])
    while True:
        try:
            bet_type = input().lower()
            if bet_type == '1' or bet_type == 'Red':
                return bet_type
            elif bet_type == '2' or bet_type == 'Black':
                return bet_type
            else:
                print('Wrong input! Choose from the options!')
        except ValueError:
            print('Wrong input! Choose from the options!')


def bet_on_odd_even():
    options = ['Odd', 'Even']
    cprint('Choose from below: ', attrs=['bold'])
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nChoose which one you want to bet on!', attrs=['bold'])
    while True:
        try:
            bet_type = input().lower()
            if bet_type == '1' or bet_type == 'Odd':
                return bet_type
            elif bet_type == '2' or bet_type == 'Even':
                return bet_type
            else:
                print('Wrong input! Choose from the options!')
        except ValueError:
            print('Wrong input! Choose from the options!')


def bet_on_low_high():
    low = 18
    high = 36
    options = ['Low', 'High']
    cprint('Choose from below: ', attrs=['bold'])
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nChoose which one you want to bet on!', attrs=['bold'])
    while True:
        try:
            bet_type = input().lower()
            if bet_type == '1' or bet_type == 'Low':
                low_list = [low_nums for low_nums in range(1, low+1)]
                return low_list
            elif bet_type == '2' or bet_type == 'High':
                high_list = [high_nums for high_nums in range(low, high+1)]
                return high_list
            else:
                print('Wrong input! Choose from the options!')
        except ValueError:
            print('Wrong input! Choose from the options!')


def roll_number():
    pass


def check_number():
    pass


def is_winner():
    pass


def main():
    number_colors = [   'green', 'red', 'black', 'red', 'black', 'red', 'black',
                        'red', 'black', 'red', 'black', 'black', 'red', 'black', 
                        'red', 'black', 'red', 'black', 'red', 'red', 'black', 'red', 
                        'black', 'red', 'black','red', 'black', 'red', 'black', 'black', 
                        'red', 'black', 'red', 'black', 'red', 'black', 'red']

    options = ['Numbers', 'Dozens', 'Rows', 'Red or Black', 'Odd or Even', 'Low or High']
    # pocket = 10000
    # bet_input(pocket)
    # place_bet(100, options, number_colors)
    bet_on_low_high()
    # bet_on_numbers(number_colors)
    # elif bet_type == '2' or bet_type == '1st 12':
    # elif bet_type == '3' or bet_type == '2nd 12':
    # elif bet_type == '4' or bet_type == '3rd 12':


if __name__ == "__main__":
    main()
