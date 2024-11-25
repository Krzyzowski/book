
#a
count = 1
while count <= 5:
    print(count)
    count += 1

#b

while True:
    stuff = input("Wpisz tekst [lub q, aby zakończyć]: ")
    if stuff == "q":
        break
    print(stuff.capitalize())

#c

while True:
    value = input("Podaj liczbę [lub q, aby zakończyć]: ")
    if value == 'q': # Wyjście
        break
    number = int(value)
    if number % 2 != 0: # ianczej niż w książce. Liczba parzysta
        continue
    print(number, "do kwadratu to", number*number)


#d
numbers = [1, 3, 5, 6]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Znaleziona liczba parzysta', number)
        break
    position += 1
else: # Instrukcja break nie została użyta
    print('Nie ma liczb parzystych')

#e

word = 'słowo'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 1
print(                    )

word = 'słowo'
offset = 0
while offset < len(word):
    print(word[offset])
    offset += 2  # lub co drugie
print(                    )
#f 

word = 'słowo'
for letter in word: #zwykła pętla
     print(letter)
print(                    )

# g
word = 'słowo'
for letter in word:
  if letter == 'x':
    print("Jest litera 'x'!")
    break
  print(letter)
else:
  print("Nie ma litery 'x'.")

# h

for x in range(0,3):
    print(x)

z = list( range(0, 3) )
print(z)

#i

for x in range(2, -2, -1):
  print(x)

y = list( range(2, -2, -1) )
print(y)
print(                      )
#Examples

#6.1 

print(" to do 6.1" )

for x in [3,2,1,0]:
  print(x)
print(               )

#6.2 
print(" to do 6.2" )

guess_me=7

number=1

 

while True:

    if number < guess_me:

        print ("number:" + str(number))

        print ("za malo")

        number += 1

    elif number == guess_me:

        print ("number:" + str(number))

        print ("jest ok")

        number += 1

        print ("break number:" + str(number))

        #break

    else:

        print ("number:" + str(number))

        print ("ups")

        break
    
print(                   )
#6.3

print(6.3)
guess_me = 5

for number in range(10):
     if number < guess_me:

        print ("number:" + str(number))

        print ("za malo")

        number += 1

     elif number == guess_me:

        print ("number:" + str(number))

        print ("jest ok")

        number += 1

        print ("break number:" + str(number))

        #break

     else:

        print ("number:" + str(number))

        print ("ups")

        break
