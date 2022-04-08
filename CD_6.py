#  Balanced Number (Special Numbers Series #1 )
def balanced_num(number):
    num = [int(i) for i in str(number)]
    at1 = len(num) // 2
    at2 = at1 + 1
    if len(num) <= 2:
        return "Balanced"
    elif len(num) % 2 == 0 and sum(num[:at1-1]) == sum(num[at2:]):
        print(num)
        return "Balanced"
    elif len(num) % 2 != 0 and sum(num[:at1]) == sum(num[at2:]):
        print(num)
        return "Balanced"
    else:
        print(num)
        return "Not Balanced"
'''
def balancedNum(n):
    s = str(n)
    l = (len(s)-1)//2
    same = len(s) < 3 or sum(map(int, s[:l])) == sum(map(int, s[-l:]))
    return "Balanced" if same else "Not Balanced"

balanced_num = balancedNum
'''

#   ___________________16+18=214________________________________________________

def add(num1, num2):
    num1_l = [int(x) for x in str(num1)]
    num2_l = [int(y) for y in str(num2)]
    rez = []
    if len(num2_l) == len(num1_l):
        for i, j in num1_l, num2_l:
            rez.append(i+j)
        return int(''.join(str(x) for x in rez))
    elif len(num1_l) > len(num2_l):
        d = len(num1_l) - len(num2_l)
        for i,j in num1_l[d:], num2_l:
            rez.append(i+j)
        return int(''.join(str(x) for x in num1_l[:d]) + ''.join(str(x) for x in rez))
    else:
        d = len(num2_l) - len(num1_l)
        for i, j in zip(num2_l[d:], num1_l):
            rez.append(i + j)
        return int(''.join(str(x) for x in num2_l[:d]) + ''.join(str(x) for x in rez))


print(add(416,2198))

#CD sprendimai:

def add1(a,b):
    s = ""
    while a+b:
        a,p = divmod(a,10)
        b,q = divmod(b,10)
        s = str(p+q)+s
    return int(s or'0')

def add2(*args):
    a, b = map(str, sorted(args))
    a = a.zfill(len(b))
    result = [int(x) + int(y) for x, y in zip(a, b)]
    return int("".join(map(str, result)))


class List:
    def __init__(self, type):
        self.type = type
        self.items = []
        self.count = 0

    def add(self, item):
        if type(item) != self.type:
            item_type = "str" if self.type == str else "int" if self.type == int else "float"
            return "This item is not of type: %s" % (item_type)
        elif type(item) == self.type:
            self.items += [item]
            self.count += 1
            return len(self.items)


list_ = List(str)
list_.add("Hello")
print(list_.add("Hello"))
print(list_.add(6))
print(list_.add("Hello"))     




#test.assert_equals(my_list.add(5), "This item is not of type: str", 'Wrong type added')
#test.assert_equals(my_list.add(' ').add('World!').count, 3, 'How many items in the List?')


def nb_year(p0, percent, aug, p):
    year = 0
    while p0 < p:
        p0 += p0 * (percent/100) + aug
        year += 1
    return year

print(nb_year(1000, 2.0, 50, 1214))