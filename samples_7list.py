
#a
empty_list = [ ]
print(type(empty_list))
print(len(empty_list))

weekdays = ['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek']
print(type(weekdays))
print(len(weekdays))

big_birds = ['emu', 'struś', 'kazuar']
print(type(big_birds))
print(len(big_birds))

first_names = ['Jan', 'Joanna', 'Tomasz', 'Tomasz', 'Monika']
print(type(first_names))
print(len(first_names))

leap_years = [2000, 2004, 2008]
print(type(leap_years))
print(len(leap_years))

randomness = ['Warszawa', {"pies": "Reksio"}, "2 lutego"]
print(type(randomness))
print(len(randomness))
print( )

#b
another_empty_list = list()

print(type(another_empty_list))
print(len(another_empty_list))

#c
a = list('kot')
print(type(a))
print(a)
print( )

#d
a_tuple = ('raz', 'dwa', 'trzy')
print(type(a_tuple))
a_list = list(a_tuple)

print(type(a_list))
print( )

#e

talk_like_a_pirate_day = '2019-09-19'
a = talk_like_a_pirate_day.split('-')
print(a)
print(type(a))
print(len(a))
print( )

#f
splitme = 'a/b//c/d///e'
b = splitme.split('/')
print(b)
print(type(b))
print(len(b))
print( )

#g
splitme = 'a/b//c/d///e'
c = splitme.split('//')
print(c)
print(type(c))
print(len(c))
print( )

#h
marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes[0])

print(marxes[1])

print(marxes[2])

# ujemne
print(marxes[-1])

print(marxes[-2])

print(marxes[-3])
print( )

#i

marxes = ['Groucho', 'Chico', 'Harpo']
d = marxes[0:2]
print(d)
print(type(d))
print(len(d))
print( )

#j

marxes = ['Groucho', 'Chico', 'Harpo', '1Groucho', '1Chico', '1Harpo']
e = marxes[::2]
print(e)
print(type(e))
print(len(e))
print( )

#k

marxes = ['Groucho', 'Chico', 'Harpo', '1Groucho', '1Chico', '1Harpo']
f = marxes[::-2] # dla mnie dziwne ze od el 0 nie liczone
print(f)
print(type(f))
print(len(f))
print( )


#l

marxes = ['Groucho', 'Chico', 'Harpo', '1Groucho', '1Chico', '1Harpo']
g = marxes[::-1]
print(g)
print(type(g))
print(len(g))
print( )

#m

marxes = ['Groucho', 'Chico', 'Harpo', '1Groucho', '1Chico', '1Harpo']
marxes.reverse()
print(marxes)
print(type(marxes))
print(len(marxes))
print( )

#n

marxes = ['Groucho', 'Chico', 'Harpo', '1Groucho', '1Chico', '1Harpo']
h = marxes[6:]
print(h)
print(type(h))
print(len(h))
print( )


#o

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.append('Zeppo')

print(marxes)
print(type(marxes))
print(len(marxes))
print( )

#p

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(2, 'Gummo')
print(marxes)
print(type(marxes))
print(len(marxes))
print( )

#r

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.insert(9, 'Gummo')
print(marxes)
print(type(marxes))
print(len(marxes))
print( )

#s

i = ["blah"] * 3
print(i)
print(type(i))
print(len(i))
print( )

#t
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
print(marxes)
print(type(marxes))
print(len(marxes))
print( )

#u

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
print(marxes)
print(type(marxes))
print(len(marxes))
print( )

#v

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
print(marxes)
print(type(marxes))
print(len(marxes))
print( )

#w

numbers = [1, 2, 3, 4]
numbers[1:3] = [8, 9]
print(numbers)
print(type(numbers))
print(len(numbers))
print( )

#x
numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9, 10, 11]
print(numbers)
print(type(numbers))
print(len(numbers))
print( )

#y

numbers = [1, 2, 3, 4]
numbers[1:3] = (98, 99, 100) #wrzucił krotkę?
print(numbers)
print(type(numbers))
print(len(numbers))
print( )

