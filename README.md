Autor: Karol Siłuch

Projekt: Antywirus
Program skanujący pliki w wybranym folderze, ostrzegający przed potęcialnym zagrożeniem.
Wykrywa podejżane pliki i pozwala je usuną.
Antywirus porównuje zawartość pliku z bazą wirusów w pliku virus_database.json.
Porównywanie działa na podstawie porównywania zahashowanej zawartości pliku z zahashowanym wirusem.

Przykład:
dodając do listy w pliku virus_database.json napis '68de3d88c0efb98603398d148882b847' = md5('wirus')
program będzie wykrywał wszyskie pliki z zawartością 'wirus' jako podejrzane.


Podział na klasy:

File - Przechowuje infowrmacje na temat pliku, takie jak nazwa, hash, czy status.
obiekt klasy File nie zna swojego położenia w katalogu. podczas tworzenia obiektu klasy File,
jest on autoatyccznie skanowyany.

Catalog - Służy do zarządzania plikami. W katalogu są zapisane ścieżki do każdego z plików.

Scanner - Służy do importowania plików z folderu na komputerze.

FastScanner - Służy do importowania plików z folderu na komputerze, których informacje nie znajdują się w wybranym indexie.

Antivirus - Pozwala użytkownikowi na łatwe kożystanie z funkcji antywirusa, takich jak skanowanie, szybkie skanowanie, tworzenie i aktualzację indexu, usuwanie zaifekowanych plików.


Instrukcja użytkowania:

-Prosty skan katalogu pod kontem wirusów:
Należy stworzyć obiekt klasy Antywirus, podając ścieżkę do wybranego folderu i wywołać metodę scan

-Stworzenie indexu w wybranym pliku:
Należy stworzyć obiekt klasy Antywirus, podając ścieżkę do wybranego folderu
i wywołać metodę create_index, podając ścieżkę do folderu, w którym ma znadować.

-Aktualizacja indexu:
Należy stworzyć obiekt klasy Antywirus, podając ścieżkę do wybranego folderu i wywołać metodę update_index.

-Szybki skan:
Należy stworzyć obiekt klasy Antywirus, podając ścieżkę do wybranego folderu i wywołać metodę fast_scan.
Obiekt klasy Antywirus do szybkiego skanowania kożysta zawsze z pliku index.json znajdującego się w folderze programu.
jeżeli plik index.json nie istnieje, zostanie wygenerowany automatycznie. Aby wykonać szybki skan w odniesieniu do innego
indexu, należy wykożystać obiekt kalsy FastScanner

-Usuwanie zainfekowanych plików:
Należy stworzyć obiekt klasy Antywirus, podając ścieżkę do wybranego folderu i wywołać metodę repair_catalog.

-Cykliczny skan:
Należy stworzyć obiekt klasy Antywirus, podając ścieżkę do wybranego folderu i wywołać metodę cyclic_scan i podać czas
w sekundach między poszczególnym skanem i ilość skanów do wykonania.


Część refleksyjna:
Aby wykonać projekt, musiałem przeczytać wiele artykułów na temat działania antywirusów. Na początku miałem w planach stworzyć katalog z drzewiastą struktórą plików, zdecydowałem się na słownik, w którym kluczem jest ścieżka a zawartością plik, aby w wygodny sposób kożystać z wbudowanych funkcji pythona.




