#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    roman_string_upper = roman_string.upper()
    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    num = roman_dict.get(roman_string_upper[0])
    roman_string_upper = roman_string_upper[1:]
    for i, roman in enumerate(roman_string_upper):
        rom = roman_dict.get(roman_string_upper[i])
        if roman not in roman_dict:
            return 0
        if num >= rom:
            num += rom
            if len(roman_string) > 3:
                if i == 1 and rom < roman_dict.get(roman_string_upper[i+1]):
                    num -= 2
        else:
            num = roman_dict.get(roman_string_upper[i]) - num
    return num
