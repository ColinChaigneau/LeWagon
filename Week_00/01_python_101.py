###
### Challenge - What is your name
###

def compute_name(first_name, middle_name, last_name): #
    return f"{first_name} {middle_name} {last_name}"

###
### Challenge - Stupid Coaching
###

def coach_answer(your_message):
    if your_message == "I am going to work right now!":
        return ""
    elif your_message[-1] == "?":
        return "Silly question, get dressed and go to work!"
    else:
        return "I don't care, get dressed and go to work!"

def custom_isupper(string):
    return string.upper() == string

def coach_answer_enhanced(your_message):
    if your_message.lower() == "I am going to work right now!".lower():
        return ""
    if custom_isupper(your_message):
        return f"I can feel your motivation! {coach_answer(your_message)}"
    else:
        return coach_answer(your_message)

###
### Challenge - Colorful Algorithm
###

from itertools import combinations

def compute_product(digit_string):
    digits = list(digit_string)
    product = 1
    for digit in digits:
        product *= int(digit)
    return product

def is_colorful(n):
    # Split n into into parts
    n_string = str(n)
    n_parts = [n_string[i:j] for i,j in combinations(range(len(n_string) + 1),2)]
    # Combinations from itertools compute all possible pairs (a,b) with a strictly lower than b
    # Equivalent to a double for loop
    
    # Compute product of digits
    n_parts_product = [compute_product(part) for part in n_parts]
    
    # To ckeck if there is duplicate compute set(<list>) to eliminate duplicates
    return len(n_parts_product) == len(set(n_parts_product))  # If same length no duplicate, hence n is a colorful number
