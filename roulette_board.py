from blessings import Terminal


def print_board(upper_part, middle_part, lower_part, board_middle, board_lower):
    term = Terminal()
    board_length = 86
    short_board_length = 74
    upper_part_length = 14
    middle_part_length = 3
    lower_part_length = 6

    slot = '|{:^{width}}|'
    upper_lines = slot * upper_part_length
    middle_line = slot * middle_part_length
    lower_line = slot * lower_part_length
    width = len(slot)/middle_part_length

    decor = ('—' * board_length)
    green_decor = ('||' + term.bold_white_on_green + '    ' + term.normal + ' ' + '—' * (board_length-9) + '||')
    short_middle_decor = ('||' + '—' * (short_board_length-4) + '||')
    short_lower_decor = ('—' * short_board_length)
    left_padding = '               '
    lower_padding = left_padding + '      '

    print(left_padding + decor)
    print(left_padding + '|' + upper_lines.format(*upper_part, width=width) + '|')
    print(left_padding + green_decor)
    print(left_padding + '|' + upper_lines.format(*middle_part, width=width) + '|')
    print(left_padding + green_decor)
    print(left_padding + '|' + upper_lines.format(*lower_part, width=width) + '|')
    print(left_padding + decor)

    print(lower_padding + '|' + middle_line.format(*board_middle, width=20) + '|')
    print(lower_padding + short_middle_decor)

    print(lower_padding + '|' + lower_line.format(*board_lower, width=width*2.5) + '|')
    print(lower_padding + short_lower_decor)


def main():
    term = Terminal()
    upper_row = [term.bold_white_on_red + ' 3  ' + term.normal, term.bold_white_on_black + ' 6  ' + term.normal,
                term.bold_white_on_red + ' 9  ' + term.normal, term.bold_white_on_red + ' 12 ' + term.normal,
                term.bold_white_on_black + ' 15 ' + term.normal, term.bold_white_on_red + ' 18 ' + term.normal, 
                term.bold_white_on_red + ' 21 ' + term.normal, term.bold_white_on_black + ' 24 ' + term.normal,
                term.bold_white_on_red + ' 27 ' + term.normal, term.bold_white_on_red + ' 30 ' + term.normal,
                term.bold_white_on_black + ' 33 ' + term.normal, term.bold_white_on_red + ' 36 ' + term.normal]

    middle_row = [term.bold_white_on_black + ' 2  ' + term.normal, term.bold_white_on_red + ' 5  ' + term.normal,
                term.bold_white_on_black + ' 8  ' + term.normal, term.bold_white_on_black + ' 11 ' + term.normal,
                term.bold_white_on_red + ' 14 ' + term.normal, term.bold_white_on_black + ' 17 ' + term.normal,
                term.bold_white_on_black + ' 20 ' + term.normal, term.bold_white_on_red + ' 23 ' + term.normal,
                term.bold_white_on_black + ' 26 ' + term.normal, term.bold_white_on_black + ' 29 ' + term.normal,
                term.bold_white_on_red + ' 32 ' + term.normal, term.bold_white_on_black + ' 35 ' + term.normal]

    lower_row = [term.bold_white_on_red + ' 1  ' + term.normal, term.bold_white_on_black + ' 4  ' + term.normal,
                term.bold_white_on_red + ' 7  ' + term.normal, term.bold_white_on_black + ' 10 ' + term.normal,
                term.bold_white_on_black + ' 13 ' + term.normal, term.bold_white_on_red + ' 16 ' + term.normal,
                term.bold_white_on_red + ' 19 ' + term.normal, term.bold_white_on_black + ' 22 ' + term.normal,
                term.bold_white_on_red + ' 25 ' + term.normal, term.bold_white_on_black + ' 28 ' + term.normal,
                term.bold_white_on_black + ' 31 ' + term.normal, term.bold_white_on_red + ' 34 ' + term.normal]

    dernier = [term.bold_white_on_green + '    ' + term.normal] + upper_row + [term.bold_white_on_green + ' U  ' + term.normal]  
    moyen = [term.bold_white_on_green + ' 0  ' + term.normal] + middle_row + [term.bold_white_on_green + ' M  ' + term.normal]
    premier = [term.bold_white_on_green + '    ' + term.normal] + lower_row + [term.bold_white_on_green + ' L  ' + term.normal]

    board_middle = [    term.bold_white_on_green + '         1st12        ' + term.normal,
                        term.bold_white_on_green + '         2nd12        ' + term.normal, 
                        term.bold_white_on_green + '         3rd12        ' + term.normal]

    board_lower = [term.bold_white_on_green + '  1 - 18  ' + term.normal,
                    term.bold_white_on_green + '   EVEN   ' + term.normal,
                    term.bold_white_on_red + '   RED    ' + term.normal,
                    term.bold_white_on_black + '  BLACK   ' + term.normal,
                    term.bold_white_on_green + '   ODD   ' + term.normal,
                    term.bold_white_on_green + '  19 - 36  ' + term.normal]

    print_board(dernier, moyen, premier, board_middle, board_lower)


if __name__ == "__main__":
    main()