numbers = [1, 2, 3, 4] 
numbers[1:3] = 'co?' #kazda litera osobno? no tak
print(numbers)
print(type(numbers))
print(len(numbers))
print( )

numbers = [1, 2, 3, 4] 
numbers[1:3] = ('co?',) #a tak jako krotka,,,,
print(numbers)
print(type(numbers))
print(len(numbers))
print( )

#z

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
print(len(marxes))
del marxes[-1]
print(marxes)
print(type(marxes))
print(len(marxes))
print( )

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Karl']
print(len(marxes))
del marxes[1]
print(marxes)
print(type(marxes))
print(len(marxes))
print( )

# """Słowo del jest instrukcją, a nie funkcją.
#  Nie można użyć zapisu marxes[-1].del().Instrukcja ta jest swego rodzaju odwróconym przypisaniem,
#  tj. odłącza obiekt od nazwy i jeżeli nie jest on skojarzony z inną nazwą, zwalnia zajmowaną przez niego pamięć."""""


#za

marxes = ['Groucho', 'Chico', 'Groucho', 'Harpo']
print(len(marxes))
marxes.remove('Groucho')
print(marxes)
print(type(marxes))
print(len(marxes))
print( )

#zb
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
print(len(marxes))
marxes.pop()
print(marxes)
print(type(marxes))
print(len(marxes))
print( )

#Czas na trochę fachowego żargonu. Dodając do końca listy kolejne elementy za pomocą
#funkcji append() i usuwając je za pomocą pop(), implementuje się kolejkę LIFO
#(ang. Last-In, First-Out — ostatni wchodzi, pierwszy wychodzi), bardziej znaną
#pod pojęciem stosu. Natomiast za pomocą funkcji pop(0) tworzy się kolejkę FIFO
#(ang. First-In, First-Out — pierwszy wchodzi, pierwszy wychodzi). Struktury te 
#wykorzystuje się do gromadzenia danych i przetwarzania ich, począwszy od najstarszych (FIFO) lub najnowszych (LIFO).

#zc

work_quotes = ['Masz chwilę?', 'Szybkie pytanie!', 'Na wczoraj!']
print(work_quotes)
print(len(work_quotes))

work_quotes.clear()
print(len(work_quotes))
print( )

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo'] #sposób wywołania
marxes.index('Chico')
print(marxes.index('Chico'))

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
position_of_chico = marxes.index('Chico')
print(position_of_chico)
print( )

#zd
marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo'] #sposób wywołania
print('Groucho' in marxes)

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
is_present = 'Groucho' in marxes
print(is_present)
print( )


#ze

marxes = ['Groucho', 'Chico', 'Harpo'] #sposób wywołania
print(marxes.count('Harpo'))

marxes = ['Groucho', 'Chico', 'Harpo']
how_many = marxes.count('Harpo')
print(how_many)
print( )

#zf

marxes = ['Groucho', 'Chico', 'Harpo'] #wydarzyło się tu coś wogóle? str 117
print(len(marxes))
print(type(marxes))

joijn = ', '.join(marxes)
print(joijn)

print(len(marxes))
print(type(marxes))
      
print( )


marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes))
print(type(marxes))

print(', '.join(marxes))
print(joijn)

print(len(marxes))
print(type(marxes))
      
print( )

#zg

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes)
sorted_marxes = sorted(marxes)
print(sorted_marxes)
print( )

marxes = ['Groucho', 'Chico', 'Harpo']
print(marxes)
marxes.sort()
print(marxes)
print( )

#zh

numbers = [2, 1, 4.1, 3] #W takich przypadkach dane są automatycznie przekształcane w obiekty jednego typu: no chyba nie
print(numbers)
numbers.sort()
print(numbers)
print( )


numbers = [2, 1, 4.1, 3] #W takich przypadkach dane są automatycznie przekształcane w obiekty jednego typu: no chyba nie
print(numbers)
numbers.sort(reverse = True)
print(numbers)
print( )

#zi

marxes = ['Groucho', 'Chico', 'Harpo']
print(len(marxes))
print( )

