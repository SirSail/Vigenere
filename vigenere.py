import re
from math import gcd
from collections import defaultdict, Counter

# Odczyt szyfrogramu z pliku
def wczytaj_szyfrogram(nazwa_pliku):
    with open(nazwa_pliku, 'r', encoding='utf-8') as plik:
        szyfrogram = re.sub(r'[^a-z]', '', plik.read().lower())  # Usuwamy znaki inne niż litery a-z
    return szyfrogram
# Oblicza współczynnik koincydencji do metody Friedmana
def oblicz_ic(szyfrogram):
    
    N = len(szyfrogram)
    licznik = Counter(szyfrogram)
    
    suma_fi = sum(f * (f - 1) for f in licznik.values())
    IC = suma_fi / (N * (N - 1)) if N > 1 else 0
    return IC
# Szacuje długość klucza 
def metoda_friedmana(szyfrogram):
    
    N = len(szyfrogram)
    IC = oblicz_ic(szyfrogram)
    
    # Współczynniki dla języka polskiego
    IC_pol = 0.065
    IC_losowy = 0.038
    
    # Oszacowanie długości klucza
    if IC - IC_losowy != 0:
        szacowana_dl_klucza = (0.027 * N) / ((IC_pol - IC) + (N * (IC - IC_losowy)))
    else:
        szacowana_dl_klucza = 1  # Zabezpieczenie przed błędem dzielenia przez zero
    
    return round(szacowana_dl_klucza)
# Badanie powtarzających się sekwencji o różnych długościach
def badanie_powtorzen(szyfrogram):
    powtorzenia = defaultdict(list)
    
    for dlugosc in range(3, 15):  # Szukamy powtórzeń o różnych długościach, aż do połowy szyfrogramu
        for i in range(len(szyfrogram) - dlugosc):
            sek = szyfrogram[i:i + dlugosc]
            indeksy = [m.start() for m in re.finditer('(?=' + sek + ')', szyfrogram)]
            if len(indeksy) > 1:  # Sekwencja powtarza się więcej niż raz
                powtorzenia[sek] = indeksy
    
    # Posortuj powtórzenia wg liczby wystąpień
    posortowane_powtorzenia = sorted(powtorzenia.items(), key=lambda x: len(x[1]), reverse=True)
    return posortowane_powtorzenia

# Funkcja do obliczania odległości między kolejnymi wystąpieniami sekwencji
def oblicz_odleglosci(powtorzenia):
    odleglosci = []
    for sek, indeksy in powtorzenia:
        odleglosci_sekwencji = [indeksy[i] - indeksy[i - 1] for i in range(1, len(indeksy))]
        odleglosci.append((sek, odleglosci_sekwencji))  # Zapisać sekwecję i jej odległości
    return odleglosci

# Funkcja do szukania największego wspólnego dzielnika dla listy odległości
def znajdz_nwd_dla_odleglosci(odleglosci):
    if len(odleglosci) == 0:
        return None
    
    nwd = odleglosci[0]
    for odleglosc in odleglosci[1:]:
        nwd = gcd(nwd, odleglosc)
    return nwd

# Podział szyfrogramu na 5 kolumn (z racji długości klucza)
def podziel_na_kolumny(szyfrogram, klucz_dlugosc=5):
    kolumny = ['' for _ in range(klucz_dlugosc)]
    for i, litera in enumerate(szyfrogram):
        kolumny[i % klucz_dlugosc] += litera
    return kolumny
def wypisz_tekst_w_kolumnach(kolumny):
    print("\nTekst podzielony na 5 kolumny:")
    for i, kolumna in enumerate(kolumny):
        print(f"Kolumna {i+1}: {kolumna}")

# Analiza częstotliwości liter w każdej kolumnie
def analiza_czestotliwosci(kolumny):
    # Dla każdej kolumny przeprowadzamy analizę częstotliwości
    for i, kolumna in enumerate(kolumny):
        print(f"\nAnaliza częstotliwości w kolumnie {i+1}:")
        
        # Zliczamy częstotliwości liter w kolumnie
        licznik = Counter(kolumna)
        
        # Przechodzimy przez wszystkie litery alfabetu
        for litera in 'abcdefghijklmnopqrstuvwxyz':
            ilosc = licznik.get(litera, 0)  # Jeśli litera nie występuje, liczba wynosi 0
            
            # Dla wizualizacji: dodajemy gwiazdki do częstotliwości
            gwiazdki = '*' * ilosc
            
            # Wypisujemy literę, liczbę jej wystąpień i gwiazdki
            print(f"{litera}: {ilosc} {gwiazdki}")
