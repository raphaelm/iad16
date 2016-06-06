Aufgabe 3: Raumfüllende Kurve
=============================

2a) Implementation
------------------

Das Projektionsverfahren ist in tsp03_spacefilling.py in der Methode
project() umgesetzt. In der selben Datei findet sich eine QuickSort-Implementierung
sowie die Methode spacefilling_tour(), die anhand von project() und quicksort()
eine Tour generiert.

2b) Anwendung
-------------

Die Anwendung des Verfahrens liefert folgende Ergebnisse (gekürzt, damit diese Datei lesbar bleibt):

    $ python tsp03_spacefilling.py ../data/pcb442.tsp
    Tour: [442, 1, 34, 35, 2, 3, 5, 6, 39, 38, 4, 37, ..., 387, 104, 441, 67, 102, 103, 66]
    Length: 65879

    $ python tsp03_spacefilling.py ../data/usa13509.tsp
    Tour: [3, 2, 4, 5, 6, 7, 8, 10, 9, 11, 12, 13, 14, 25, 32, 33, ..., 3181]
    Length: 31044594

    $ python tsp03_spacefilling.py ../data/d18512.tsp
    Tour: [690, 797, 794, 858, 859, 981, 1080, 1356, 1343, 1306, ..., 2802, 2781, 2554, 2645, 2782, 2815]
    Length: 853201

Ein Vergleich mit der Nächster-Nachbar-Heuristik ergibt:

|---------------|------------------|--------------------|
|               | Nächster Nachbar | Raumfüllende Kurve |
|---------------|------------------|--------------------|
| usa13509.tsp  |         24973197 |           31044594 |
| d18512.tsp    |           799220 |             853201 |
| pcb442.tsp    |            61979 |              65879 |
| gr96.tsp      |            70916 |              71299 |
| berlin52.tsp  |             8980 |              10261 |
| HWGrid250.tsp |            37300 |              25000 |
| HWGrid506.tsp |            75700 |              50600 |
|---------------|------------------|--------------------|

Es zeigt sich, dass die raumfüllende Kurve bei unseren Beispielproblemen tendenziell schlechter
abschneidet als die Nächster-Nachbar-Heuristik, wenn auch meist nur um etwa 10%. Eine wirklich
starke Abweichung nach unten zeigt sich nur beim usa13509-Problem. Die HWGrid*-Probleme, die bewusst
so konstruiert waren,dass sie von der Nächster-Nachbar-Näherung schlecht erfasst werden, werden von
der raumfüllenden Kurve jedoch deutlich besser gelöst. Eine mögliche Einordnung der raumfüllenden
Kurve wäre also, dass Sie tendenziell etwas schlechtere Ergebnisse ist als die Nächste-Nachbar-Heuristik,
dafür aber deutlich robuster bei ausgefallenen Problemstellungen.

2c) Charakterisierung des Aufwands
----------------------------------

spacefilling_tour() hat mindestens O(n²) im schlechtesten Fall und O(n log(n)) im durchschnittlichen
Fall, da es Quicksort aufruft. Zusätzlich werden 4 Maxima/Minima berechnet (das geht jeweils in O(n))
und n-mal project() aufgerufen. project() enthält zwei for-Schleifen, die jedoch beide eine feste Anzahl an
Durchläufen haben, project() hat somit O(1). Damit hat spacefilling_tour() die asymptotische Laufzeit
O(spacefilling_tour) = O(quicksort) + O(n) = O(quicksort), d.h. O(n²) im schlechtesten Fall und O(n log(n))
im durchschnittlichen Fall. Damit läuft spacefilling_tour() signifikant schneller als next_neighbor_tour(),
was beim Ausführen der Programme auch deutlich spürbar ist. next_neighbor_tour() braucht für usa13509 etwa
105 Sekunden und spacefilling_tour() nur etwa 0,3 Sekunden auf der selben CPU.