#zj

a = [1, 2, 3]
print(a)
b = a
print(b)

a[0] = 'niespodzianka'
print(a)
print(b)
#b.sort(reverse = True)
#print(b)
print()

#zk

a = [1, 2, 3]
b = a.copy()
print(b)

c = list(a)
print(c)

d = a[:]
print(d)
print( )

#zl

a = [1, 2, [8, 9]]
b = a.copy()
print(b)

c = list(a)
print(c)

d = a[:]
print(d)
print( )

a = [1, 2, [8, 9]]
a [2][1] = 10
b = a.copy()
print(b)

c = list(a)
print(c)

d = a[:]
print(d)

#zm

import copy
a = [1, 2, [8, 9]]
b = copy.deepcopy(a)
print( )
print(a)
print(b)
print( )

a = [7, 2]
b = [7, 2, 9]
print(a == b)
print(a <= b)
print(a < b)
print( )

#zn

cheeses = ['topiony', 'żółty', 'pleśniowy']
for i in cheeses:
    print(i)
print( )

# Jak poprzednio instrukcja break powoduje przerwanie pętli, a continue — wykonanie następnej
#iteracji:

cheeses = ['topiony', 'żółty', 'pleśniowy']
for cheese in cheeses:
    if cheese.startswith('ż'):
        print("Nie jem niczego, co się zaczyna na 'ż'")
        break
    else:
        print(cheese)



#ZO

days = ['poniedziałek', 'wtorek', 'środa']
fruits = ['banan', 'pomarańcza', 'brzoskwinia']
drinks = ['kawa', 'herbata', 'piwo']
desserts = ['tiramisu', 'lody', 'ciasto', 'sernik']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": do picia -", drink, "- do jedzenia", fruit, "- na deser", dessert)

print( )


days = ['poniedziałek', 'wtorek', 'środa']
fruits = ['banan', 'pomarańcza', 'brzoskwinia']
drinks = ['kawa', 'herbata', 'piwo']
desserts = ['tiramisu', 'lody', 'ciasto', 'sernik']
for d, f, r, e in zip(days, fruits, drinks, desserts):
    print(d, ": do picia -", f, "- do jedzenia", r, "- na deser", e) # skrócenie 


#zp
polish = 'poniedziałek', 'wtorek', 'środa'
print(type(polish))
french = 'lundi', 'mardi', 'mercredi'
print(type(french))

list(zip(polish, french))
print(type(list(zip(polish, french))))
print(list(zip(polish, french)))
print( )


polish = 'poniedziałek', 'wtorek', 'środa'
french = 'lundi', 'mardi', 'mercredi'
dict(zip(polish, french))
print(type(dict(zip(polish, french))))
print( )

#zr

number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)
print(type(number_list))
print( )

#zs

number_list = []
for number in range(1,6):
    number_list.append(number)

print(number_list)
print(type(number_list))
print( )

#zt

number_list = list(range(1, 6))
print(type(number_list))
print( )

number_list = [i for i in range(1,6)]
print(number_list)
print( )


number_list = [i-2 for i in range(1,6)] #strona 123
print(number_list)
print( )

a_list = [i for i in range(1,6) if i % 2 == 1]
print(a_list)
print( )

a_list = []
for number in range(1,6):
    if number % 2 == 1:
        a_list.append(number)

print(a_list)
print()

rows = range(1,4)
cols = range(1,3)

for row in rows:
    for col in cols:
        print(row, col)

print( )

rows = range(1,4)
cols = range(1,3)

cells = [(row, col) for row in rows for col in cols] #str 125
for cell in cells:
    print(cell)

print( )

#zu

small_birds = ['koliber', 'wróbel']
extinct_birds = ['dodo', 'gołąb wędrowny', 'nestor skalny']
carol_birds = [3, 'kura', 2, 'turkawka']
all_birds = [small_birds, extinct_birds, 'papuga', carol_birds]

print(all_birds)
print( )

print(all_birds[0])
print(all_birds[1][0])

#zv

