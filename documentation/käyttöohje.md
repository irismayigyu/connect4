## Käyttöohjeet

1. Kloonaa repositorio

2. Asenna riippuvuudet komennolla

```bash
poetry install
```

3. Mene src kansioon 

4. Käynnistä ohjelma komennolla
```bash
poetry run python main.py
```

tai juurikansiossa komennolla 
```bash
poetry run invoke start
```

Coverage report ja testit:
```bash
poetry run invoke coverage-report
```