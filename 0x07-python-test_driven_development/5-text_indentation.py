#!/usr/bin/python3
def text_indentation(text):
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
