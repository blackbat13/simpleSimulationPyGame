# Simple Simulation Example

## Struktura projektu

- **requirements.txt**: plik z zależnościami
- **.gitignore**: wykluczenia z repozytorium
- **main.py**: główny plik programu
- **simulation**: podstawowy pakiet naszego projektu
- - **containers**: kontenery symulacji
- - **elements**: podstawowe elementy symulacji
- - **simulation**: główne klasy symulacji
- - **test**: testy jednostkowe

## Tworzenie środowiska wirtualnego i instalacja zależności

### Windows

```
python -m venv sim-env
sim-env\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Linux

```
python3 -m venv sim-env
source sim-env/bin/activate
pip install -r requirements.txt
```

### Wyjście ze środowiska wirtualnego

```
deactivate
```
