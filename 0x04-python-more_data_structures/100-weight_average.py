#!/usr/bin/python3

def weight_average(my_list=[]):
        sum = 0
        sum2 = 0

        if my_list == []:
                return 0

        _list = list(map(lambda x: x[0] * x[1], my_list))
        _list2 = list(map(lambda x: x[1], my_list))
        for i in _list:
                sum += i
        for j in _list2:
                sum2 += j
        
        return (sum / sum2)