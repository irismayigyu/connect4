## Testausdokumentti

Testit voi suorittaa juurikansiossa komennolla
```bash
poetry run invoke test
```
Testikattavuusraportin saa komennolla (ajaa myös testit)
```bash
poetry run invoke coverage-report
```

Heuristiikkafunktiota on testattu muutamassa eri tilanteessa, jotta se pisteyttää pelitilanteet oikein.

Sovelluslogiikan ja tekoälyn funktiot on testattu yksikkötesteillä sekä testattu molempien luokkien eri funktioita samassa testissa. Minimaxia tulee testata kattavemmin erilaisissa tilanteissa. 

