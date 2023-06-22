Po wczytaniu bazy danych pozbywamy się wierszy, w których w kolumnach
"iso2" lub "year" występuje wartość NaN.
Następnie pozbywamy się wszystkich wierszy, w których występują więcej
niż 4 wartości NaN (4 ponieważ oczekujemy wartości różnej od NaN w kolumanch:
"iso2", "year", "new_sp", oraz w co najmniej jednej z kolejnych kolumn.
W kolejnym kroku pozbywamy się kolumn: "new_sp_m04", "new_sp_f04", "new_sp_m514",
"new_sp_f514" (ponieważ są one równoważne kolumnom "new_sp_m014", "new_sp_f014"),
a także kolumn: "new_sp_mu", "new_sp_fu", gdyż są one w całości wypełnione NaN.
Następnie wszystkie wartości NaN w bazie danych zamieniamy na 0, kolumny "iso2",
oraz "year" ustawiamy jako zmienne identyfikatora, a pozostałe kolumny jako 
wartości mierzone, po czym wydzielamy odpowiednie wartości dla nowych kolumn.
Na końcu naszej pracy z bazą danych wybieramy jedynie interesujące nas kolumny,
sortujemy bazę wg wartości w odpowiednich kolumnach, zmieniamy nazwę "iso2"
na bardziej czytelną, a więc "country", oraz resetujemy indeksy wierszy.
Ostatnim krokiem jest zapisanie bazy do odpowiedniego folderu.