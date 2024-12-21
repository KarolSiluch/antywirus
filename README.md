Autor: Karol Siłuch

Projekt: Antywirus
Program skanujący pliki w wybranym folderze, ostrzegający przed potęcialnym zagrożeniem.
Wykrywa podejżane pliki i pozwala je usuną.
Antywirus wykrywa testowego wisrusa EICAR.


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



