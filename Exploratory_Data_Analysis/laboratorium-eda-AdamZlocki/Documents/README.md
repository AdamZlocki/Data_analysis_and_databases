Opis zmiennych:

* data1: pd.read_csv(f"{DIR}data_with_specified_in_gender.csv") - reprezentuje dane zawarte w pliku:  data_with_specified_in_gender.csv file
Użyte by zaprezentować na wykresach sprzedaż odkurzaczy każdej z firm. Zmienne:
    * Dni od zakupu - (int) number of days since the vaccum cleaner was purchased
    * Marka - (string) brand of the vaccum cleaner
    * Wiek kupującego - (int) age of person who purchased the vaccum cleaner
    * Płeć kupującego - (string) gender of person who bought the vaccum cleaner
    * Ocena - (float) rating given for the vaccum cleaner since the day it was bought

* data2 (identyczne jak data1):
Użyte by zaprezentować różnicę w sprzedaży między kobietami a mężczyznami dla każdej marki

* data3: pd.read_csv(f"{DIR}data_with_proper_age_values.csv") -  reprezentuje dane zawarte w pliku: data_with_proper_age_values.csv file
Użyte by zaprezentować na wykresach różnicę w wieku klientów i oceanch przez nich nadawanych dla każdej makri. Zmienne takie same jak w data1


* Kroki do osiągnięcia takiego rezultatu:
  1) Wczytaj plik csv, który może być znaleziony w katalogu: ../Analysis Data i zapisz pod dowolną zmienną
  2) Utwórz słownik który będzie prezentować relację: vaccum_cleaner_brand -> number_of_people_who_bought_it
  3) Stórzy wykresy przy pomocy plt.subplots and plt.bar
  4) Utwórz kolejny słownik który będzie prezentować relację: vaccum_cleaner_brand -> (number_of_males_who_bought_it, number_of_females_who_bouht_it)
  5) Stwórz wykres pokazujący różnicę między danymi dla kobiet i mężczyzn
  6) Wczytaj kolejny plik csv z tego samego katalogu i zapisz pod nową zmienną
  7) Stwórz wykres dla każdej marki: oś y to liczba ludzi, natomiast na osi x mamy wiek kupujących w przedziałach co 10 lat
  8) Stwórz wykres dla każdej marki: oś x to oceny wydane przez ludzi w skali 0,5-5 z krokiem 0,5, natomiast oś y to ilość ludzi, która wydała daną ocenę
