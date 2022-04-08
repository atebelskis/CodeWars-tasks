import re

def uncollapse(digits):
    b = []
    temper = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    while len(digits) != 0:
        for i in temper:
            if re.match(i, digits):
                b.append(i)
                digits = re.sub(i, '', digits, 1)
    return ' '.join(b)

print(uncollapse("fivethreefivesixthreenineonesevenoneeight"))

def finance(n):
    b=[]
    for i in range(n):
        a = sum(range(i+2, n+i))
        b.append(a)
    return b

print(finance(6))

import re

def solution(roman):
    temp_1 = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    temp_2 = {'IV': -2, 'IX': -2, 'XL': -20, 'XC':-20, 'CD':-200, 'CM':-200}
    sum = 0
    for key in temp_1:
        for i in roman:
            if i == key:
                sum += temp_1.get(i)
    for i in temp_2:

        if re.search(i, roman):
            sum += temp_2.get(i)
    return sum

print(solution('IV'))


def xmastree(n):
    t = [i for i in range(n+1)]
    t_2 = []
    tree = []
    for i in t:
        if i != 0:
            t_2.append(t[i]+t[i-1])
    for i in t_2:
        a = int((t_2[-1] - i)/2)
        part = '_'*a+'#'*i+'_'*a
        tree.append(part)
    b = int((t_2[-1]-1)/2)
    part_2 = '_'*b+'#'+'_'*b
    tree.append(part_2)
    tree.append(part_2)
    return tree

import math

def convert(degrees):
    #frac, whole = math.modf(degrees)
    #return frac, whole
    a = int(degrees)
    b = degrees - a
    degr = int(a)
    minut = int(round((b*60),4))
    sec = round(((b*60-minut)*60))
    return [degr, minut, sec]

print(convert(0.0001398888888888889))
print(convert(91.33333333333333))
';;'