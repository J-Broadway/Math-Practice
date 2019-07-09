import argparse
import random
from collections import OrderedDict

parser = argparse.ArgumentParser(description='Math Practice')
parser.add_argument('-p', '--practice', nargs='+', type=str, help='Use the letters "asmd" to practice (a)ddition'
                    ' (s)subtraction, (m)ultiplication, or (d)ivision')

args = parser.parse_args()
operations = args.practice[0]
practice = {'a': 'Addition,', 's': 'Subtraction,', 'm': 'Multiplication,', 'd': 'Division,'}

# If operator string has characters other than a,s,m, or d, return an error.
empylist = []
for x in range(len(operations)):
    if 'asmd'.find(operations[x]) < 0:
        print(operations[x] + ' is not a valid operation')
        empylist.append(operations[x])

# Remove invalid characters from operations
for x in range(len(empylist)):
    operations = operations.replace(empylist[x], '')

# Remove duplicate characters
operations = ''.join(OrderedDict.fromkeys(operations))

# Create practice message
empylist = []
pmessage = "Now practicing: "
for x in range(len(operations)):
    empylist.append(practice[operations[x]])

print(pmessage + ' '.join(empylist)[:-1] + ". Type 'q' to quit" +":")

# Okay now actually start serving the user math problems
# If wrong_answer = True, the same problem will be served.
wrong_answer = False
stop_practice = False

while not stop_practice:
    # Pick a random operation to serve as a problem
    def pick_random():

        # Choose an operation at random
        if len(operations) > 1:
            x = round(random.uniform(0, len(operations)-1))
        else:
            x = 0

        return operations[x]

    if wrong_answer is False:
        live_operation = pick_random()
    else:
        pass

    # TODO: Get Ranges from ranges.txt
    aRange1 = 1
    aRange2 = 10
    bRange1 = 1
    bRange2 = 100

    if wrong_answer is False:
        num = [0, 0]
        num[0] = round(random.uniform(aRange1, aRange2))
        num[1] = round(random.uniform(bRange1, bRange2))
        num = sorted(num, key=lambda x: random.random())  # Scramble num list
    else:
        pass

    # TODO: Division Function Here

    def practice_math(live_operation, aRange1, aRange2, bRange1, bRange2):

        global wrong_answer, stop_practice
        try:  # Addition
            if live_operation == 'a':
                answer = input('{} + {} = '.format(str(num[0]), str(num[1])))
                if answer == 'q':
                    stop_practice = True
                elif int(answer) == num[0] + num[1]:
                    wrong_answer = False
                else:
                    wrong_answer = True
                    print("Ur Gay")
        except:
            print("That's not an answer")
            wrong_answer = True

        try:  # Subtraction
            if live_operation == 's':
                answer = input('{} - {} = '.format(str(num[0]), str(num[1])))
                if answer == 'q':
                    stop_practice = True
                elif int(answer) == num[0] - num[1]:
                    wrong_answer = False
                else:
                    wrong_answer = True
                    print("Ur Gay")
        except:
            print("That's not an answer")
            wrong_answer = True

        try:  # Multiplication
            if live_operation == 'm':
                answer = input('{} x {} = '.format(str(num[0]), str(num[1])))
                if answer == 'q':
                    stop_practice = True
                elif int(answer) == num[0] * num[1]:
                    wrong_answer = False
                else:
                    wrong_answer = True
                    print("Ur Gay")
        except:
            print("That's not an answer")
            wrong_answer = True

    practice_math(live_operation, aRange1, aRange2, bRange1, bRange2)