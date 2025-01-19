#a 

PT = 'Czytałeś "Pana Tadeusza"?'
print('Example a:', PT)
print(               )


PL = "Znasz prawo Laplace'a?"
print('Example a:', PL)
print(               )


diameter = 'Średnica rury: 1/2" lub 3/4"'
print('Example a:', diameter)
print(               )

# b

limeryk = '''Był Chińczyk w pustyni Gobi,
który straszne kawały robił.
W końcu, znienawidzony,
przeniósł się w inne strony,
ale nic sobie z tego nie robił.'''

print('Example b:', limeryk)
print(                  )

# c

limeryk2 = '''Ambitnemu hodowcy w Łobzowie\nrosła bujnie pietruszka na głowie.\nEkolodzy pospołu\nzrywali ją do rosołu,\nbo pietruszka to samo zdrowie.\n'''

print('Example c:', limeryk2)
print(                  )

# d
print('Example d:', 'Zrób', "tutaj", '''trochę''', """miejsca""")
print(                  )

# e
palindrom = 'Gór\nech\nchce\nróg'
print('Example e:\n' + palindrom)
print(                  )

palindrom = ' Gór\n ech\n chce\n róg' # "n" oddzielone spacją
print('additional space:\n' + palindrom)
print(                       )

# f
oświadczenie = "\"Niczego nie zrobiłem!\" - powiedział. \"Oprócz tego.\""
print('Example f:' , oświadczenie)

oświadczenie = '"Niczego nie zrobiłem!" - powiedział. "Oprócz tego."'
print('Example f:' , oświadczenie)
print(                  )


# g

tekst = 'To jest lewy ukośnik: \\.'
print('Example g:' , tekst)
print(                  )

# h

info = r'Aby zwykły ciąg znaków wyświetlić w dwóch wierszach, wpisz\n.'
print('Example h:' , info)
print(                  )
info = 'Aby zwykły ciąg znaków wyświetlić w dwóch wierszach, wpisz\\n nie zeszło niżej.'
print('Example h:' , info)
print(                  )
info = 'Aby zwykły ciąg znaków wyświetlić w dwóch wierszach, wpisz\n \\n :) a teraz zeszło niżej.'
print('Example h:' , info)
print(                  )

# i

sentencja = r'''Mowa jest srebrem,
a milczenie złotem.'''
print('Example i:' , sentencja)

sentencja = 'Mowa jest srebrem,\na milczenie złotem.'
print('Example i:' , sentencja)
print(                  )

# j
suma = 'Nie ma tego złego, ' + 'co by na dobre nie wyszło.'
print('Example j:' , suma)

suma =  "Wszędzie dobrze, " "ale w domu najlepiej."
print('Example j:' , suma)
print(                  )

samogłoski = ('a'
"e" '''i'''
'o' """u"""
"y")
print('Example j:' , samogłoski)
print(                  )

a = 'Raz,'
b = a
c = 'Dwa, trzy!'

print('Example j:' ,a, b, c)


początek = 'Raz ' * 4 + '\n'
środek = 'Dwa ' * 3 + '\n'
koniec = 'Trzy.'
print('Example j:' ,początek + środek + koniec)
print(                  )

# k
litery = 'abcdefghijklmnopqrstuvwxyz'
print('Example k:' , litery[2])
print(                  )

# l

imię = 'Marek'
imię = 'D' + imię[1:] 
print(imię)

imię = 'Marek'

try:
  imię[0] = 'D'
except TypeError:
  print("Nie można modyfikować wartości znaków w łańcuchu znaków.")

print('Example l:' , imię)
print(                  )

imię = 'Marek'
imię.replace('M', 'D', 1) # poprawione wzgledem ksiazki

print('Example l:', imię)

imię = 'D' + imię[1:]
print('Example l:', imię)
print(                  )

# m
litery = 'abcdefghijklmnopqrstuvwxyz'
print('Example m:', litery[:])

print('Example m:', litery[20:])

print('Example m:', litery[20:23:2])

print('Example m:', litery[-4::2])
print(                  )