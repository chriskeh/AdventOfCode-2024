#!/usr/bin/env /usr/bin/python

input_data_file = "part1.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: A list of sets. Each set represents the given answers in a group.
    """
    my_data = []

    with open(input_file, 'r') as f:
        while True:
            # Read a line.
            line = f.readline()
            # When readline returns an empty string, the file is fully read.
            # Break out of the while loop
            if line == "":
                break

            line = line.strip()
            levels_strings = line.split()
            # convert list of strings into list of integers
            levels = list(map(int, levels_strings))
            my_data.append(levels)

    return my_data


def check_level_increase(level):
    for pos in range(len(level) - 1):
        if level[pos] >= level[pos + 1] or int(level[pos + 1]) - int(level[pos]) > 3:
            return False
    return True


def check_level_decrease(level):
    for pos in range(len(level) - 1):
        if level[pos] <= level[pos + 1] or int(level[pos]) - int(level[pos + 1]) > 3:
            return False
    return True


def generate_variants(level):
    varianten = []
    for pos in range(len(level) - 1):
        tmp = level.copy()
        del tmp[pos]
        varianten.append(tmp)
    return varianten


def check_line(zeile):

    # 1. Wert kleiner als zweiter Wert ...
    if zeile[0] < zeile[1]:
        # pruefe, ob ganze Zeile ansteigend ist
        return check_level_increase(zeile)

    # 1. Wert grösser als zweiter Wert ==> decreasing ...
    if zeile[0] > zeile[1]:
        # pruefe, ob ganze Zeile absteigend ist
        return check_level_decrease(zeile)



def main():

    # uncomment the next line to read the input data from the test file
    #input_data_file = "part1_test.data"

    data = slurp_input(input_data_file)

    safe = 0
    nummer = 0
    for level in data:
        nummer += 1
        level_variants = generate_variants(level)

        for variant in level_variants:
            if check_line(variant):
                safe += 1
                break

    print(safe)


if __name__ == "__main__":
    main()
