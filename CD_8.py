def count_checkerboard(width, height, r):
    a = 0
    b = 0
    liekana = width - int(width/r)*r
    liekana2 = height - int(height / r) * r

    if liekana == 0:
        for i in range(r+1, width+1, r):
            a += r
    '''
    if width % r == 0:
        for i in range(int(width/r)+1):
        if i % 2 != 0:
            for x in range(resolution+1, width+1, resolution):
                a += 1
        elif i % 2 == 0:
            for x in range(1, width + 1, resolution):
                a += 1
    '''
    return a

print(count_checkerboard(15,6,3))
#assert  count_checkerboard(11,6,2) == 32

'''
def count_checkerboard(width, height, r):
    a = 0
    b = 0
    if width % r == 0:
        for i in range(int(width/r)+1):
        if i % 2 != 0:
            for x in range(resolution+1, width+1, resolution):
                a += 1
        elif i % 2 == 0:
            for x in range(1, width + 1, resolution):
                a += 1
    return a
'''

import re
#surasti skliaustelius teisingus:
def valid_braces(string):
    temp = ['\(\)', '\{}', '\[]']

    for n in range(len(string)):
        for i in temp:
            if re.search(i, string):
                print(string)
                string = re.sub(i, '', string, 1)
                #string = string.replace(i, '')
                print(string)
    if len(string) ==0:
        return True
    else:
        return False

print(valid_braces('([{}])'))
print(valid_braces('(){}['))

'''
def validBraces(string):
    while '()' in string or '{}' in string or '[]' in string:
        string = string.replace('()', '')
        string = string.replace('{}', '')
        string = string.replace('[]', '')
    return False if len(string) != 0 else True
'''

class Objektas:
    pass