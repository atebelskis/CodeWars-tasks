from operator import itemgetter

def scoreboard(waw):
    b=[]
    for i in waw:
        #for key,item in i.items():
        d = {'name': i.get('name'), 'score': i.get("chickenwings",0) * 5 + i.get("hamburgers",0) * 3 + i.get("hotdogs",0)*2}
        b.append(d)
    b_sorted = sorted(b, key=itemgetter('score'), reverse=True)
    return b_sorted
            #a = key["chickenwings"] * 5 + key["hamburgers"] * 3 + key["hotdogs"] *2
            #waw['chickenwings'] * 5
            #i = {waw["name"], waw["chickenwings"] * 5, waw["hamburgers"] * 3, waw["hotdogs"] *2}
            #key == "chickenwings"
            #a += item*5
            #key == "hamburgers"
            #a += item*3
            #return a

# waw["chickenwings"] * 5, waw["hamburgers"] * 3, waw['hotdogs'] * 2
'''   
    for i in who_ate_what:
        if i["chickenwings"]:
            b.append(i.item*10)
        elif i == "hamburgers":
            b.append(x*4)
        elif i == 'hotdogs':
            b.append(x*4)
'''

# return f'{who_ate_what.key[0]}: {sum(b)}'


letters = {"a": 1, "b": 2}
print(letters.get("b"))

print(scoreboard([{"name": "Big Bob", "chickenwings": 2, "hamburgers": 4, "hotdogs": 11},
                 {"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15}]))


def balanced_num(number):
    num = [i for i in str(number)]
    if len(num) <= 2:
        return f"Balanced"
    elif len(num) % 2 == 0:
        pivot_1 = num[len(num) / 2]
        pivot_2 = num[pivot_1 + 1]
        return pivot_2
