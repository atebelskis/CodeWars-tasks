#https://www.codewars.com/kata/52fba66badcd10859f00097e/solutions/python

'''
def disemvowel(s):
    return s.translate(None,"aeiouAEIOU")
'''
def disemvowel(s):
    for i in 'aeuioAEUIO':
        s = s.replace(i, '')
    return s

print(disemvowel("Grazus ruduo"))


# https://www.codewars.com/kata/5a53a17bfd56cb9c14000003/train/python
def disarium_number(number):
    num = [int(x) for x in str(number)]
    suma = 0
    for i, x in enumerate(num, 1):
        suma += pow(x, i)
    if suma == number:
        return f'Disarium !!'
    else:
        return f'Not !!'

def disarium_number(n):
    return "Disarium !!" if n == sum(int(d)**i for i, d in enumerate(str(n), 1)) else "Not !!"

#https://www.codewars.com/kata/585a033e3a36cdc50a00011c/train/python
'''
test.assert_equals(freq_seq('hello world', '-'), '1-1-3-3-2-1-1-2-1-3-1')
        test.assert_equals(freq_seq('19999999',    ':'), '1:7:7:7:7:7:7:7')
        test.assert_equals(freq_seq('^^^**$',      'x'), '3x3x3x2x2x1')
'''
def freq_seq(s, sep):
    x = []
    for i in s:
        a = s.count(i)
        x.append(str(a))
    return sep.join(x)
print(freq_seq("varna", '='))

def freq_seq(s, sep):
    return sep.join([str(s.count(i)) for i in s])



# https://www.codewars.com/kata/6089c7992df556001253ba7d/train/python

'''
mount_moose = Song('Mount Moose', 'The Snazzy Moose')
# day 1 (or test 1)
mount_moose.how_many(['John', 'Fred', 'BOb', 'carl', 'RyAn']) => 5
# These are all new since they are the first listeners.
'''

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.klausyt = []

    def how_many(self,a):
        b = 0
        for i in a:
            if not i.upper() in self.klausyt:
                b += 1
                self.klausyt.append(i.upper())
        return b

''' seno tel klaviatura: https://www.codewars.com/kata/59564a286e595346de000079/train/python mobileKeyboard("codewars") => 26 (4+4+2+3+2+2+4+5) '''

def mobile_keyboard(s):
    a = [{'1':1}, {'2':1, 'a':2, 'b':3, 'c':4}, {'3':1, 'd':2, 'e':3, 'f':4},
        {'4':1, 'g':2, 'h':3, 'i':4}, {'5':1, 'j':2, 'k':3, 'l':4}, {'6':1, 'm':2, 'n':3, 'o':4},
        {'7':1, 'p':2, 'q':3, 'r':4, 's':5}, {'8':1, 't':2, 'u':3, 'v':4},
        {'9':1, 'w':2, 'x':3, 'y':4, 'z':5}]
    b = []
    for el in s:
        for i in a:
            for x,y in i.items():
                if x == el:
                    b.append(y)
    return sum(b)

''' vienas codewars sprendimu
def mobile_keyboard(s):
    lookup = {
        c: i 
        for s in "1,2abc,3def,4ghi,5jkl,6mno,7pqrs,8tuv,9wxyz,*,0,#".split(",") 
        for i, c in enumerate(s, start=1)
    }
    return sum(lookup[c] for c in s)
'''

# Professor Oak's Trouble - New Pokedex prototype    https://www.codewars.com/kata/57520361f2dac757360018ce/solutions/python


'''
integer_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
values_list = [1, 3]
l.remove_(integer_list, values_list) == [2, 2, 4]
'''
class List(object):
    def remove_(self, integer_list, values_list):
        return [i for i in integer_list if not i in values_list]





#    https://www.codewars.com/kata/53368a47e38700bd8300030d/solutions/python
'''
namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'
namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'
namelist([ {'name': 'Bart'} ])
# returns 'Bart'
namelist([])
# returns ''
'''

def namelist(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']



#  https://www.codewars.com/kata/582ba36cc1901399a70005fc/solutions/python
'''
var list1 = [
  { firstName: 'Maria', lastName: 'Y.', country: 'Cyprus', continent: 'Europe', age: 30, language: 'Java' },
  { firstName: 'Victoria', lastName: 'T.', country: 'Puerto Rico', continent: 'Americas', age: 70, language: 'Python' },
];
return : average oof ages;, round
'''


def get_average(lst):
    return round(sum(x["age"] for x in lst) / len(lst))

from operator import itemgetter
from statistics import mean
age = itemgetter("age")

def get_average2(lst):
    return round(mean(map(age, lst)))