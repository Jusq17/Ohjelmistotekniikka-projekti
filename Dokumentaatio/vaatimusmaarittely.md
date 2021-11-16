Vaatimusmäärittely

Sovelluksen tarkoitus:

    Sovellus on sudoku-peli, jolla on graafinen käyttöliittymä. Sovellus tekee 9x9 sudokun, jonka pelaaja ratkaisee käyttöliittymää käyttäen.

Käyttäjät:

    Sovellus on yksinpelattava peli, joten se tarvitsee vain yksittäisen peruskäyttäjän.

Käyttöliittymä:

Sovelluksella on kaksi näkymää:

    - Menu, josta voi aloittaa pelin tai lopettaa sovelluksen
    - Pelinäkymä, jossa varsinainen sudokun pelaaminen tapahtuu

Sovelluksen perustoiminnallisuus:

    - Käyttäjä voi luoda itselleen nimen pelin alkaessa(default = "guest")
    - Käyttäjän sudokun ratkaisemiseen kestävä aika tallenetaan nimelle
    
    - Pelin alkaessa sovellus luo sudoku-matriisin ja tarkastaa algoritmilla, onko matriisi ratkaistavissa vai ei.
    - Sovellus löytää sopivan matriisin tällä menetelmällä
    
    - Itse pelin pelaaminen käy kuten normaalissa sudokussa yleensä. Pelaaja täydentää tyhjät paikat valitsemallaan numerolla (1-9).
    - Kun pelaaja on valmis, hän voi tarkastaa ratkaisun nappia painamalla ja sovellus ilmoittaa onko sudoku valmis.
    
