#8.1
p2e ={"pies" : "dog", "kot" : "cat", "mors" : "walrus"}

print(p2e.items())
print(type(p2e))

#8.2

print(p2e["mors"])

#8.3
#how?

p2e = {"pies": "dog", "kot": "cat", "mors": "walrus"}
e2p = {value: key for key, value in p2e.items()}
print(e2p)

p2e = {"pies" : "dog", "kot" : "cat", "mors" : "walrus"}


e2p = {}
for polish, english in p2e.items():
    e2p[english] = polish
print(e2p)

print(e2p)
print( )

#8.4
print(e2p['cat'])

#8.5

print(p2e.keys())

#8.6

life = {'zwierzęta': {'koty': ['Filemon', 'Bonifacy', 'Klakier'],'psy': {},'ptaki': {}},
         'rośliny': {},
         'inne': {}
         }

print( )
#8.7

print(life.keys())
print( )

#8.8

print(life['zwierzęta'].keys())
print( )

#8.9

print(life['zwierzęta']['koty'])
print( )

#8.10

squares = {x: x**2 for x in range(10)}
print(squares)
print( )

#8.11

odd = {x for x in range(10) if x % 2 != 0}
print(odd)
print( )

#8.12

# Wyrażenie generatorowe
generator = ('Liczba ' + str(x) for x in range(10))

# Wyświetlanie wartości zwróconych przez generator
for value in generator:
    print(value)

print( )