
## Ohjelman yleisrakenne

- UI-kansiossa on pelinäkymä (gameview.py), jossa piirretään pelinäkymä pygamessa. Käyttää Matrix (peliruudukko) ja Ai luokkien olioita

- Ai.py on tekoälystä vastaava tiedosto.

- Main.py suorittaa pelilooppia.

- Services-kansion matrix.py sisältää toimintalogiikan.

### Aika- ja tilavaativuudet

- Aikavaativuus: O(n^m), jossa n: mahdollisten siirtojen määrä ja m: kuinka monta siirtoa eteenpäin lasketaan (syvyys). 

- Tilavaativuus: O(nm), jossa n: mahdollisten siirtojen määrä ja m: kuinka monta siirtoa eteenpäin lasketaan (syvyys). 

Pelissä käytetään maksimisyvyyttä 6. Korkeammilla syvyyksillä peli alkaa hidastua huomattavasti.

### Jatkokehitysideoita

- UI:n parantelu esim ohjeet screenille eikä vaan READ.MEhen. 

- Tekoälyn tehokkuuden parantelu niin, että syvyyttä voisi lisätä.

### Laajojen kielimallien käyttö:

Käytetty debuggaukseen, Chat-GPT 5.5.

### Lähteet, joita olet käyttänyt: 

- Video: Sebastian Lague, 2018: Algorithms Explained – minimax and alpha-beta pruning 
https://www.youtube.com/watch?v=l-hh51ncgDI 

- Tiralabran kurssimateriaali