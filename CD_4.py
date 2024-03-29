

#Jumping Number (Special Numbers Series #4)

#code wars sprendimai:

def jumping_number(number):
    arr = list(map(int, str(number)))
    return ('Not!!', 'Jumping!!')[all(map(lambda a, b: abs(a - b) == 1, arr, arr[1:]))]

def jumping_number2(number):
    digits = [int(char) for char in str(number)]
    if len(digits) == 1:
        return 'Jumping!!'
    else:
        deltas = (abs(x - y) for x, y in zip(digits, digits[1:]))
        return 'Jumping!!' if all(delta == 1 for delta in deltas) else 'Not!!'

def jumping_number3(number):
    digits = [int(n) for n in list(str(number))]
    for i in range(len(digits)-1):
        if abs(digits[i] - digits[i+1]) != 1:
            return 'Not!!'
    return 'Jumping!!'


def last_survivor(letters, coords):
    a = [i for i in letters]
    for i in coords:
        del a[i]

    return a

print(last_survivor('foiflxtpicahhkqjswjuyhmypkrdbwnmwbrrvdycqespfvdviucjoyvskltqaqirtjqulprjjoaiagobpftywabqjdmiofpsr', [8, 59, 52, 93, 21, 40, 88, 85, 59, 10, 82, 18, 74, 59, 51, 47, 75, 49, 23, 56, 1, 33, 39, 33, 34, 44, 25, 0, 51, 25, 36, 32, 57, 10, 57, 12, 51, 55, 24, 55, 31, 49, 6, 15, 10, 48, 27, 29, 38, 30, 35, 42, 23, 32, 9, 39, 39, 36, 8, 29, 2, 33, 14, 3, 13, 25, 9, 25, 18, 10, 1, 2, 20, 8, 2, 11, 5, 7, 0, 10, 10, 8, 12, 3, 5, 1, 7, 7, 5, 1, 4, 0, 4, 0, 0, 1]))