def wypisz_analizy():
    print("Analiza częstotliwości i przesunięcia w lewo:")
    
    # Pierwsza analiza
    print("\nAnaliza 1 - Przesunięcie w lewo: 2 (x → v, y → w, z → x)")
    print("Przesunięcie wynika z analizy fragmentu szyfrogramu, gdzie fragment 'x: 0, y: 4 ****, z: 0' odpowiada fragmentowi 'v: 0, w: 46 ****, x: 0'.")
    print("e litery w szyfrogramie są przesunięte o 2 w lewo.")

    # Druga analiza
    print("\nAnaliza 2 - Przesunięcie w lewo: 25 (a → z, b → a, c → b, ...)")
    print("Przesunięcie jest o jeden w dół (tzn. zamiast a mamy z, zamiast x mamy w itp.).")
    print(" litera w szyfrogramie została przesunięta o jedno miejsce w lewo w porównaniu do oryginalnego alfabetu.")

    # Trzecia analiza
    print("\nAnaliza 3 - Przesunięcie: 0 (Brak przesunięcia)")
    print("Nie ma przesunięcia w tej analizie, ponieważ częstotliwości odpowiadają literom w sposób bez zmian.")

    # Czwarta analiza
    print("\nAnaliza 4 - Przesunięcie w lewo: 10 (o → e, p → f, q → g, r → h, s → i)")
    print("Przesunięcie dotyczy fragmentu 'o: 16 **************, p: 0, q: 0, r: 0, s: 10 **********'.")
    print(" litery są przesunięte o 10 w lewo w alfabecie, ponieważ porównując fragmenty, widać, że o odpowiada e, p odpowiada f itd.")

    # Piąta analiza
    print("\nAnaliza 5 - Przesunięcie w lewo: 14 (j → v, k → w, l → x, m → y)")
    print("Przesunięcie dotyczy fragmentu 'j: 0, k: 6 ******, l: 0, m: 3 ***'.")
    print(" litery są przesunięte o 14 w lewo w alfabecie, ponieważ porównując fragmenty, widać, że j odpowiada v, k odpowiada w itd.")

# Funkcja przesuwająca tekst w prawo lub w lewo
def przesun_tekst(tekst, przesuniecie, kierunek='lewo'):
    wynik = []
    for litera in tekst:
        if litera.isalpha():  # Przesuwamy tylko litery
            indeks = ord(litera) - ord('a')  # Indeks w alfabecie (0-25)
            if kierunek == 'lewo':
                nowy_indeks = (indeks - przesuniecie) % 26
            else:  # kierunek 'prawo'
                nowy_indeks = (indeks + przesuniecie) % 26
            nowa_litera = chr(nowy_indeks + ord('a'))  # Nowa litera po przesunięciu
            wynik.append(nowa_litera)
        else:
            wynik.append(litera)  # Niezmienne znaki
    return ''.join(wynik)
def deszyfruj_kolumny(kolumny, przesuniecia):
    # Deszyfrujemy każdą kolumnę przy zastosowaniu odpowiednich przesunięć
    kolumny_deszyfrowane = []
    
    for i, kolumna in enumerate(kolumny):
        # Przesuwamy każdą kolumnę w lewo o odpowiednią ilość miejsc
        przesuniecie = przesuniecia[i]
        kolumna_deszyfrowana = przesun_tekst(kolumna, przesuniecie, kierunek='lewo')
        kolumny_deszyfrowane.append(kolumna_deszyfrowana)
    
    return kolumny_deszyfrowane
def polacz_kolumny(kolumny_deszyfrowane):
    # Łączymy kolumny, tworząc pełny tekst
    wynik = []
    max_dlugosc = max(len(kolumna) for kolumna in kolumny_deszyfrowane)
    
    for i in range(max_dlugosc):
        for kolumna in kolumny_deszyfrowane:
            if i < len(kolumna):
                wynik.append(kolumna[i])
    
    return ''.join(wynik)

def main():
    # Wczytaj szyfrogram z pliku
    szyfrogram = wczytaj_szyfrogram('szyfrogram.txt')

    dlugosc_klucza_friedman = metoda_friedmana(szyfrogram)
    print(f"Szacowana długość klucza metodą Friedmana: {dlugosc_klucza_friedman}")

    # Znajdź wszystkie powtarzające się sekwencje
    powtorzenia = badanie_powtorzen(szyfrogram)

    # Oblicz odległości między wystąpieniami powtarzających się sekwencji
    odleglosci = oblicz_odleglosci(powtorzenia)

    # Wyświetl wszystkie powtarzające się sekwencje z odległościami
    print(f"Wykryto {len(powtorzenia)} powtarzających się sekwencji:")
    for sek, indeksy in powtorzenia:
        print(f"Sekwencja: {sek}, Powtórzenia: {len(indeksy)}, Indeksy: {indeksy}")
    
    # Wyświetlanie odległości między powtórzeniami
    print("\nOdległości między powtórzeniami:")
    for sek, odleglosci_sekwencji in odleglosci:
        print(f"Sekwencja: {sek}, Odległości: {odleglosci_sekwencji}")

    if odleglosci:
        # Oblicz odległości między wystąpieniami powtarzających się sekwencji
        odleglosci_wszystkie = [odl for sek, odl in odleglosci]
        odleglosci_flat = [item for sublist in odleglosci_wszystkie for item in sublist]

        # Znajdź największy wspólny dzielnik dla odległości
        nwd = znajdz_nwd_dla_odleglosci(odleglosci_flat)
        if nwd:
            print(f"Największy wspólny dzielnik odległości: {nwd}")
        else:
            print("Nie znaleziono wspólnego dzielnika odległości.")

    
    # Podziel szyfrogram na 5 kolumn
    kolumny = podziel_na_kolumny(szyfrogram, klucz_dlugosc=5)
    wypisz_tekst_w_kolumnach(kolumny)
    # Analiza częstotliwości liter w każdej z kolumn
    analiza_czestotliwosci(kolumny)
    wypisz_analizy()
    przesuniecia = [2, 25, 0, 10, 14]  # Przesunięcia na podstawie poprzednich analiz
    kolumny_deszyfrowane = deszyfruj_kolumny(kolumny, przesuniecia)
    
    # Połączenie kolumn w pełny tekst
    tekst_deszyfrowany = polacz_kolumny(kolumny_deszyfrowane)
    
    # Wyświetlenie deszyfrowanego tekstu
    print("\nDeszyfrowany tekst:")
    print(tekst_deszyfrowany)

if __name__ == "__main__":
    main()
