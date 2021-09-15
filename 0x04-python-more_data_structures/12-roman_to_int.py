#!/usr/bin/python3

def char(char):
    switch = {
      'I':1,
      'V': 5,
      'X': 10,
      'L': 50,
      'C': 100,
      'D': 500,
      'M': 1000,
      'IV': 4,
      'IX': 9,
      'XL': 40,
      'XC': 90,
      'CD': 400,
      'CM': 900
    }
    return switch.get(char,"Invalid input")


def roman_to_int(roman_string):
        num = 0
        if type(roman_string) != str or roman_string == None:
                return None
        
        for i in range(len(roman_string)):
                c = roman_string[i]
                if len(roman_string) > i + 1:
                        _c = roman_string[i + 1]
                else: 
                        _c = " "

                if c == 'I':
                        if _c == 'V':
                                num += char(c + _c)
                                i += 1
                        elif _c == 'X':
                                num += char(c + _c)
                                i += 1
                        else:
                                num += char(c)
                elif c == 'V':
                        num += char(c)
                elif c == 'X':
                        if _c == 'L':
                                num += char(c + _c)
                                i += 1
                        elif _c == 'C':
                                num += char(c + _c)
                                i += 1
                        else:
                                num += char(c)
                elif c == 'L':
                        num += char(c)
                elif c == 'C':
                        if _c == 'D':
                                num += char(c + _c)
                                i += 1
                        elif _c == 'M':
                                num += char(c + _c)
                        else:
                                num += char(c)
                elif c == 'D':
                        num += char(c)
                elif c == 'M':
                        num += char(c)
        return num