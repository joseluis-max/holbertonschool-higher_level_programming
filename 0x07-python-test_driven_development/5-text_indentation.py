#!/usr/bin/python3
""" 
Test-driven development
    text_indentation - Arg: 
        text: str
"""

def text_indentation(text):
    """
    Put double \n after :, ?, .
    """
    if type(text) is str:
        for i in range(len(text)):
            if text[i] in [".", "?", ":"]:
                print(text[i], end="")
                print("\n")
            else:
                if text[i - 1] not in [".", "?", ":"]:
                    print(text[i], end="")
    else:
        raise TypeError("text must be a string")
