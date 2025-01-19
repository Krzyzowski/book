
# a
furry = True
large = False

if furry:
    if large:
        print("Example a. To jest yeti.")
    else:
        print("Example a. To jest kot.")
else:
        if large:
            print("Example a. To jest wieloryb.")
        else:
            print("Example a. To jest człowiek.")
print(                  )


# b
disaster = False

if disaster:
    print("Example b. Niedobrze!")
else:
    print("Example b. Dobrze!")
print( )

# c
color = "lawendowy"

if color == "czerwony":
    print("Example c. To jest pomidor.")
elif color == "zielony":
    print("Example c. To jest ogórek")
elif color == "ultrafioletowy":
    print("Example c. Nie wiem, co to jest. Tylko pszczoła może to zobaczyć.")
else:
    print("Example c. Nie znam koloru", color)
print(  )


# d
letter = 'o'
if letter == 'a' or letter == 'e' or letter == 'i' \
or letter == 'o' or letter == 'u' or letter == 'y':
    print('Example d. Litera', letter, 'jest samogłoską')
else:
    print('Example d. Litera', letter, 'nie jest samogłoską ')
print(                )

# e
vowels = 'aeiouy'
letter = 'e'
#letter in vowels #why False: mistake in book
#False
if letter in vowels:
    print(letter, 'jest samogłoską. Example e.')
print(                )



# f
letter = 'o'
vowel_set = {'a', 'e', 'i', 'o', 'u', 'y'}
is_vowel = letter in vowel_set 
print(is_vowel)

letter = "o"
vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
is_vowel = letter in vowel_list
print(is_vowel)

letter = "o"
vowel_tuple = ('a', 'e', 'i', 'o', 'u', 'y')
is_vowel = letter in vowel_tuple
print(is_vowel)

letter = "o"
vowel_dict = {'a': 'Ania', 'e': 'Ewa', 'i': 'Iwona', 'o': 'Ola', 'u': 'Ula', 'y': 'Yves'}
is_vowel = letter in vowel_dict
print(is_vowel)

letter = "o"
vowel_string = "aeiouy"
is_vowel = letter in vowel_string
print(is_vowel)
print(                )

# g


tweet_limit = 280
tweet_string = "coś" * 50
diff = tweet_limit - len(tweet_string)
print('Example g tweet_limit_remaining = ',diff)
if diff >= 0:
    print("Example g. Dobry tweet")
else:
    print("Example g. Tweet za długi o", abs(diff), "znaków")
print(                )

# h 

tweet_limit = 280
tweet_string = "coś" * 5000
diff = tweet_limit - len(tweet_string)
print(diff)
if (diff := tweet_limit - len(tweet_string)) >= 0: 
    print("Example h. Dobry tweet")
    print(diff)
else:
    print(" Example h. Tweet za długi o", abs(diff), "znaków")
    print('Example g tweet_limit = ' , diff)
print(     )           
print(diff)
print(                )

#Do zrobienia str 80
# 4.1. Przypisz zmiennej secret liczbę z przedziału od 1 do 10. Następnie wybierz inną liczbę z tego
# samego przedziału i przypisz ją zmiennej guess. Napisz kod porównujący obie zmienne za pomocą instrukcji
#  if, elif oraz else i wyświetlający napis „za mało”, jeżeli zmienna guess jest mniejsza
# od secret, „za dużo”, jeżeli zmienna guess jest większa od secret, lub „równo”, jeżeli zmienna
# guess jest równa secret

# do update

import random
secret = random.randint(1, 10)

guess = int(input("Please enter an integer between 1 and 10: "))
delta = secret - guess


if delta >= 0:
    print(" Example 4.1 . za mało.")
elif delta <= 0:
    print(" Example 4.1 . za dużo")

else:
    print(" Example 4.1 . równo")
print(                )






# 4.2. Przypisz zmiennym mały i zielony wartości True lub False.
#  Napisz kod sprawdzający za pomocą kilku instrukcji if/else, czy coś jest wiśnią, groszkiem, arbuzem czy dynią.


green = True
small = True


if green:
    if large:
        print(" Example 4.2 . To jest arbuz.")
    else:
        print(" Example 4.2 . To jest groszek.")
else:
        if large:
            print(" Example 4.2 . To jest dynia.")
        else:
            print(" Example 4.2 . To jest wiśnia.")
print(                )









