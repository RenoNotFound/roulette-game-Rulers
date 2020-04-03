from termcolor import cprint
import os
from roulette_board import main as print_board
import random
from blessings import Terminal
import time
import sys

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
            value = int(input(term.bold_white + "\nEnter the amount of money you want to play with!(€)\n" + term.normal + '\n'))
            return value
        except TypeError:
            print('Wrong input! Enter valid numbers!')
        except KeyboardInterrupt:
            clear()
            sys.exit()


def print_cash_box(cash):

    print('—' * (len(str(cash))+6))
    cprint('| ' + str(cash) + ' € |', attrs=['bold'])
    print('—' * (len(str(cash))+6))


def bet_input(pocket):
    minimum = 5
    betting = True
    while betting:
        try:
            if pocket >= minimum:
                cprint('\nMinimum bet is 5 €', attrs=['bold'])
                amount = int(input('\nPlace your bets: '))
                if amount > pocket:
                    print('You don\'t have enough money! Sad..')
                elif amount < minimum:
                    print('\nYour bet is too low!')
                else:
                    return amount
            else:
                print('You don\'t have enough money!')
                betting = False
        except TypeError:
            print('Please enter valid amount!')
        except ValueError:
            print('Please enter valid amount!')
        except KeyboardInterrupt:
            clear()
            sys.exit()

        clear_screen(pocket)


def place_bet(options, number_colors, cash, placed_bet, rolled_number, valid_numbers):
    clear_screen(placed_bet)
    print(term.bold_underline + '\nOptions' + term.bold + ':\n' + term.normal)
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nChoose your bet:', attrs=['bold'])

    while True:
        try:
            bet_type = input().lower()
            if bet_type == 'cheat':
                print_cheat_box(rolled_number, valid_numbers)
                input('\nI hope you are happy now... Choose from the options above\n')

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
                print('\nWrong input! Choose from the options!')
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

    print(term.bold_underline + '\nChoose from below' + term.bold + ':\n' + term.normal)
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

    print(term.bold_underline + '\nChoose from below' + term.bold + ':\n' + term.normal)
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nPlace your bet!', attrs=['bold'])

    while True:
        try:
            bet_type = input().lower()
            if bet_type == '1' or bet_type == 'Upper':
                return 'upper'
            elif bet_type == '2' or bet_type == 'Middle':
                return 'middle'
            elif bet_type == '3' or bet_type == 'Lower':
                return 'lower'
            else:
                print(term.bold_red + 'Wrong input!' + term.normal + '\nChoose from the options!')
        except ValueError:
            print(term.bold_red + 'Wrong input!' + term.normal + '\nChoose from the options!')


def bet_on_color(number_colors, placed_bet):
    clear_screen(placed_bet)
    options = ['Red', 'Black']

    print(term.bold_underline + '\nChoose from below' + term.bold + ':\n' + term.normal)
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nPlace your bet!', attrs=['bold'])

    while True:
        try:
            bet_type = input().lower()
            if bet_type == '1' or bet_type == 'Red':
                return 'red'
            elif bet_type == '2' or bet_type == 'Black':
                return 'black'
            else:
                print(term.bold_red + 'Wrong input!' + term.normal + '\nChoose from the options!')
        except ValueError:
            print(term.bold_red + 'Wrong input!' + term.normal + '\nChoose from the options!')


def bet_on_odd_even(placed_bet):
    clear_screen(placed_bet)
    options = ['Odd', 'Even']

    print(term.bold_underline + '\nChoose from below' + term.bold + ':\n' + term.normal)
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nPlace your bet!', attrs=['bold'])

    while True:
        try:
            bet_type = input().lower()
            if bet_type == '1' or bet_type == 'Odd':
                return 'odd'
            elif bet_type == '2' or bet_type == 'Even':
                return 'even'
            else:
                print('Wrong input! Choose from the options!')
        except ValueError:
            print('Wrong input! Choose from the options!')


