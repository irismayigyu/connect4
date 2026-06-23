## Testausdokumentti

Testit voi suorittaa juurikansiossa komennolla
```bash
poetry run invoke test
```
Testikattavuusraportin saa komennolla (ajaa myös testit)
```bash
poetry run invoke coverage-report
```

Sovelluslogiikan ja tekoälyn funktiot on testattu yksikkötesteillä sekä molempien luokkien yhteistoimintaa on myös testattu. Heuristiikkafunktiota on testattu muutamassa eri tilanteessa, tarkistaakseen että se pisteyttää pelitilanteet oikein.

