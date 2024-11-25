
#a

def do_nothing():
    pass

do_nothing()
print( )


def make_a_sound():
    print('Hej!')

make_a_sound()
print( )

def agree():
    return True

agree() #nie wyświetla, bo zwraca tylko w returnie
print(agree()) 
print( )

def agree():
    return False

if agree():
    print('Super!')
else:
    print('A to niespodzianka.')

#b

def echo(anything):
    return anything + ' ' + anything

print(echo('Test'))
print( )

#c

def commentary(color):
    if color == 'czerwony':
        return 'To jest pomidor'
    elif color == 'zielony':
        return 'To jest ogórek'
    elif color == 'ultrafioletowy':
        return 'co to?'
    else:
        return 'Nie znam koloru ' + color + '.'
    

print(commentary('zielony'))
print( )

#d

thing = None #albo True False
if thing:
    print('Jakaś wartość')
else:
    print('Brak wartości')

#e

def whatis(thing):
    if thing is None:
        print(thing, 'to None')
    elif thing:
        print(thing, 'to True')
    else:
        print(thing, 'to False')

whatis(None)
print(whatis(None)) # bo nie ma Return

#f

def menu(wine, entree, dessert):
    return {'wino': wine, 'danie główne': entree, 'deser': dessert}

print(menu('chardonnay', 'kurczak', 'ciasto')) # czemu muszę print - bo zwraca returnem i tego nie widać
print( )

print(menu('pieczeń', 'bajgiel', 'bordeaux')) # na innej pozycji

#g

def menu(wine, entree, dessert):
    return {'wino': wine, 'danie główne': entree, 'deser': dessert}

print(menu('chardonnay', 'kurczak', 'ciasto')) # czemu muszę print
print( )

print(menu('pieczeń', 'bajgiel', 'bordeaux')) # na innej pozycji
print( )

print(menu(entree='pieczeń', dessert='bajgiel', wine='bordeaux'))
print( )

print(menu('frontenac', dessert='tarta', entree='ryba'))
print( )

#h

def menu(wine, entree, dessert ='budyń'):
    return {'wino': wine, 'danie głowne': entree, 'deser': dessert}

print(menu('chardonnay', 'kurczak'))
print( )

print(menu('dunkelfelder', 'kaczka', 'pączek'))
print( )

#i 154

def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')
buggy('b')
buggy('a')
buggy('b')
print( )

# bez akumulacji danych

def works(arg):
    result = []
    result.append(arg)
    return result

works('a')
works('b')
works('a')
works('b')
print(works('a'))
print(works('b'))
print(works('a'))
print(works('b'))

print( )

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

nonbuggy('a')
nonbuggy('b')
nonbuggy('a')
nonbuggy('b')
print( )
#print(nonbuggy('a'))
#print(nonbuggy('b'))

#j 155

def print_args(*args):
    print('Krotka z argumentami pozycyjnymi:', args)

print_args()
    
print( )

def print_args(*args):
    print('Krotka z argumentami pozycyjnymi:', args)

print_args(3,2,1, 'raz', 'dwa')


