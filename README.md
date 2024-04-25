# list-_left_rotation
#
def left_rotate(l, num):
Ta linia definiuje funkcję left_rotate przyjmującą dwie argumenty: l (lista do przesunięcia) i num (liczba określająca, o ile miejsc należy przesunąć listę w lewo).

return l[num:] + l[:num]
Ta linia wykonuje właściwe przesunięcie w lewo. Działa to przez połączenie dwóch fragmentów listy: fragmentu od indeksu num do końca (l[num:]) oraz fragmentu od początku do indeksu num (l[:num]). To właśnie te dwa fragmenty zostają ze sobą połączone, co daje przesuniętą w lewo listę.

list_ = list("1234567")
Tutaj tworzymy listę list_, która jest zbudowana z kolejnych cyfr od 1 do 7.

print(left_rotate(list_, 4))
Wywołujemy funkcję left_rotate na liście list_ z argumentem num ustawionym na 4. Wynik jest drukowany na ekranie.

print(left_rotate(list_, 5) is not list_)
To sprawdza, czy wynik przesunięcia w lewo nie jest tą samą listą co list_. Jeśli funkcja działa poprawnie, powinno to zwrócić True.