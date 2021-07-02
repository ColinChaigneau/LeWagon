###
### Challenge - Calculator
###

import operator

operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod
}

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def simple_calculator(array):
    if len(array) != 3:
        return 'Please enter valid format: [Operand, Operator, Operand]'
    if not ( is_number(array[0]) and is_number(array[2]) ):
        return 'Please enter valid format: [Operand, Operator, Operand]'
    if not array[1] in '+-*/%':
        return 'Please enter a valid operator [ +, -, /, *, % ]'
    
    operand1 = int(array[0]) if array[0].isdigit() else float(array[0])
    operand2 = int(array[2]) if array[2].isdigit() else float(array[2])
    operator = operators[array[1]]
    
    return operator(operand1,operand2)


###
### Challenge - Fizz Buzz
###

def fizz_buzz(number):
    array = []
    for i in range(1,number+1):
        if i % 3 == 0 and i % 5 == 0:
            array.append('FizzBuzz')
        elif i % 3 == 0:
            array.append('Fizz')
        elif i % 5 == 0:
            array.append('Buzz')
        else:
            array.append(i)
    
    return array


###
### Challenge - Shuffle
###

import random
from copy import copy

def manual_shuffle(array):
    shuffled_array = []
    temp_array = copy(array)
    array_length = len(temp_array)
    for _ in range(array_length):
        random_index = random.randrange(len(temp_array))
        shuffled_array.append(temp_array[random_index])
        del temp_array[random_index]
    
    return shuffled_array