def bet_on_low_high(placed_bet):
    clear_screen(placed_bet)
    options = ['Low(1 - 18)', 'High(19 - 36)']

    print(term.bold_underline + '\nChoose from below' + term.bold + ':\n' + term.normal)
    for i, option in enumerate(options):
        print(f'[{i+1}] {option}')
    cprint('\nChoose which one you want to bet on!', attrs=['bold'])

    while True:
        try:
            bet_type = input().lower()
            if bet_type == '1' or bet_type == 'Low':
                return 'low'
            elif bet_type == '2' or bet_type == 'High':
                return 'high'
            else:
                print('Wrong input! Choose from the options!')
        except ValueError:
            print('Wrong input! Choose from the options!')


def betting_turn(pocket, options, number_colors, rolled_number, valid_numbers):
    bet_amount = 0
    bet_holder = {}

    betting = True
    while betting:
        cash = pocket - bet_amount
        clear_screen(cash)
        game = []

        turn = True
        while turn:
            placed_bet = bet_input(cash)
            bet_amount += placed_bet
            clear_screen(placed_bet)
            stake = place_bet(options, number_colors, cash, placed_bet, rolled_number, valid_numbers)
            bet_holder[stake] = placed_bet
            clear()
            print_board()
            new_bet = place_new_bet()
            if new_bet == 'wheel':
                game.append(new_bet)
                turn = False
            elif new_bet == 'bet':
                turn = False
        if len(game) > 0:
            break
        else:
            continue

    return bet_holder


def place_new_bet():
    while True:
        try:
            cprint('\nAre you ready to spin the wheel?', attrs=['bold'])
            print('\n[1] Yes! Let\'s do this!')
            print('[2] Nope, want to place another bet!')
            cprint('\nSo what\'s up?', attrs=['bold'])
            new_bet = input().lower()
            if new_bet == 'y' or new_bet == '1':
                return 'wheel'
            elif new_bet == 'n' or new_bet == '2':
                return 'bet'
            else:
                print('Wrong input!')
        except ValueError:
            print('Wrong input!')


def roll_number():
    rolled_number = random.randint(0, 36)
    return rolled_number


def check_number(rolled_number, bet_holder, valid_numbers):
    low = 18
    high = 36
    length = 12
    num_range = 37
    bet_values = []

    for key, value in bet_holder.items():
        if rolled_number == key:
            bet_values.append(bet_holder[key]*34)

        elif key == '1st12':
            first_twelve = [num for num in range(1, length+1)]
            if rolled_number in first_twelve:
                bet_values.append(bet_holder[key]*2)
            else:
                bet_values.append(bet_holder[key] - (bet_holder[key]*2))

        elif key == '2nd12':
            second_twelve = [num for num in range(length, (length*2)+1)]
            if rolled_number in second_twelve:
                bet_values.append(bet_holder[key]*2)
            else:
                bet_values.append(bet_holder[key] - (bet_holder[key]*2))

        elif key == '3rd12':
            third_twelve = [num for num in range((length*2), (length*3)+1)]
            if rolled_number in third_twelve:
                bet_values.append(bet_holder[key]*2)
            else:
                bet_values.append(bet_holder[key] - (bet_holder[key]*2))

        elif key == 'upper':
            upper = [num for num in range(1, num_range) if num % 3 == 0]
            if rolled_number in upper:
                bet_values.append(bet_holder[key]*2)
            else:
                bet_values.append(bet_holder[key] - (bet_holder[key]*2))

        elif key == 'middle':
            middle = [num for num in range(1, num_range) if num % 3 == 2]
            if rolled_number in middle:
                bet_values.append(bet_holder[key]*2)
            else:
                bet_values.append(bet_holder[key] - (bet_holder[key]*2))

        elif key == 'lower':
            lower = [num for num in range(1, num_range) if num % 3 == 1]
            if rolled_number in lower:
                bet_values.append(bet_holder[key]*2)
            else:
                bet_values.append(bet_holder[key] - (bet_holder[key]*2))

        elif key == 'red':
            red_numbers = [key for key, value in valid_numbers.items() if value == 'red']
            if rolled_number in red_numbers:
                bet_values.append(bet_holder[key])
            else:
                bet_values.append(bet_holder[key] - (bet_holder[key]*2))

        elif key == 'black':
            black_numbers = [key for key, value in valid_numbers.items() if value == 'black']
            if rolled_number in black_numbers:
                bet_values.append(bet_holder[key])
            else:
                bet_values.append(bet_holder[key] - (bet_holder[key]*2))

        elif key == 'odd':
            odds = [num % 2 != 0 for num in range(1, num_range)]
            if rolled_number in odds:
                bet_values.append(bet_holder[key])
            else:
                bet_values.append(bet_holder[key] - (bet_holder[key]*2))

        elif key == 'even':
            evens = [num % 2 == 0 for num in range(1, num_range)]
            if rolled_number in evens:
                bet_values.append(bet_holder[key])
            else:
                bet_values.append(bet_holder[key] - (bet_holder[key]*2))

        elif key == 'low':
            low_list = [low_nums for low_nums in range(1, low+1)]
            if rolled_number in low_list:
                bet_values.append(bet_holder[key])
            else:
                bet_values.append(bet_holder[key] - (bet_holder[key]*2))

        elif key == 'high':
            high_list = [high_nums for high_nums in range(low, high+1)]
            if rolled_number in high_list:
                bet_values.append(bet_holder[key])
            else:
                bet_values.append(bet_holder[key] - (bet_holder[key]*2))

    return sum(bet_values)


