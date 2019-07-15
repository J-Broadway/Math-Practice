import argparse
import random
import pickle
import sys
import initialize

initialize.main()

parser = argparse.ArgumentParser(description='Math Practice')
g = parser.add_mutually_exclusive_group()
g.add_argument('-p', '--practice', nargs='?', const='asmd', type=str, help=
               'Use the letters "asmd" to practice (a)ddition, (s)subtraction, (m)ultiplication, or (d)ivision')
g.add_argument('-r', '--ranges', nargs='+', type=str, help='Edit math practice ranges')
g.add_argument('-ls', '--list', nargs='?', const='asmd', type=str, help='List Ranges')

args = parser.parse_args()
practice = {'a': 'Addition', 's': 'Subtraction', 'm': 'Multiplication', 'd': 'Division'}
valid_operations = 'asmd'


# Checks for valid operations
def check_operations(string):
    for i in range(len(string)):
        if valid_operations.find(string[i]) == -1:
            raise Exception


# Load ranges.pickle
def load_ranges():
    global ranges
    with open('ranges.pickle', 'rb') as f:
        ranges = pickle.load(f)


# Save ranges to ranges.pickle
def save_ranges():
    with open('ranges.pickle', 'wb') as f:
        pickle.dump(ranges, f)
        print('Range Saved')


# Generate Practice Message
def practice_msg(x):
    empty_list = []
    for i in x:
        empty_list.append(practice[i] + ',')

    empty_list[len(empty_list) - 1] = empty_list[len(empty_list) - 1][:-1]
    pmessage = ' '.join(empty_list)

    print("Now practicing: " + pmessage)
    print("Type 'q' to quit")


# Pick random operation
def rand_operation():
    operation = args.practice[random.randint(0, len(args.practice)-1)]
    return operation


def math_practice():
    operation = rand_operation()

    a1 = ranges[operation][0][0]
    a2 = ranges[operation][0][1]
    b1 = ranges[operation][1][0]
    b2 = ranges[operation][1][1]

    shuffle_list = random.sample([random.randint(a1, a2), random.randint(b1, b2)], 2)
    num1 = shuffle_list[0]
    num2 = shuffle_list[1]

    if operation == 'a':
        answer = num1 + num2
        while True:
            try:
                user_input = input('{} + {} = '.format(num1, num2))
                if str(user_input).lower() == 'q':
                    break
                elif answer == int(user_input):
                    math_practice()
                else:
                    print("Ur Gay")
            except ValueError:
                print("Not a valid input.")
    elif operation == 's':
        answer = num1 - num2
        while True:
            try:
                user_input = input('{} - {} = '.format(num1, num2))
                if str(user_input).lower() == 'q':
                    break
                elif answer == int(user_input):
                    math_practice()
                else:
                    print("Ur Gay")
            except ValueError:
                print("Not a valid input.")
    elif operation == 'm':
        answer = num1 * num2
        while True:
            try:
                user_input = input('{} * {} = '.format(num1, num2))
                if str(user_input).lower() == 'q':
                    break
                elif answer == int(user_input):
                    math_practice()
                else:
                    print("Ur Gay")
            except ValueError:
                print("Not a valid input.")
    elif operation == 'd':
        num = num1 * num2
        divisor = random.sample([num1, num2], 1)[0]
        answer = num / divisor
        while True:
            try:
                user_input = input('{} / {} = '.format(num, divisor))
                if str(user_input).lower() == 'q':
                    break
                elif answer == int(user_input):
                    math_practice()
                else:
                    print("Ur Gay")
            except ValueError:
                print("Not a valid input.")

    print("Practice Finished")
    sys.exit()


# Do Math Practice
if args.practice is not None:
    practice_msg(args.practice)
    load_ranges()
    math_practice()

