#!/usr/bin/env /usr/bin/python

input_data_file = "part1.data"


def slurp_input(input_file):
    """
    Read the input file.
    :param input_file:
    :return: Two lists, one for the left column, one for the right column
    """
    links = []
    rechts = []

    with open(input_file, 'r') as f:
        while (True):
            # Read a line.
            line = f.readline()
            # When readline returns an empty string, the file is fully read.
            # Break out of the while loop
            if line == "":
                break

            line = line.strip()
            a, b = line.split()
            links.append(int(a))
            rechts.append(int(b))

    return sorted(links), sorted(rechts)


def abstand(x, y):
    return abs(x - y)


def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    left, right = slurp_input(input_data_file)

    abstaende = []
    pos = 0
    for x in left:
        abstaende.append(abstand(x, right[pos]))
        pos += 1

    # print("abstaende: ", abstaende)
    print("Summe : ", sum(abstaende))


if __name__ == "__main__":
    main()
