
#a

empty_set = set()
print(empty_set)
print(type(empty_set))
print( )

even_numbers = {0, 2, 4, 6, 8}
print(even_numbers)
print(type(even_numbers))
print( )

#b

W = set( 'programowanie' )
print(W)
print(type(W))
print( )

#c

W = set( ['Ala', 'Basia', 'Czarek', 'Darek'] )
print(W)
print(type(W))
print( )

#d

W = set( ['Ala', 'Basia', 'Czarek', 'Darek'] )
print(len(W))
print(W)
print(type(W))
print( )

#e
# różne typy wejściowe, ten sam output
# Using a tuple
W = set((1, 2, 3))
print(len(W))  # Outputs: 3
print(W)  # Outputs: {1, 2, 3}
print(type(W))  # Outputs: <class 'set'>
print("()")  
print()

# Using a list
W = set([1, 2, 3])
print(len(W))  # Outputs: 3
print(W)  # Outputs: {1, 2, 3}
print(type(W))  # Outputs: <class 'set'>
print("[]")  
print()

# Using a set
W = set({1, 2, 3})
print(len(W))  # Outputs: 3
print(W)  # Outputs: {1, 2, 3}
print(type(W))  # Outputs: <class 'set'>
print("{}")  
print()

#f

W = set((1,2,3))
print(len(W))
print(W)

W.remove(3)
print(len(W))
print(W)
print( )

#g

# Using a tuple
furniture = set(('sofa', 'fotel', 'stół'))
for piece in furniture:
    print(piece)
print()

# Using a list
furniture = set(['sofa', 'fotel', 'stół'])
for piece in furniture:
    print(piece)
print()

# Using a set
furniture = set({'sofa', 'fotel', 'stół'})
for piece in furniture:
    print(piece)
print()

#h

W = set( 'programowanie' )
print(len(W)) # Wycięte te które się powtarzają
print(len( 'programowanie' ))
print(W)
print(type(W))
print( )

W = set( {'jabłko': 'czerwone', 'pomarańcza': 'pomarańczowa', 'wiśnia': 'czerwona'} )
{'jabłko', 'pomarańcza', 'wiśnia'}

print(len(W))
print(W)
print(type(W))
print( )

names = set( ['Ala', 'Basia', 'Czarek', 'Darek'] )
print(len(names))

#i

s = set((1,2,3))
print(s)
print(len(s))
print( )

s.add(4)
print(s)
print(len(s))
print( )

s.remove(3)
print(s)
print(len(s))
print( )

#j

furniture = set(('sofa', 'fotel', 'stół'))
for piece in furniture:
    print(piece)

print( )

#k


drinks = {
'martini': {'wódka', 'wermut'},
'czarny rosjanin': {'wódka', 'likier'},
'biały rosjanin': {'śmietanka', 'likier', 'wódka'},
'manhattan': {'whisky', 'wermut', 'gorzka nalewka'},
'screwdriver': {'sok pomarańczowy', 'wódka'}
}

print(drinks.items())
print(len(drinks.items()))

for name, contents in drinks.items():
    if 'wódka' in contents:
        print(name)

print( )

for name, contents in drinks.items():
    if 'wódka' in contents and not ('wermut' in contents or 'śmietanka' in contents):
        print(name)

print( )

for name, contents in drinks.items():
    if contents & {'wermut', 'sok pomarańczowy'}:
        print(name)
print( )

for name, contents in drinks.items():
    if 'wódka' in contents and not contents & {'wermut', 'śmietanka'}:
        print(name)

bruss = drinks['czarny rosjanin']
wruss = drinks['biały rosjanin']
print(drinks.items())
print(len(drinks.items()))
print( )

#l

a = {1, 2}
b = {2, 3}

print(a & b)
print(a.intersection(b))
print( )

print( bruss & wruss)
print(type(print( bruss & wruss)))
print( )

print( a| b)
print(a.union(b))
print( )

print( bruss | wruss)
print( )

#m

a = {1, 2}
b = {2, 3}

print(a - b)
print(a.difference(b))
print( )

print(bruss - wruss)
print(wruss-bruss)
print( )

#n

#symmetric_difference():
print( a ^ b)
print()

print(a.symmetric_difference(b))
print( )

print(bruss ^ wruss)
print(wruss ^ bruss)
print( )

#m

a = {1, 2}
b = {2, 3}

print( a<= b)
print(a.issubset(b))
print( )

print(bruss <= wruss)
print( )

print(a <= a)
print(a.issubset(a))
print( )

print(a < b)
print(a < a)
print(bruss < wruss)
print( )

print( a >= b)

#o

furniture = set(['sofa', 'fotel', 'stół'])
print(furniture)
furniture.add(4)
print(furniture)
print( )


#furniture = frozenset(['sofa', 'fotel', 'stół']) #wyskakuje błąd
#print(furniture)
#f\urniture.add(4)
#print(furniture)
#print( )



