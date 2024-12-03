#!/usr/bin/env /usr/bin/python

import re
input_data_file = "part1.data"


def berechne(task):
    local_pattern = re.compile(r"\d+")
    data = local_pattern.findall(task)
    return(int(data[0]) * int(data[1]))



def main():

    # uncomment the next line to read the input data from the test file
    # input_data_file = "part1_test.data"

    my_file = open(input_data_file, "rt")
    my_data = my_file.read()
    my_file.close()

    # find all correct patterns
    mul_pattern = re.compile("mul\(\d+,\d+\)")
    all_valid = re.findall(mul_pattern, my_data)

    # sum up the products
    sum = 0
    for task in all_valid:
        sum += berechne(task)
    print("Total: {}".format(sum))


if __name__ == "__main__":
    main()
