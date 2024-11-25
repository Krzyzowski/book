
# 7.1. Utwórz listę o nazwie years_list zawierającą listę lat od roku, w którym się urodziłeś, do Twoich
#piątych urodzin. Jeżeli na przykład urodziłeś się w 1980 r., niech lista ma postać years_list =
#[1980, 1981, 1982, 1983, 1984, 1985]. Nie wiem, co mam Ci powiedzieć, jeżeli nie skończyłeś
#jeszcze 5 lat i czytasz tę książkę.

years_list = [1983, 1984, 1985, 1986, 1987, 1988]
print(type(years_list))
print( )

# 7.2. W którym roku zawartym w liście years_list były Twoje trzecie urodziny? Pamiętaj, że
# w pierwszym roku miałeś 0 lat.

print(years_list[3])
print( )

# 7.3. W którym roku zawartym w liście years_list miałeś najwięcej lat?

years_list = [1983, 1984, 1985, 1986, 1987, 1988]
print(years_list[len(years_list) - 1])
print( )
print(len(years_list))
print(years_list[5])


# 7.4. Utwórz listę o nazwie things zawierającą trzy ciągi znaków: "seradela", "mortadela",
# "cytadela".

things = ["seradela", "mortadela", "cytadela"]
print(things)
print(type(things))
print( )

# 7.5. Pierwszą literę ciągu w liście things, opisującego jedzenie, zamień na wielką i wyświetl całą listę.
# Czy zmieniła się jej zawartość?


things = ["seradela", "mortadela", "cytadela"]
Things = things.copy()
print(Things)

for i in range(2):
    Things[i] = Things[i].capitalize()

print(Things)
print(things == Things)


things = ["seradela", "mortadela", "cytadela"]
print( )

#Wszystkie litery ciągu w liście things, opisującego jedzenie, zamień na wielkie i wyświetl
#całą listę.


things = ["seradela", "mortadela", "cytadela"]
Things = []


Things.append(things[0].upper())
Things.append(things[1].upper())
Things.append(things[2])

print(Things)  
print(things)  
print(things == Things)


# 7.7. Usuń z listy things element opisujący budowlę i wyświetl całą listę.

things = ["seradela", "mortadela", "cytadela"]
things.remove("cytadela")

print(things)
print( )


#7.8. Utwórz listę o nazwie surprise zawierającą ciągi znaków: "Groucho", "Chico" i "Harpo".

surprise = ["Groucho", "Chico", "Harpo"] 
print(surprise)
print(type(surprise))
print( )

#7.9. Zamień wszystkie litery ostatniego ciągu w liście surprise na małe, odwróć ich kolejność
#i zamień pierwszą literę na wielką.


surprise = ["Groucho", "Chico", "Harpo"] 
surprise[2] = surprise[2].lower()
print(surprise)
surprise[2] = surprise[2][::-1]
print(surprise)
surprise[2] = surprise[2].capitalize()
print(surprise)
print( )

#7.10 Za pomocą wyrażenia listowego utwórz listę o nazwie even zawierającą liczby parzyste z zakresu
# od 0 do 9.

even = [10]
for x in range(10):
    if x % 2 == 0:
        even.append(x)
print(even)

# 7.11. Utwórz rymowankę do skakanki. Wyświetl serię dwuwierszowych rymowanek. Poniżej przedstawiony
# jest początek programu:

start1 = ["raz", "dwa", "trzy"]

rymy = [
("sklep", "schylił łeb"),
("ziut", "przeciął drut"),
("bom", "chwycił łom"),
("gaz", "szybko wlazł"),
("siup", "wyniósł łup"),
("siad", "głupio wpadł"),
("cóż", "siedzi już"),
]

start2 = "Mały Jasio"

start1_caps = " ".join([word.capitalize() + "!" for word in start1])
#print(start1_caps)
for pierwsza, druga in rymy:
    print(f"{start1_caps} {pierwsza.capitalize()}!")
    print(f"{start2} {druga}.")