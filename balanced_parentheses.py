# Write a function called balance that takes a string as a parameter
# loop through string
# if character is left parens, make a note
# if character is right parens
#   if there is matching left parens, leave alone
    # else make a note
# remove all non_matched parens
# return balanced_string

def balance(string):
   ¡ left_stack = []
    right_stack = []
    for index, char in enumerate(string):
        if char == "(":
            left_stack.append(index)
        elif char == ")":
            if len(left_stack) > 0:
                left_stack.pop()
            else:
                right_stack.append(index)
    # print(f'Left stack: {left_stack}, right stack: {right_stack}')
    bad_indices = left_stack + right_stack
    bad_indices.sort(reverse=True)
    return_string = ""
    for index, char in enumerate(string):
        if index not in bad_indices:
           return_string += char
    return return_string
balance(")(")