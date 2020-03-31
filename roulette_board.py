def print_board(upper_part, middle_part, lower_part, board_middle, board_lower):
    slot = '|{:^{width}}|'
    upper_lines = slot * 14
    middle_line = slot * 3
    lower_line = slot * 6
    width = len(slot)/3
    decor = ('_' * ((len(slot) * (int(14/2))) - 5))
    shorter_decor = ('_' * ((len(slot) * (int(14/2))) - 4 - int(6.5*2)))

    print(decor)
    print('\n' + '|' + upper_lines.format(*upper_part, width=width) + '|')
    print(decor)
    print('\n' + '|' + upper_lines.format(*middle_part, width=width) + '|')
    print(decor)
    print('\n' + '|' + upper_lines.format(*lower_part, width=width) + '|')
    print(decor)

    print('\n'+'      '+'|' + middle_line.format(*board_middle, width=22.5) + '|')
    print('      '+shorter_decor)
    print('\n'+'      '+'|' + lower_line.format(*board_lower, width=width*2.5) + '|')


def main():
    # board = init_board()
    dernier = [''] + [str(i) for i in range(1, 37) if i % 3 == 0] + ['D']  
    moyen = ['0'] + [str(i) for i in range(1, 37) if i % 3 == 2] + ['M']
    premier = [''] + [str(i) for i in range(1, 37) if i % 3 == 1] + ['P']
    board_middle = ['1st12', '2nd12', '3rd12']
    board_lower = ['1 - 18', 'EVEN', 'RED', 'BLACK', 'ODD', '19 - 36']
    print_board(dernier, moyen, premier, board_middle, board_lower)


if __name__ == "__main__":
    main()
