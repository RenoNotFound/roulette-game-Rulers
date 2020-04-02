from termcolor import cprint
import os
from roulette_board import main as print_board
import random
from blessings import Terminal

term = Terminal()


def clear():
    os.system('clear')


def clear_screen(cash):
    clear()
    print_default(cash)


def print_default(cash):
    print_board()
    print_cash_box(cash)


def money_input():
    while True:
        try:
            value = int(input(term.bold_white + "\nEnter the amount of money you want to play with!(€)\n" + term.normal))
            return value
        except TypeError:
            print('Wrong input! Enter valid numbers!')
        except ValueError:
            print('Wrong input! Enter valid numbers!')


def print_cash_box(cash):

    print('—' * (len(str(cash))+6))
    cprint('| ' + str(cash) + ' € |', attrs=['bold'])
    print('—' * (len(str(cash))+6))


def available_money(pocket, bet_amount):
    cash = pocket - bet_amount
    return cash

def bet_input(pocket):
    minimum = 5
    betting = True
    while betting:
        try:
            if pocket >= minimum:
                cprint('\nMinimum bet is 5€', attrs=['bold'])
                amount = int(input('\nPlace your bets: '))
                if amount > pocket:
                    print('You don\'t have enough money! Sad..')
                elif amount < minimum:
                    print('The minimum is 5€')
                else:
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


def place_bet(options, number_colors, cash, placed_bet):
    clear_screen(placed_bet)
    print(term.bold_underline + 'Options' + term.bold + ':' + term.normal)
    # cprint('Options:\n', attrs=['bold', 'underline'])
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nChoose your bet:', attrs=['bold'])

    while True:
        try:
            bet_type = input().lower()
            if bet_type == '1' or bet_type == 'numbers':
                clear_screen(placed_bet)
                number = bet_on_numbers(number_colors, placed_bet)
                return number
            elif bet_type == '2' or bet_type == 'dozens':
                clear_screen(placed_bet)
                dozen = bet_on_dozens(placed_bet)
                return dozen
            elif bet_type == '3' or bet_type == 'rows':
                clear_screen(placed_bet)
                row = bet_on_rows(placed_bet)
                return row
            elif bet_type == '4' or bet_type == 'red or black':
                color = bet_on_color(number_colors, placed_bet)
                return color
            elif bet_type == '5' or bet_type == 'odd or even':
                clear_screen(placed_bet)
                odd_even = bet_on_odd_even(placed_bet)
                return odd_even
            elif bet_type == '6' or bet_type == 'low or high':
                clear_screen(placed_bet)
                low_high = bet_on_low_high(placed_bet)
                return low_high
            else:
                print('Wrong input! Choose from the options!')
        except ValueError:
            print('Wrong input! Choose from the options!')


def bet_on_numbers(number_colors, placed_bet):
    clear_screen(placed_bet)
    valid_numbers = number_colors

    while True:
        try:
            number = int(input('Choose a number between 0 - 36: '))
            if number not in valid_numbers:
                print('Enter a valid number!')
            else:
                return number
        except ValueError:
            print(term.bold_red + 'Wrong input!' + term.normal + '\nPlease enter a valid number!')


def bet_on_dozens(placed_bet):
    clear_screen(placed_bet)
    options = ['1st12', '2nd12', '3rd12']

    print(term.bold_underline + 'Choose from below' + term.bold + ':' + term.normal)
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nPlace your bet!', attrs=['bold'])

    while True:
        try:
            bet_type = input()
            if bet_type == '1' or bet_type == '1st12':
                return '1st12'
            elif bet_type == '2' or bet_type == '2nd12':
                return '2nd12'
            elif bet_type == '3' or bet_type == '3rd12':
                return '3rd12'
            else:
                print(term.bold_red + 'Wrong input!' + term.normal + '\nChoose from the options!')
        except ValueError:
            print(term.bold_red + 'Wrong input!' + term.normal + '\nChoose from the options!')


def bet_on_rows(placed_bet):
    clear_screen(placed_bet)
    options = ['Upper', 'Middle', 'Lower']

    print(term.bold_underline + 'Choose from below' + term.bold + ':' + term.normal)
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nPlace your bet!', attrs=['bold'])

    while True:
        try:
            bet_type = input().lower()
            if bet_type == '1' or bet_type == 'Upper':
                dernier = [i for i in range(1, 37) if i % 3 == 0]
                return 'upper'
            elif bet_type == '2' or bet_type == 'Middle':
                moyen = [i for i in range(1, 37) if i % 3 == 2]
                return 'middle'
            elif bet_type == '3' or bet_type == 'Lower':
                premier = [i for i in range(1, 37) if i % 3 == 1]
                return 'lower'
            else:
                print(term.bold_red + 'Wrong input!' + term.normal + '\nChoose from the options!')
        except ValueError:
            print(term.bold_red + 'Wrong input!' + term.normal + '\nChoose from the options!')


