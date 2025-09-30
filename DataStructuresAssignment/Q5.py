
# This function simply takes in any string and will attempt to execute it with the assumption that it is an RPN
# expression. Then if it is valid it will output the answer and if it is not it will output that the expression is wrong
# Not That the only accepted delimiter between numbers is a comma.
def evaluate(expression):
    stack = []
    stack_pt = 0
    final_value = 0
    operators = ['+', '-', '*', '/']

    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            # if the next character is a digit then it will consume digits until met with an operator or comma and form
            # a number with the digits
            digit_buffer = ''
            j = i
            while expression[j].isdigit() and j < len(expression):
                digit_buffer += expression[j]
                j += 1
            stack.append(int(digit_buffer))
            stack_pt += 1
            i = j - 1

        elif expression[i] in operators and len(stack) >= 2:
            # if the character is an operator then it performs the respective operation on the last two items on stack,
            # removes them, and then places the answer on stack
                if expression[i] == '+':
                    final_value = stack[stack_pt - 2] + stack[stack_pt-1]
                elif expression[i] == '-':
                    final_value = stack[stack_pt - 2] - stack[stack_pt-1]
                elif expression[i] == '*':
                    final_value = stack[stack_pt - 2] * stack[stack_pt-1]
                elif expression[i] == '/':
                    if stack[stack_pt - 1] == '0':
                        print("Div 0")
                    else:
                        final_value = stack[stack_pt - 2] / stack[stack_pt-1]

                stack[stack_pt - 2] = final_value
                del stack[stack_pt-1]
                stack_pt -= 1

        # if the delimiter is not a comma then the expression is rendered invalid
        elif expression[i] != ',':
            print("Invalid expression")
            return
        i += 1

    # finally if there is more than one item on stack, the expression is rendered invalid
    if len(stack) != 1:
        print("Invalid expression")
        return
    else:
        print(stack[0])


# answer = 10
expres = "10,2,2+*4/"
evaluate(expres)
# answer = 3
expres = "1,2+3+2/"
evaluate(expres)
# answer = 90
expres = "100,50+30+2/"
evaluate(expres)
expres = "ashdashdlsad"
evaluate(expres)