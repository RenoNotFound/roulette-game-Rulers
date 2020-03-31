from termcolor import colored


def print_board(upper_part, middle_part, lower_part, board_middle, board_lower):
    slot = '|{:^{width}}|'
    upper_lines = slot * 14
    middle_line = slot * 3
    lower_line = slot * 6
    width = len(slot)/3
    upper_decor = ('_' * 86)
    decor = ('||' + '_' * 82 + '||')
    shorter_decor = ('||' + '_' * 70 + '||')

    print(upper_decor)
    print('||' + ' ' * 82 + '||')
    print('|' + upper_lines.format(*upper_part, width=width) + '|')
    print(decor)
    print('||' + ' ' * 82 + '||')
    print('|' + upper_lines.format(*middle_part, width=width) + '|')
    print(decor)
    print('||' + ' ' * 82 + '||')
    print('|' + upper_lines.format(*lower_part, width=width) + '|')
    print(decor)

    print('      '+'||' + ' ' * 70 + '||')
    print('      '+'|' + middle_line.format(*board_middle, width=22.5) + '|')
    print('      '+shorter_decor)
    print('      '+'||' + ' ' * 70 + '||')
    print('      '+'|' + lower_line.format(*board_lower, width=width*2.5) + '|')
    print('      '+shorter_decor)

def main():
    dernier = [colored('    ', 'white', 'on_green', attrs=['bold'])] + [str(i) for i in range(1, 37) if i % 3 == 0] + ['U']  
    moyen = [colored(' 0  ' , 'white', 'on_green')] + [str(i) for i in range(1, 37) if i % 3 == 2] + ['M']
    premier = [colored('    ', 'white', 'on_green')] + [str(i) for i in range(1, 37) if i % 3 == 1] + ['L']
    board_middle = ['1st12', '2nd12', '3rd12']
    board_lower = ['1 - 18', 'EVEN', colored('   RED    ', 'white', 'on_red', attrs=['bold']), 'BLACK', 'ODD', '19 - 36']
    print_board(dernier, moyen, premier, board_middle, board_lower)


if __name__ == "__main__":
    main()
