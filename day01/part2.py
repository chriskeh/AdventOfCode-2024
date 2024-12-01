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
        while True:
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

    return links, rechts


def main():
    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    left, right = slurp_input(input_data_file)

    summe = 0
    for x in left:
        numx = right.count(x)
        summe += x * numx

    print("Summe : ", summe)


if __name__ == "__main__":
    main()
