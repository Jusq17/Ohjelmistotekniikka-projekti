# Vaatimusmäärittely

## Sovelluksen tarkoitus:

- Sovellus on sudoku-peli, jolla on graafinen käyttöliittymä. Sovellus tekee 9x9 sudokun, jonka pelaaja ratkaisee käyttöliittymää käyttäen.

## Käyttäjät:

- Sovellus on yksinpelattava peli, joten se tarvitsee vain yksittäisen peruskäyttäjän.

## Käyttöliittymä:

Sovelluksella on kolme näkymää:

- Menu, josta voi aloittaa pelin tai lopettaa sovelluksen
- Leveli menu, josta voi ladata levelin 1-8 tai lopettaa sovelluksen
- Pelinäkymä, jossa varsinainen sudokun pelaaminen tapahtuu
    
![view](https://user-images.githubusercontent.com/86538024/147420301-a6284882-645e-4d4c-b3ef-5840b47df5c1.JPG)

  

## Sovelluksen perustoiminnallisuus:
    
 - Pelin alkaessa valittu leveli ladataan tekstitiedostosta.
 - Pelaaja voi halutessaan käydä muuttamassa sudoku-matriiseja, mutta jos matriisi rikkoo sudokun sääntöjä, ei oikeaa vastausta ole olemassa.
    
 - Itse pelin pelaaminen käy kuten normaalissa sudokussa yleensä. Pelaaja täydentää tyhjät paikat valitsemallaan numerolla (1-9).
 - Muutettavissa olevat ruudut ovat valkoisia ja tyhjiä. Niiden arvoa voi kasvattaa tai vähentää yhdellä hiiripainikkeilla. Alkuarvo on nolla
 - Kun pelaaja on valmis, hän voi tarkastaa ratkaisun nappia painamalla ja sovellus ilmoittaa onko sudoku ratkaistu oikein vai ei.
    
## Jatkokehitysideoita:

### Perusversion jälkeen sovellusta voi parantaa lisäämällä esimerkiksi:

- Pelin tallennus ja myöhemmin jatkaminen
- Kirjautumisjärjestelmä
- Randomin sudoku-matriisin voisi generoida algoritmilla. Ns. "random pelimuoto"
- Sovelluksen yleistä optimointia
    
