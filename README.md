# Sudoku

Sovellus on yksinkertainen sudoku-peli. Sovelluksessa käyttäjä pääsee pelaamaan kahdeksaa eri sudokua, jotka ovat tallennettu tiedostolle.
Käyttäjä voi muokata tiedoston sisällä olevia sudokuja, jos haluaa. Huom. sudokujen pitää olla sudokun sääntöjen mukaisia, jotta sovellus voi ilmoittaa ratkaisun olevan oikein.

Tarkemmat tiedot sovelluksen toiminnallisuudesta löytyvät dokumentaatiosta.

## Dokumentaatio

[Vaatimusmäärittely](Dokumentaatio/vaatimusmaarittely.md)  
[Käyttöohje](Dokumentaatio/käyttöohje)

## Ohjelman asentaminen ja ajaminen:
Pelin ajamiseen vaaditaan vain src kansio ja sen sisältämät tiedostot.

Ennen kuin pelin voi käynnistää pitää asentaa riippuvuudet komennolla:

- poetry install

Sitten pelin voi aloittaa src/ kansiossa komennolla:

- poetry run python3 sudoku.py


