
#a

empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))
print( )

#b
one_marx = 'Grouch',
print(one_marx)
print(type(one_marx))
print( )

#c
one_marx = ('Groucho',)
print(one_marx)
print(type(one_marx))
print( )

#d without coma ,

one_marx = ('Groucho')
print(one_marx)
print(type(one_marx))
print( )

#e
marx_tuple = ('Groucho', 'Chico', 'Harpo')
print(marx_tuple)
print(type(marx_tuple))
print( )

#f

marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print( )

#g

password = 'swordfish',
print(type(password))
print(password)
print( )
icecream = 'tuttifrutti',
print(type(icecream))
print(icecream)
print( )

#h

marx_list = ['Groucho', 'Chico', 'Harpo']
print(type(marx_list))
print(marx_list)
print( )
marx_tuple = tuple(marx_list)
print(type(marx_tuple))
print(marx_list)
print( )

#i
m = ('Groucho',) + ('Chico', 'Harpo')
print(m)
print(type(m))
print( )

#j
n = ('yada',) * 3
print(n)
print(type(n))
print( )

#k

a = (7, 2)
b = (7, 2, 9)
print(a == b)
print(a <= b)
print(a < b)
print( )

#j

words = ('głowa', 'pełna', 'pomysłów')
print(type(words))

for i in words:
    print(i)

print( )

#k

t1 = ('Fee', 'Fie', 'Foe')
print(type(t1))
print(id(t1))
t2 = ('Flop',)
print(type(t2))
t1 = t1 + t2
print(id(t1))
print(t1)
print( )