def valid_numbers(color_list):
    valid_nums = {}
    for i, color in enumerate(color_list):
        valid_nums[i] = color

    return valid_nums


def print_bet_holder(bet_holder):

    cprint('Your bets:\n', attrs=['bold'])

    for key, value in bet_holder.items():
        print('  ' + '—' * (len(str(key))+len(str(value))+11))
        cprint('  ' + '| ' + str(key) + ' --> ' + str(value) + ' € |', attrs=['bold'])
        print('  ' + '—' * (len(str(key))+len(str(value))+11))


def print_cheat_box(rolled_number, valid_numbers):

    cprint('\nNoice, I see you know about the secret passage...\n', attrs=['bold'])
    print('  ' + '—' * (len(str(rolled_number))+5+len(valid_numbers[rolled_number])))
    cprint('  ' + '| ' + valid_numbers[rolled_number] + ' ' + str(rolled_number) + ' |', attrs=['bold'])
    print('  ' + '—' * (len(str(rolled_number))+5+len(valid_numbers[rolled_number])))


def print_rolled_number(rolled_number):
    cprint('\nYour lucky number:\n', attrs=['bold'])
    print('  ' + '—' * (len(str(rolled_number))+4))
    cprint('  ' + '| ' + str(rolled_number) + ' |', attrs=['bold'])
    print('  ' + '—' * (len(str(rolled_number))+4))


def print_win_amount(win_amount):
    turning_point = 0
    if win_amount > turning_point:
        cprint('\nYou won:\n', attrs=['bold'])
        print('  ' + '—' * (len(str(win_amount))+6))
        cprint('  ' + '| ' + str(win_amount) + ' € |', attrs=['bold'])
        print('  ' + '—' * (len(str(win_amount))+6))
    elif win_amount < turning_point:
        cprint('\nYou lost:\n', attrs=['bold'])
        print('  ' + '—' * (len(str(win_amount))+8))
        cprint('  ' + '| ' + str(win_amount) + ' € |', attrs=['bold'])
        print('  ' + '—' * (len(str(win_amount))+8))


