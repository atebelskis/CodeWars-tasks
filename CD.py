# Code Wars
def check_exam(arr1, arr2):
    arr3 = []
    for i, a in zip(arr1, arr2):
        if i == a:
            arr3.append(4)
        elif i == '' or a == '':
            arr3.append(0)
        elif i != a:
            arr3.append(-1)
    suma = sum(arr3)
    if suma < 0:
        return 0
    else:
        return suma


# ____________________________________________________
# _____________________________________________________

def define_suit(card):
    if card.count('C'):
        return 'clubs'
    if card.count('S'):
        return 'spades'
    if card.count('D'):
        return 'diamonds'
    if card.count('H'):
        return 'hearts'


print(define_suit('10H'))
#____________________________
def define_suit(card):
    d = {'C': 'clubs', 'S':'spades', 'D':'diamonds','H':'hearts'}
    return d[card[-1]]


# ________________________________________________________
# https://www.codewars.com/kata/5865918c6b569962950002a1/train/python
def str_count(strng, letter):
    return strng.count(letter)

# https://www.codewars.com/kata/570e8ec4127ad143660001fd/train/python
def billboard(name, price=30):
    suma = 0
    for i in name:
        suma += price
    return suma
print(billboard('alfa teb', 30))

#https://www.codewars.com/kata/545afd0761aa4c3055001386/train/python
def take(arr,n):
    rez = []
    for i,x in enumerate(arr, 1):
        if i <= n:
            rez.append(x)
    return rez

    #sprendimas:
def take(arr,n):
    return list(arr[i] for i in range(0, n, 1)) if len(arr) >= n else arr

    #sprendimas:
def take(arr, n):
    return arr[:n]

print(take([2, 4, 6, 10], 2))

#https://www.codewars.com/kata/56bcaedfcf6b7f2125001118/train/python
def html_special_chars(data):
    return data.replace('&', '&amp').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot')

print(html_special_chars('>6654<'))


#https://www.codewars.com/kata/5761a717780f8950ce001473/solutions/python
def calculate_age(year_of_birth, current_year):
    year = (year_of_birth - current_year)
    c1 = f"You are {abs(year)} {['year','years'][abs(year)!=1]} old."
    c2 = f"You will be born in {year} {['year','years'][year!=1]}."
    return 'You were born this very year!' if not year else [c1,c2][year >0 ]


def distinct(seq):
    a = set(seq)
    b = []
    for i in a:
        b.append(i)
    return b
print(distinct([1, 1, 2, 3]))

def hello(name):
    if name == () or name == "":
        return f"Hello, World!"
    else:
        return f"Hello, {name.capitalize()}!"


#https://www.codewars.com/kata/50654ddff44f800200000007/train/python

def solution(a, b):
    short, long = sorted((a, b), key=len)
    return short + long + short

#https://www.codewars.com/kata/57ab3c09bb994429df000a4a/train/python

def two_highest(arg1):
    return sorted(set(arg1), reverse=True)[:2]

#  https://www.codewars.com/kata/55ecd718f46fba02e5000029/solutions/python

def between(a,b):
    x = []
    c = b + 1
    while a < c:
        x.append(a)
        a += 1
    return x
print(between(3, 19))

#https://www.codewars.com/kata/56853c44b295170b73000007/solutions/python   Are they square?
import math

#sprendimai CD
def is_square(arr):
    a = [(i ** 0.5).is_integer() for i in arr]
    if False in a:
        return False
    elif not a:
        return None
    else:
        return True

def is_square(arr):
    if arr:
        return all((a ** 0.5).is_integer() for a in arr)

def is_square(a):
    if a:
        return all(isqrt(x)**2 == x for x in a)

import array
def fix_the_meerkat(arr):
    arr.reverse()
    return arr

print(fix_the_meerkat(['a', 'b', 'c']))

class Color:
    name: str
    code: str

    def __init__(self, name, code):
        self.name = name
        self.code = code

class Animal:
    name: str
    weight: float
    heigh: float
    color: Color

    def __init__(self, name, weight, heigh, color):
        self.name = name
        self.weight = weight
        self.heigh = heigh
        self.color = color

class Dog(Animal):
    kind: str = 'dog'

class Cat(Animal):
    kind: str = 'cat'

brown = Color('brown', '4453')
bob = Animal('Bob', 15, 60, brown)

print(bob.name)
print(bob.weight)
print(bob.color.code)



