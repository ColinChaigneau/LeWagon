###
### Challenge - Simple Burger
###

MACDO_CALORIES = {
    'Hamburger': 250,
    'Cheese Burger': 300,
    'Big Mac': 540,
    'McChicken': 350,
    'French Fries': 230,
    'Salad': 15,
    'Coca Cola': 150,
    'Sprite': 150
}

def poor_calories_counter(item1,item2,item3):
    count = 0
    
    if item1 in MACDO_CALORIES:
        count += MACDO_CALORIES.get(item1, 0)
    else:
        return f'{item1} not found'
    
    if item2 in MACDO_CALORIES:
        count += MACDO_CALORIES.get(item2, 0)
    else:
        return f'{item1} not found'
    
    if item3 in MACDO_CALORIES:
        count += MACDO_CALORIES.get(item3, 0)
    else:
        return f'{item1} not found'
    
    return count

###
### Challenge - Advanced Burger
###

MACDO_MEALS = {
    'Happy Meal': ['Cheese Burger', 'French Fries', 'Coca Cola'],
    'Best Of Big Mac': ['Big Mac', 'French Fries', 'Coca Cola'],
    'Best Of McChicken': ['McChicken', 'Salad', 'Sprite']
}

def advanced_calories_counter(items):
    calories = 0
    for item in items:
        if item in MACDO_MEALS:
            for dishes in MACDO_MEALS[item]:
                calories += MACDO_CALORIES.get(dishes, 0)
        elif item in MACDO_CALORIES:
            calories += MACDO_CALORIES.get(item, 0)
        else:
            return f"{item} not found"
    
    return calories


###
### Challenge - Roman Numerals
###

ROMAN_UNITS = { 'I': 1, 'II' : 2, 'III' : 3, 'V' : 5, 'VI' : 6, 'VII' : 7, 'VIII' : 8, 'IV' : 4, 'IX' : 9 }
ROMAN_TENS = { 'X': 10, 'XX' : 20, 'XXX' : 30, 'L' : 50, 'LX' : 60, 'LXX' : 70, 'LXXX' : 80, 'XL' : 40, 'XC' : 90 }
ROMAN_HUNDREDS = {'C': 100, 'CC' : 200, 'CCC' : 300, 'D' : 500, 'DC' : 600, 'DCC' : 700, 'DCCC' : 800, 'CD' : 400, 'CM' : 900 }
ROMAN_THOUSANDS = {'M': 1000, 'MM' : 2000, 'MMM' : 3000 }

ROMAN_NUMERALS = {
    'UNITS' : ROMAN_UNITS,
    'TENS' : ROMAN_TENS,
    'HUNDREDS' : ROMAN_HUNDREDS,
    'THOUSANDS' : ROMAN_THOUSANDS
}

def roman_to_int(roman_string):
    int_value = 0
    for dico in ROMAN_NUMERALS.values(): # we are going to check which symbol represent the units, tens, hundreds and thousands step by step
        possible_symbol = ""
        for symbol in dico:
            if symbol in roman_string:     # we check if each symbol of the dictionnary is in the roman string, it it does then we store it
                possible_symbol = symbol   # we have constructed the dictionnaries to avoid that possible_symbol contain the wrong symbol, in case
                                           # of 'III' for instance being mistaken with 'II' or 'I'
        if possible_symbol: # if we found a symbol then we add its numerical value 
            int_value += dico[possible_symbol]
            roman_string = roman_string[:-len(possible_symbol)] # if we found a symbol we delete it from the roman_string to avoid a case such that 'X' is mistaken with 'IX'
    
    return int_value