def bet_on_color(number_colors, placed_bet):
    clear_screen(placed_bet)
    valid_numbers = number_colors
    options = ['Red', 'Black']

    print(term.bold_underline + 'Choose from below' + term.bold + ':' + term.normal)
    # cprint('Choose from below: ', attrs=['bold'])
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nPlace your bet!', attrs=['bold'])

    while True:
        try:
            bet_type = input().lower()
            if bet_type == '1' or bet_type == 'Red':
                red_numbers = [key for key, value in valid_numbers.items() if value == 'red']
                return 'red'
            elif bet_type == '2' or bet_type == 'Black':
                black_numbers = [key for key, value in valid_numbers.items() if value == 'black']
                return 'black'
            else:
                print(term.bold_red + 'Wrong input!' + term.normal + '\nChoose from the options!')
                # print('Wrong input! Choose from the options!')
        except ValueError:
            print(term.bold_red + 'Wrong input!' + term.normal + '\nChoose from the options!')


def bet_on_odd_even(placed_bet):
    clear_screen(placed_bet)
    options = ['Odd', 'Even']

    print(term.bold_underline + 'Choose from below' + term.bold + ':' + term.normal)
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nPlace your bet!', attrs=['bold'])

    while True:
        try:
            bet_type = input().lower()
            if bet_type == '1' or bet_type == 'Odd':
                odds = [num % 2 != 0 for num in range(1, 37)]
                return 'odd'
            elif bet_type == '2' or bet_type == 'Even':
                evens = [num % 2 == 0 for num in range(1, 37)]
                return 'even'
            else:
                print('Wrong input! Choose from the options!')
        except ValueError:
            print('Wrong input! Choose from the options!')


def bet_on_low_high(placed_bet):
    clear_screen(placed_bet)
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
                return 'low'
            elif bet_type == '2' or bet_type == 'High':
                high_list = [high_nums for high_nums in range(low, high+1)]
                return 'high'
            else:
                print('Wrong input! Choose from the options!')
        except ValueError:
            print('Wrong input! Choose from the options!')


def betting_turn(pocket, options, number_colors):
    bet_amount = 0
    bet_holder = {}

    betting = True
    while betting:
        cash = available_money(pocket, bet_amount)
        clear_screen(cash)
        game = []

        turn = True
        while turn:
            placed_bet = bet_input(cash)
            bet_amount += placed_bet
            clear_screen(placed_bet)
            stake = place_bet(options, number_colors, cash, placed_bet)
            bet_holder[stake] = placed_bet

            new_bet = place_new_bet()
            if new_bet == 'no':
                game.append(new_bet)
                turn = False
            else:
                turn = False

        if len(game) == 1:
            break
        else:
            continue

    print(bet_holder)
    


def place_new_bet():
    try:
        new_bet = input('Do you want to place a new bet?(Y/N) ').lower()
        if new_bet == 'y':
            return 'yes'
        elif new_bet == 'n':
            return 'no'
        else:
            print('Wrong input!')
    except ValueError:
        print('Wrong input!')


def roll_number():
    rolled_number = random.randint(0, 36)
    return rolled_number


def check_number(rolled_number, bet_holder):
    length = 12
    bet_values = []
    for key, value in bet_holder.items():
        if key == '1st12' or key == '2nd12' or key == '3rd12':
            first_twelve = [num for num in range(1, length+1)]
            second_twelve = [num for num in range(length, (length*2)+1)]
            third_twelve = [num for num in range((length*2), (length*3)+1)]
            if rolled_number in first_twelve or rolled_number in second_twelve or rolled_number in third_twelve:
                bet_values.append(bet_holder[key*3])





def is_winner(check_number):
    pass


def valid_numbers(color_list):
    valid_nums = {}
    for i, color in enumerate(color_list):
        valid_nums[i] = color

    return valid_nums


def main():
    clear()

    number_colors = [   'green', 'red', 'black', 'red', 'black', 'red', 'black',
                        'red', 'black', 'red', 'black', 'black', 'red', 'black',
                        'red', 'black', 'red', 'black', 'red', 'red', 'black', 'red',
                        'black', 'red', 'black', 'red', 'black', 'red', 'black', 'black',
                        'red', 'black', 'red', 'black', 'red', 'black', 'red']

    options = ['Numbers', 'Dozens', 'Rows', 'Red or Black', 'Odd or Even', 'Low or High']

    valid_nums = valid_numbers(number_colors)

    # print(bet_input(pocketed_money))
    # print(place_bet(100, options, number_colors))
    rolled_number = 10
    
    # if is_winner = True:
    #     print("You win")
    # if is_winner = False:
    #     print("You lost")
    
    print_board()
    cash = money_input()
    betting_turn(cash, options, valid_nums)
    print(f"And the rolled number is : {rolled_number}")


if __name__ == "__main__":
    main()
