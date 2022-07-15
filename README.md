# dostanesie.pl - API przeliczników

Ta krótka dokumentacja przybliży Ci metodę implementacji nowych przeliczników punktów.

**Dodawanie przeliczników jest dostępne wyłącznie dla współpracujących z nami uczelni,
jeśli jesteś zainteresowany dodaniem swojej uczelni wejdź na stronę [kontakt](https://dostanesie.pl/kontakt)**

## Implementacja

Implementacja przeliczników w dostanesie.pl jest obiektowa i w całości napisana w języku Python w wersji 3.10.

## Jak dodawać wzór?

Aby dodać nowy wzór, musisz upewnić się, że zostanie zachowana poprawna struktura klas i plików.

1. _utajnione_ - nie istotne dla partnerów
2. _utajnione_ - nie istotne dla partnerów
3. _utajnione_ - nie istotne dla partnerów

   Klasa MUSI
   mieć uzupełnione pola:
    - `year` - orientacyjny rok, dla którego jest wzór. Nie ma to wpływu na przypisanie wzoru do rekrutacji, jest to
      tylko wskazówka, która pomoże podczas dobierania wzorów do rekrutacji
    - `uuid` - UUID4, musi być unikalny i ustawiony na sztywno. Nie wolno go już nigdy zmieniać.
4. Każda konkretna klasa powinna implementować metodę statyczną `caculate`.
5. Dla każdego kierunku należy zaimplementować osobną klasę (nawet jeśli ma tylko dziedziczyć po innej), a nazwa klasy
   MUSI zgadzać się z nazwą kierunku (bez polskich znaków, CamelCase, wraz ze spójnikami).


## Dodatkowe ułatwienia "syntactic sugar"

Klasa dla `MaturaResults` zawiera szereg skrótów, z których warto korzystać.

- metody z prefiksem `any_` zwracają najlepszy przedmiot z danej grupy
- metody z prefiksem `all_` zwracają listę przedmiotów z danej grupy
- metody z sufiksem `_pair` zwracają tuplę przedmiotów z poziomu podstawowego i rozszerzonego (dla fizyki rozszerzonej
  maks ze starej formuły i nowej formuły)
- _utajnione_ - nie istotne dla partnerów
