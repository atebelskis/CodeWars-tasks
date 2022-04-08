def divid(a):
        return a/2



print(divid(2))

#def zem(b):
    #return [map(divid, b)]
b = [2,4,6,23,40]
c = list(map(divid, b))

print(c)

l = ['sat', 'bat', 'cat', 'mat']

# map() can listify the list of strings individually
test = list(map(list, l))
print(test)


s = 'qewqewqeqeqwewqytrytryryryrytrrrrrrrrrrrrrrrrrrrrrrrrrr'
str_list = list(map(lambda x: x+'a', s))

print(str_list)
l = 'x'
def replac_(s):
    for y,i in enumerate(s):
        s = s.replace(s[y], l)
    return s

print(replac_(s))


