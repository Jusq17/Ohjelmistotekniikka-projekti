# Käyttöohje:

## Konfigurointi:

- Pelattavat sudoku-matriisit ovat tallenettuna sudoku_grids.txt tiedostoon, josta sovellus lukee ja lataa ne.
- Pelaaja voi siis halutessaan käydä muokkaamassa sudokuja tai laittaa aivan uuden sudokun tiedostoon. Sudoku pitää kuitenkin olla kunnollinen. Sovellus ei korjaa siitä virheitä

## Ohjelman ajaminen:

Ennen kuin pelin voi käynnistää pitää asentaa riippuvuudet komennolla:

- poetry install

Sitten pelin voi aloittaa src/ kansiossa komennolla:

- poetry run python3 sudoku.py

## Pelin toiminnot:

### Kun peli alkaa, ensimmäiseksi tulee näkyviin start menu:

![startmenu](https://user-images.githubusercontent.com/86538024/147418557-257f1a4f-e76c-4ee8-ad6b-4cadc8496802.JPG)

Tästä menusta voi siirtyä leveli menuun tai lopettaa pelin quit-napista.

### Seuraava näkymä, johon pelaaja pääsee on leveli-menu:

![levelmenu](https://user-images.githubusercontent.com/86538024/147418622-bf142e57-003c-405a-8b20-3db5db8f6dba.JPG)

Tässä menussa pelaaja voi valita levelin väliltä 1-8. Tässä näkymässä on myös quit-nappi, joka toimii samalla tavalla kuin aikaisemmin

### Kun pelaaja valitsee tason, kyseinen taso ladataan tiedostolta ja näkymä vaihtuu varsinaiseen peli osioon:

![gameplay](https://user-images.githubusercontent.com/86538024/147418756-03051d9c-bd05-41ba-9cb3-92ef96a8542b.JPG)

Varsinainen pelaaminen tapahtuu käyttämällä hiiren painikkeita. Vasen nappi kasvattaa valkoisen tyhjän ruudun arvoa yhdellä ja oikea nappi vähentää arvoa yhdellä.
Vihreiden valmiiksi annettujen ruutujen arvoa pelaaja ei pysty muuttamaan, kun peli on käynnissä.

Kun pelaaja on tehnyt sudokun mielestään loppuun, hän voi tarkistaa onko sudoku ratkaistu oikein "check" nappia painamalla. Sovellus ilmoittaa tuloksen piirtämällä tekstiä sudoku-matriisin alle. Sudokun oikean ratkaisun näkeminen tapahtuu painamalla "show answer nappia".

Peli-näkymästä voi siirtyä takaisin leveli-valikkoon painamalla "back" nappia

### Näkymän siirtymiä kuvaa seuraava kuva:

![view](https://user-images.githubusercontent.com/86538024/147418982-d8f1786d-b86c-40fd-b8b5-92a0a3c25650.JPG)

