file = open('puzzle.txt', 'r')
string = file.read()
file.close()


# Task number 1
def step1():
    global string

    def f(sym):
        if sym == '%':
            return 'k'
        return sym
    string = ''.join(list(map(f, string)))


# Task number 2
def step2():
    global string
    cache = {'delete': False}

    def f(sym):
        if cache['delete']:
            cache['delete'] = False
            return False
        if sym == 'z':
            cache['delete'] = True
        return True
    string = ''.join(list(filter(f, string)))


# Task number 3
def step3():
    global string

    def f(sym):
        if sym == '#':
            return 'e'
        return sym
    string = ''.join(list(map(f, string)))


# Task number 4
def step4():
    global string
    cache = {'even': True, 'last_sym': '', 'index': -1}

    def f(sym):
        cache['index'] += 1
        cache['even'] = not cache['even']
        if cache['even']:
            return cache['last_sym']
        cache['last_sym'] = sym
        return string[cache['index'] + 1]
    string = ''.join(list(map(f, string)))


# Task number 5
def step5():
    global string

    def f(sym):
        if sym == '&':
            return False
        return True
    string = ''.join(list(filter(f, string)))


# Task number 6
def step6():
    global string

    def f(sym):
        if sym == '*':
            return False
        return True
    string = ''.join(list(filter(f, string)))


# Task number 7
def step7():
    global string
    cache = {'delete': False}

    def f(sym):
        if sym == '.':
            cache['delete'] = True
            return False
        return cache['delete']
    string = ''.join(list(filter(f, string)))


# Task number 8
def step8():
    global string
    cache = {'index': 0}

    def f(sym):
        cache['index'] += 1
        if cache['index'] % 3:
            return False
        return True
    string = ''.join(list(filter(f, string)))

i = 0
step1()
i += 1
print(string + ' :'+ str(i) +': ' + str(len(string)) + '\n\n')

step2()
i += 1
print(string + ' :'+ str(i) +': ' + str(len(string)) + '\n\n')

step3()
i += 1
print(string + ' :'+ str(i) +': ' + str(len(string)) + '\n\n')

step4()
i += 1
print(string + ' :'+ str(i) +': ' + str(len(string)) + '\n\n')

step5()
i += 1
print(string + ' :'+ str(i) +': ' + str(len(string)) + '\n\n')

step6()
i += 1
print(string + ' :'+ str(i) +': ' + str(len(string)) + '\n\n')

step7()
i += 1
print(string + ' :'+ str(i) +': ' + str(len(string)) + '\n\n')

step8()
i += 1
print(string + ' :'+ str(i) +': ' + str(len(string)) + '\n\n')
