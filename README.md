# Vigenere
Vigenère Cipher Cryptanalysis in python – a tool for breaking the cipher using frequency analysis.
## 1. Wymagania wstępne

- Python w wersji 3.x (zalecane 3.8 lub nowszy).
- Komputer szybszy niż toster

## 2. Pobranie i zapisanie kodu

- Skopiuj kod źródłowy i zapisz go w pliku o nazwie vigenere.py.

## 3. Przygotowanie pliku wejściowego

- Upewnij się, że w katalogu ze skryptem znajduje się plik szyfrogram.txt , zawierający zaszyfrowany tekst do analizy.

## 4. Uruchomienie programu

### a) Otwórz terminal

- **Windows**: `cmd` lub PowerShell
- **Linux/macOS**: Terminal

### b) Przejdź do katalogu, w którym zapisałeś plik `vigenere.py`:

```
cd /sciezka/do/vigenere.py
```

 c) Uruchom program:

```
python vigenere.py
```

Jeśli masz wiele wersji Pythona zainstalowanych, użyj:

```
python3 vigenere.py
```

## 5. Opis działania programu

- **Wczytuje** szyfrogram z pliku `szyfrogram.txt`.
- **Analizuje** częstość liter oraz stosuje metodę Friedmana do oszacowania długości klucza.
- **Wyszukuje** powtarzające się sekwencje i oblicza największy wspólny dzielnik odległości między nimi.
- **Dzieli** tekst na kolumny i wykonuje analizę przesunięcia liter.
- **Odszyfrowuje** wiadomość na podstawie uzyskanych danych i wyświetla rezultat.

## 6. Możliwe błędy i ich rozwiązania

- \*\*Błąd FileNotFoundError \*\*\`\` – upewnij się, że plik `szyfrogram.txt` jest w tym samym katalogu co skrypt.
- **Błąd uprawnień** – jeśli terminal zgłasza problem z dostępem do pliku, uruchom go jako administrator lub użyj `sudo` w Linux/macOS:
  ```
  sudo python3 vigenere.py
  ```
## 7. Autor i licencja

Program wykonał Jakub Żegliński / SirSail , program jest otwarty na darmowy użytek, modyfikacje oraz dystrybucję.



