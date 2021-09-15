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
        i = 0
        flag = 0
        if type(roman_string) != str or roman_string == None or roman_string == "":
                return None
        
        while len(roman_string) > i:
                c = roman_string[i]
                if len(roman_string) > i + 1:
                        _c = roman_string[i + 1]
                else: 
                        _c = " "

                if c == 'I':
                        print(flag)
                        if flag == 3:
                                return None
                        if _c == 'V':
                                num += char(c + _c)
                                i += 1
                        elif _c == 'X':
                                num += char(c + _c)
                                i += 1
                        else:
                                num += char(c)
                        flag += 1
                elif c == 'V':
                        num += char(c)
                        flag = 0
                elif c == 'X':
                        if _c == 'L':
                                num += char(c + _c)
                                i += 1
                        elif _c == 'C':
                                num += char(c + _c)
                                i += 1
                        else:
                                num += char(c)
                        flag = 0
                elif c == 'L':
                        num += char(c)
                        flag = 0
                elif c == 'C':
                        if _c == 'D':
                                num += char(c + _c)
                                i += 1
                        elif _c == 'M':
                                num += char(c + _c)
                                i += 1
                        else:
                                num += char(c)
                        flag = 0
                elif c == 'D':
                        num += char(c)
                        flag = 0
                elif c == 'M':
                        num += char(c)
                        flag = 0
                i += 1
        return num