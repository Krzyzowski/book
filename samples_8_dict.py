
#a
bierce = {
    "dzień": "Okres dwudziestu czterech godzin, zwykle zmitrężony.",
    "nieszczęście": "Rodzaj szczęścia, które nie wybrzydza.",
    "optymista": "Zwolennik teorii, że czarne jest białe.",
    }
print(bierce)
print(type(bierce))
print( )

#b

acme_customer = {'first': 'Waldemar', 'middle': 'Edward', 'last': 'Chrzanowski'}
print(acme_customer)
print(type(acme_customer))



acme_customer = dict(first="Waldemar", middle="Edward", last="Chrzanowski" )
print(acme_customer)
print(type(acme_customer))
print( )

#c
lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
print(type(lol))
lol_dict = dict(lol)
print(lol_dict)
print(type(lol_dict))
print( )

lol_dict = dict([ ['a', 'b'], ['c', 'd'], ['e', 'f'] ])
print(lol_dict)
print(type(lol_dict))
print( )

lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
print(type(lot))
print(dict(lot))
print(type(lot))
print( )

dict_lot = dict(lot) #trzeba nową zmienną
print(dict(lot))
print(type(dict_lot))

#d

tos = ( 'ab', 'cd', 'ef' )
dict(tos)
print(tos)
print(type(tos))
print(dict(tos))
print(type(dict(tos))) # ale sam tos jest dalej krotką
print( )
print(type(tos))
print( )

#e

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
    }
print(pythons)
print(type(pythons))
pythons['Gilliam'] = 'Gerry'
print(pythons)
pythons['Gilliam'] = 'Terry'
print(pythons)
print( )

#f

some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry':'Jones',}
print(some_pythons['John'])

print('Groucho' in some_pythons)

print(some_pythons.get('John'))

print(some_pythons.get('Groucho', 'To nie od Monthy'))

#g

signals = {'zielone': 'jedź', 'żółte': 'hamuj', 'czerwone': 'uśmiech do kamery'}

print(signals.keys())
print(type(signals.keys))
print( )

print(list(signals.keys()))
print(type(list(signals.keys())))
print( )

print(signals.values())
print(list(signals.values()))
print( )

print(list(signals.items()))
print(type(list(signals.items())))
print( )

#h
signals = {'zielone': 'jedź', 'żółte': 'hamuj', 'czerwone': 'uśmiech do kamery'}
print(len(signals.items()))
print(len(signals))
print( )

#i

first = {'a': 'Ala', 'b': 'Basia'}
second = {'b': 'Beata', 'c': 'Cezary'}
third = {'d': 'Darek'}


print({**first, **second, **third})
print( )

#j

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
}
others = {
    'Marx': 'Groucho',
    'Howard': 'Moe'
}

# Update the 'pythons' dictionary with 'others'
pythons.update(others)

print(pythons)
print( )

#Print the updated dictionary
print(pythons.items())  
print( )
print(type(pythons)) 
print( )   

del pythons['Marx']
print(pythons)

del pythons['Howard']
print(pythons)
print( )

#k
print("to tu")
print(len(pythons))
pythons.pop('Palin')
print( )
print(len(pythons))
print( )
pythons.pop('Palin', 'nie ma w domu') # dajemy cokolwiek
print(pythons.pop('Palin', 'nie ma w domu'))
print( )

pythons.clear()
print(pythons)
print(len(pythons))
print( )


#l

pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Jones': 'Terry', 'Palin': 'Michael', 'Idle': 'Eric'}
print(pythons.items())
print('Chapman' in pythons)
print( )

#m

signals = {'zielone': 'jedź','żółte': 'hamuj','czerwone': 'uśmiech do kamery'}
print(signals.items())
print(len(signals))
save_signals = signals
signals['niebieskie'] = 'zmyłka'
print(save_signals.items())
print(len(save_signals))
print( )

#n

signals = {'zielone': 'jedź', 'żółte': 'hamuj', 'czerwone': 'uśmiech do kamery'}
print(signals.items())
original_signals = signals.copy()
signals['niebieskie'] = 'zmyłka'
print(signals.items())
print(len(signals))

print(original_signals.items()) #ma starą wersję, bez niebieskiego
print(len(original_signals))
print()

#o

signals = {'zielone': 'jedź','żółte': 'hamuj','czerwone': ['stój', 'uśmiech']}
signals_copy = signals.copy()
print(signals.items())
print(len(signals))

print(signals_copy.items())
print(len(signals_copy))

print( )
print("czewone na czekaj")
signals['czerwone'][1] = 'czekaj'
print(signals.items())

print(signals_copy.items()) #oba się zmieniły
print( )


print("import copy")
import copy
signals = {'zielone': 'jedź', 'żółte': 'hamuj','czerwone': ['stój', 'uśmiech']}
print(signals.items())
signals_copy = copy.deepcopy(signals)
print(signals_copy.items())
print( )
print("czewone na czekaj")
signals['czerwone'][1] = 'czekaj'
print(signals.items())
print(signals_copy.items()) #została stara wartość

#p

a = {1:1, 2:2, 3:3}
b = {3:3, 1:1, 2:2}
#a == b
print(a == b) #tylko == lub !=

#r

accusation = {'pomieszczenie': 'sala balowa', 'narzędzie': 'gazrurka', 'osoba': 'pułkownik Musztarda'}
for card in accusation: # lub for card in accusation.keys():
    print(card)
print( )


accusation = {'pomieszczenie': 'sala balowa', 'narzędzie': 'gazrurka', 'osoba': 'pułkownik Musztarda'}
for card in accusation.items(): 
    print(card)
    print( )

#s

accusation = {'pomieszczenie': 'sala balowa', 'narzędzie': 'gazrurka', 'osoba': 'pułkownik Musztarda'}

for card, contents in accusation.items():
    print('Zawartość karty', card, ':', contents)

#t

word = 'programowanie'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
print( )


word = 'programowanie'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)
print( )