def intro():
    clear()
    cprint('Welcome to Rulers! The most reliable gambling spot out there!', attrs=['bold'])
    time.sleep(2)
    cprint('\nLow on cash at the end of the month?', attrs=['bold'])
    time.sleep(3)
    cprint('\nNo worries, here is your chance to double some money!', attrs=['bold'])
    time.sleep(2)
    cprint('\nNow, let\'s see if you will triumph or get lost in never ending spiral towards gambling addiction', attrs=['bold'])
    time.sleep(4)
    cprint('\nSounds like fun, huh?', attrs=['bold'])
    time.sleep(2)
    input(term.bold + '\nPress a button to continue to your bright future' + term.normal)
    input('\nSo proud of ya...*happy tears*\n')


def main_menu(number_colors, options, valid_nums):
    clear()
    cprint('Start betting right away!\n', attrs=['bold'])
    print('[1] Start Game')
    print('[2] Rules')
    print('[3] Quit\n')
    cprint('\nYour choice:', attrs=['bold'])

    while True:
        try:
            choose = input().lower()
            if choose == '1' or choose == 'start':
                clear()
                game_on(number_colors, options, valid_nums)
            elif choose == '2' or choose == 'rules':
                rules(number_colors, options, valid_nums)
            elif choose == '3' or choose == 'quit':
                clear()
                sys.exit()
            else:
                print('Wrong input')
        except TypeError:
            print('Wrong input')
        except ValueError:
            print('Wrong input')

        except KeyboardInterrupt:
            clear()
            sys.exit()


def rules(number_colors, options, valid_nums):
    clear()
    cprint('Coming soon...\n', attrs=['bold'])
    while True:
        input('Press a button to get back to the menu!\n')
        main_menu(number_colors, options, valid_nums)


def game_on(number_colors, options, valid_nums):
    print_board()
    cash = money_input()

    while True:
        print_board()
        rolled_number = roll_number()
        bet_holder = betting_turn(cash, options, number_colors, rolled_number, valid_nums)

        time.sleep(2)
        clear()
        print_board()
        print_bet_holder(bet_holder)
        time.sleep(2)
        print_rolled_number(rolled_number)
        win_amount = check_number(rolled_number, bet_holder, valid_nums)
        cash += win_amount
        time.sleep(5)
        print_win_amount(win_amount)
        time.sleep(5)
        withdraw_or_play(cash)


def withdraw_or_play(cash):
    clear_screen(cash)
    cprint('\nWhat about an other turn?', attrs=['bold'])
    print('\n[1] Of course! Who do you think I am..?! Peasant...')
    print('[2] Don\'t play with me! Give me my money! Can\'t believe this guy...\n')

    cprint('So which one?', attrs=['bold'])

    while True:
        try:
            game_play = input().lower()
            if game_play == '1' or game_play == 'yes':
                clear_screen(cash)
                input('\nPress a button for new turn\n')
                break
            elif game_play == '2' or game_play == 'no':
                clear()
                print_board()
                cprint('Noice! Your reward (or not):\n', attrs=['bold'])
                print_cash_box(cash)
                time.sleep(2)
                cprint('\nThanks for playing with us! See you soon!')
                time.sleep(2)
                sys.exit()
            else:
                print('Wrong input')
        except TypeError:
            print('Wrong input')
        except KeyboardInterrupt:
            clear()
            sys.exit()


def main():

    number_colors = [   'green', 'red', 'black', 'red', 'black', 'red', 'black',
                        'red', 'black', 'red', 'black', 'black', 'red', 'black',
                        'red', 'black', 'red', 'black', 'red', 'red', 'black', 'red',
                        'black', 'red', 'black', 'red', 'black', 'red', 'black', 'black',
                        'red', 'black', 'red', 'black', 'red', 'black', 'red']
    options = ['Numbers', 'Dozens', 'Rows', 'Red or Black', 'Odd or Even', 'Low or High']
    valid_nums = valid_numbers(number_colors)

    # intro()
    main_menu(number_colors, options, valid_nums)


if __name__ == "__main__":
    main()