# Edit Ranges
elif args.ranges is not None:
    try:
        str_ranges = args.ranges[0]

        # Check valid operations
        check_operations(str_ranges)
        for x in range(len(str_ranges)):
            if str_ranges[x] == 'a':
                range_check = 'n'
                while range_check == 'n':
                    load_ranges()
                    print('--Editing ranges for Addition--')
                    range1min = int(input('Range 1 Min: '))
                    range1max = int(input('Range 1 Max: '))
                    range2min = int(input('Range 2 Min: '))
                    range2max = int(input('Range 2 Max: '))

                    range_check = str(input('Is {}-{}, {}-{} correct? (Y/N): '.format(range1min, range1max, range2min,
                                                                               range2max)).lower())
                    if range_check == "y" or range_check == "n":
                        pass
                    else:
                        raise Exception
                    ranges['a'] = [[range1min, range1max], [range2min, range2max]]

                save_ranges()

            elif str_ranges[x] == 's':
                range_check = 'n'
                while range_check == 'n':
                    load_ranges()
                    print('--Editing ranges for Subtraction--')
                    range1min = int(input('Range 1 Min: '))
                    range1max = int(input('Range 1 Max: '))
                    range2min = int(input('Range 2 Min: '))
                    range2max = int(input('Range 2 Max: '))

                    range_check = str(input('Is {}-{}, {}-{} correct? (Y/N): '.format(range1min, range1max, range2min,
                                                                               range2max)).lower())
                    if range_check == "y" or range_check == "n":
                        pass
                    else:
                        raise Exception
                    ranges['s'] = [[range1min, range1max], [range2min, range2max]]

                save_ranges()

            elif str_ranges[x] == 'm':
                range_check = 'n'
                while range_check == 'n':
                    load_ranges()
                    print('--Editing ranges for Multiplication--')
                    range1min = int(input('Range 1 Min: '))
                    range1max = int(input('Range 1 Max: '))
                    range2min = int(input('Range 2 Min: '))
                    range2max = int(input('Range 2 Max: '))

                    range_check = str(input('Is {}-{}, {}-{} correct? (Y/N): '.format(range1min, range1max, range2min,
                                                                               range2max)).lower())
                    if range_check == "y" or range_check == "n":
                        pass
                    else:
                        raise Exception
                    ranges['m'] = [[range1min, range1max], [range2min, range2max]]

                save_ranges()

            elif str_ranges[x] == 'd':
                range_check = 'n'
                while range_check == 'n':
                    load_ranges()
                    print('--Editing ranges for Division--')
                    range1min = int(input('Range 1 Min: '))
                    range1max = int(input('Range 1 Max: '))
                    range2min = int(input('Range 2 Min: '))
                    range2max = int(input('Range 2 Max: '))

                    range_check = str(input('Is {}-{}, {}-{} correct? (Y/N): '.format(range1min, range1max, range2min,
                                                                               range2max)).lower())
                    if range_check == "y" or range_check == "n":
                        pass
                    else:
                        raise Exception
                    ranges['d'] = [[range1min, range1max], [range2min, range2max]]

                save_ranges()

    except:
        print('Invalid Input')
# List Ranges
elif args.list is not None:
    try:
        # Check valid operations
        check_operations(args.list)

        # Load Ranges
        with open('ranges.pickle','rb') as f:
            p_ranges = pickle.load(f)

        for x in range(len(args.list)):
            if args.list[x] == 'a':
                mystr = str(p_ranges['a'])[1:-1]
                print('Addition: ' + mystr)
            elif args.list[x] == 's':
                mystr = str(p_ranges['s'])[1:-1]
                print('Subtraction: ' + mystr)
            elif args.list[x] == 'm':
                mystr = str(p_ranges['m'])[1:-1]
                print('Multiplication: ' + mystr)
            elif args.list[x] == 'd':
                mystr = str(p_ranges['d'])[1:-1]
                print('Division: ' + mystr)
    except:
        print('Invalid Input')

namespace = vars(args)
if list(namespace.values()).count(None) == 3:
    args.practice = valid_operations
    practice_msg(args.practice)
    load_ranges()
    math_practice()