def divide_multiply(inputs2, y):
    # check the operator and use -1 and +1 to the index to reference the numbers
    match inputs2[y]:
        case '*':
            inputs2[y + 1] = inputs2[y-1] * inputs2[y + 1]
            inputs2[y-1] = "remove"
        case '/':
            # check if trying to divide by zero
            if inputs2[y+1] == 0:
                inputs2[0] = "ERROR: DIVISION BY ZERO"
                return inputs2
            inputs2[y + 1] = inputs2[y-1] / inputs2[y + 1]
            inputs2[y-1] = "remove"
    return inputs2


def addition_subtraction(inputs2, x):
    # check the operator and use -1 and +1 to the index to reference the numbers
    # the first number in the operation is changed to "remove", the second will be used for further calculations
    match inputs2[x]:
        case '+':
            inputs2[x + 1] = inputs2[x-1] + inputs2[x + 1]
            inputs2[x-1] = "remove"
        case '-':
            inputs2[x + 1] = inputs2[x-1] - inputs2[x + 1]
            inputs2[x-1] = "remove"
    return inputs2


def calculus(calculus_inputs):
    # division and multiplication
    # the first number in the operation is changed to "remove", the second will be used for further calculations
    for y in range(len(calculus_inputs)):
        # if index is odd, it is an operator
        if y % 2 != 0 and "ERROR: DIVISION BY ZERO" not in calculus_inputs:
            calculus_inputs = divide_multiply(calculus_inputs, y)
    # put the needed elements in list 2
    inputs2 = [z for z in calculus_inputs if z != "remove" and z != '/' and z != '*']
    # addition and subtraction
    for x in range(len(inputs2)):
        # if index is odd, it is an operator
        if x % 2 != 0 and "ERROR: DIVISION BY ZERO" not in inputs2:
            inputs2 = addition_subtraction(inputs2, x)
    # filter the list to remove -, + and unneeded numbers, previously changed to remove
    return [z for z in inputs2 if z != "remove" and z != '-' and z != '+']


infinite_loop = 1
inputs = []
while infinite_loop == 1:
    # try except to avoid index out of range, checking if the answer needs to be given again (x=x)
    try:
        if inputs[1] != '=':
            inputs = (input().split())
    except IndexError:
        inputs = input().split()
    # turn the numbers to float
    for i, input_element in enumerate(inputs):
        if i % 2 == 0:
            try:
                inputs[i] = float(input_element)
            except ValueError:
                inputs[0] = "INPUT ERROR"
                break
    # go to next iteration if there is an input error
    if inputs[0] == "INPUT ERROR":
        print("INPUT ERROR")
        continue
    answer = calculus(inputs)[0]
    print(answer)
    inputs.clear()
    next_operation = input()
    # if operator is given, ANS and the operator go into the next operation
    try:
        float(next_operation)
        continue
    except ValueError:
        if answer == "ERROR: DIVISION BY ZERO":
            ans = 0
        inputs = [answer, next_operation]
        print("\nANS", "\n", next_operation)
        continue
exit()
