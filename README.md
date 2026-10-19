# MLOPSLAB2026

Materialy i rozwiazania uporzadkowane wedlug numeru laboratorium.

```text
lab1/
  labs/       # cwiczenia i projekt z laboratorium 1
  homework/   # zadanie domowe 1
lab2/
  labs/       # notebooki, dane i Docker Compose z laboratorium 2
  homework/   # miejsce na zadanie domowe 2
```

## Praca z projektem

Uruchamiaj polecenia w katalogu odpowiedniego zadania, np.:

```bash
cd lab2/labs
source .venv/bin/activate
docker compose up -d
jupyter notebook
```

Kazdy istniejacy projekt ma osobne srodowisko `.venv` oraz pliki `pyproject.toml` i `uv.lock`.
Nowy terminal otwieraj w nowej lokalizacji; po przeniesieniu uruchom ponownie Jupytera.
Projekt Compose labu 2 zachowuje nazwe `lab2`, aby korzystac z istniejacego wolumenu `lab2_pgdata`.
