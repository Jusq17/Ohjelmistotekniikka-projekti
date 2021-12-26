# Sudoku

Sovellus on yksinkertainen sudoku-peli. Sovelluksessa käyttäjä pääsee pelaamaan kahdeksaa eri sudokua, jotka ovat tallennettu tiedostolle.
Käyttäjä voi muokata tiedoston sisällä olevia sudokuja, jos haluaa. Huom. sudokujen pitää olla sudokun sääntöjen mukaisia, jotta sovellus voi ilmoittaa ratkaisun olevan oikein.

Tarkemmat tiedot sovelluksen toiminnallisuudesta löytyvät dokumentaatiosta.

## Dokumentaatio

[Vaatimusmäärittely](Dokumentaatio/vaatimusmaarittely.md)  
[Käyttöohje](Dokumentaatio/käyttöohje)

## Ohjelman asentaminen ja ajaminen:
Pelin ajamiseen vaaditaan src kansio ja poetry.lock ja pyproject.toml tiedostot.

### Asenna poetry komentorivillä komennolla

- pip install poetry

Asenna riippuvuudet komennolla:

- poetry install

Sitten pelin voi aloittaa src/ kansiossa komennolla:

- poetry run python3 sudoku.py


