Aufgabe 4: Einfache Modifikationen
==================================

4a) Implementation
------------------

Die einfachen Modifikationen sind in tsp04_modifications.py in den Methoden
modify_2opt() und modify_node_insertion() umgesetzt, wobei diese zwei Methoden
jeweils bis zur ersten gefundenden Optimierung suchen und diese durchführen.
modifications() ist ein Wrapper um die beiden Funktionen, der sie so lange ausführt
bis es keine mögliche Optimierung mehr gibt.

Als Speicherform des Tourgraphen wurde eine Art doppelt verkettete Liste gewählt (NodeLink)

tests/test_tsp04.py enthält Tests für einige der implementierten Hilfsfunktionen.

4b) Experimente
---------------

Die beispielhafte Anwendung des ersten Verfahrens nach Nächster-Nachbar-Heuristik liefert
folgende Ergebnisse:

    $ python tsp04_modifications.py ../data/gr96.tsp neighbor 1
    Moving node 38 after 29 reduces length to 70807
    Moving node 1 after 29 reduces length to 70700
    Moving node 91 after 80 reduces length to 69888
    Moving node 80 after 79 reduces length to 68332
    Moving node 95 after 66 reduces length to 68172
    Moving node 50 after 91 reduces length to 68069
    Moving node 52 after 91 reduces length to 68050
    Moving node 53 after 91 reduces length to 67866
    Moving node 55 after 91 reduces length to 67500
    Moving node 81 after 91 reduces length to 67471
    Moving node 82 after 83 reduces length to 67457
    Moving node 83 after 91 reduces length to 67385
    Moving node 82 after 91 reduces length to 66547
    Moving node 82 after 83 reduces length to 66003
    Moving node 82 after 81 reduces length to 65949
    Moving node 30 after 1 reduces length to 65920
    Moving node 11 after 45 reduces length to 65914
    Moving node 40 after 50 reduces length to 65891
    Moving node 43 after 50 reduces length to 65890
    Moving node 49 after 50 reduces length to 65761
    Moving node 42 after 43 reduces length to 65675
    Moving node 41 after 42 reduces length to 65657
    Moving node 51 after 82 reduces length to 64845
    Moving node 39 after 41 reduces length to 64792
    Moving node 39 after 40 reduces length to 64406
    Moving node 31 after 29 reduces length to 64399
    Moving node 1 after 30 reduces length to 64308
    Moving node 1 after 29 reduces length to 64262
    Moving node 31 after 30 reduces length to 64002
    Moving node 32 after 30 reduces length to 63802
    Moving node 32 after 31 reduces length to 63376
    Moving node 36 after 37 reduces length to 63300
    Moving node 38 after 39 reduces length to 63272
    Moving node 36 after 32 reduces length to 63155
    Moving node 37 after 32 reduces length to 63037
    Moving node 37 after 36 reduces length to 62792
    Moving node 38 after 37 reduces length to 62422
    Moving node 69 after 82 reduces length to 62340
    Moving node 70 after 82 reduces length to 61190
    Moving node 62 after 61 reduces length to 61047
    Moving node 95 after 67 reduces length to 61045
    Moving node 95 after 68 reduces length to 59923
    Moving node 95 after 78 reduces length to 59073
    Moving node 74 after 71 reduces length to 58648
    Moving node 73 after 71 reduces length to 58597
    Moving node 89 after 90 reduces length to 58449
    Moving node 95 after 92 reduces length to 57401
    Moving node 95 after 93 reduces length to 57042
    Moving node 20 after 18 reduces length to 57016
    Moving node 6 after 4 reduces length to 57009
    Moving node 5 after 4 reduces length to 56947
    Moving node 4 after 8 reduces length to 56844
    Moving node 5 after 6 reduces length to 56843
    Moving node 6 after 8 reduces length to 56836
    Moving node 5 after 8 reduces length to 56652
    Moving node 7 after 8 reduces length to 56635
    Moving node 5 after 6 reduces length to 56501
    Tour: [1, 30, 31, 32, 36, 37, 38, 79, 80, 91, 83, 81, 82, 70, 69, 51, 55, 53, 52, 50, 49, 43, 42, 41, 40, 39, 35, 34, 33, 44, 45, 11, 46, 47, 48, 54, 58, 56, 57, 59, 60, 61, 62, 63, 64, 66, 67, 68, 76, 77, 75, 72, 71, 73, 74, 84, 85, 86, 87, 90, 89, 88, 78, 92, 93, 95, 94, 96, 65, 27, 28, 26, 22, 23, 24, 25, 21, 19, 18, 20, 17, 16, 15, 14, 13, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 29]
    Length: 56501

Die Anwendung des zweiten Verfahrens:

    $ python tsp04_modifications.py ../data/gr96.tsp neighbor 2
    Removing edges after 30 and 29 and reconnecting reduces length to 70902
    Removing edges after 30 and 11 and reconnecting reduces length to 70775
    Removing edges after 30 and 31 and reconnecting reduces length to 70690
    Removing edges after 31 and 11 and reconnecting reduces length to 70511
    Removing edges after 31 and 32 and reconnecting reduces length to 70365
    Removing edges after 32 and 11 and reconnecting reduces length to 70085
    Removing edges after 32 and 38 and reconnecting reduces length to 69966
    Removing edges after 32 and 37 and reconnecting reduces length to 69964
    Removing edges after 32 and 36 and reconnecting reduces length to 69754
    Removing edges after 36 and 37 and reconnecting reduces length to 69073
    Removing edges after 79 and 80 and reconnecting reduces length to 66785
    Removing edges after 80 and 81 and reconnecting reduces length to 66705
    Removing edges after 91 and 84 and reconnecting reduces length to 66631
    Removing edges after 38 and 35 and reconnecting reduces length to 66467
    Removing edges after 34 and 39 and reconnecting reduces length to 65599
    Removing edges after 51 and 11 and reconnecting reduces length to 65108
    Removing edges after 49 and 51 and reconnecting reduces length to 64762
    Removing edges after 50 and 45 and reconnecting reduces length to 64439
    Removing edges after 69 and 79 and reconnecting reduces length to 63976
    Removing edges after 57 and 59 and reconnecting reduces length to 63700
    Removing edges after 57 and 70 and reconnecting reduces length to 63423
    Removing edges after 57 and 69 and reconnecting reduces length to 63171
    Removing edges after 80 and 91 and reconnecting reduces length to 62867
    Removing edges after 83 and 81 and reconnecting reduces length to 62540
    Removing edges after 84 and 74 and reconnecting reduces length to 62079
    Removing edges after 73 and 71 and reconnecting reduces length to 62064
    Removing edges after 71 and 59 and reconnecting reduces length to 61877
    Removing edges after 74 and 75 and reconnecting reduces length to 61367
    Removing edges after 75 and 72 and reconnecting reduces length to 60685
    Removing edges after 75 and 73 and reconnecting reduces length to 60174
    Removing edges after 60 and 61 and reconnecting reduces length to 60031
    Removing edges after 68 and 95 and reconnecting reduces length to 59647
    Removing edges after 75 and 76 and reconnecting reduces length to 59559
    Removing edges after 82 and 73 and reconnecting reduces length to 59150
    Removing edges after 68 and 92 and reconnecting reduces length to 59007
    Removing edges after 82 and 84 and reconnecting reduces length to 58465
    Removing edges after 87 and 90 and reconnecting reduces length to 58317
    Removing edges after 78 and 77 and reconnecting reduces length to 56988
    Removing edges after 92 and 93 and reconnecting reduces length to 56629
    Removing edges after 19 and 18 and reconnecting reduces length to 56603
    Removing edges after 7 and 4 and reconnecting reduces length to 56534
    Removing edges after 7 and 8 and reconnecting reduces length to 56106
    Removing edges after 9 and 8 and reconnecting reduces length to 56088
    Tour: [1, 30, 31, 32, 36, 37, 38, 35, 34, 39, 40, 41, 42, 43, 49, 51, 55, 53, 52, 50, 45, 44, 33, 11, 46, 47, 48, 54, 58, 56, 57, 69, 70, 79, 80, 91, 83, 81, 82, 84, 85, 86, 87, 90, 89, 88, 78, 77, 76, 75, 74, 73, 72, 71, 59, 60, 61, 62, 63, 64, 66, 67, 68, 92, 93, 95, 94, 96, 65, 27, 28, 26, 22, 23, 24, 25, 21, 19, 18, 20, 17, 16, 15, 14, 13, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 29]
    Length: 56088

Ein Vergleich ergibt:

Abkürzungen:
    NN = Nächster Nachbar
    SF = Raumfüllende Kurve
    NI = Node insersion
    2O = 2-Opt

|---------------|-----------|-----------|-----------|--------------|--------------|
|               | NN        | NN + NI   | NN + 2O   | NN + NI + 2O | NN + 20 + NI |
|---------------|-----------|-----------|-----------|--------------|--------------|
| gr96.tsp      |     70916 |     56501 |     56088 |        56501 |        55716 |
|               |     100 % |      80 % |      79 % |         80 % |         79 % |
| pcb442.tsp    |     61979 |     56136 |     54285 |        53102 |        53336 |
|               |     100 % |      91 % |      88 % |         86 % |         86 % |
| berlin52.tsp  |      8980 |      8219 |      7967 |         7918 |         7902 |
|               |     100 % |      92 % |      89 % |         89 % |         88 % |
|---------------|-----------|-----------|-----------|--------------|--------------|

|---------------|-----------|-----------|-----------|--------------|--------------|
|               | SF        | SF + NI   | SF + 2O   | SF + NI + 2O | SF + 20 + NI |
|---------------|-----------|-----------|-----------|--------------|--------------|
| gr96.tsp      |     71299 |     58066 |     60226 |        58031 |        57409 |
|               |     100 % |      81 % |      84 % |         81 % |         81 % |
| pcb442.tsp    |     65879 |     56433 |     58611 |        56433 |        56459 |
|               |     100 % |      86 % |      89 % |         86 % |         86 % |
| berlin52.tsp  |     10261 |      8567 |      8790 |         7984 |         8414 |
|               |     100 % |      83 % |      86 % |         78 % |         82 % |
|---------------|-----------|-----------|-----------|--------------|--------------|

Es zeigt sich, dass beide Heuristiken die Ergebnisse der Nächster-Nachbar-Heuristik
oder der raumfüllenden Kurve auf ca. 80-90 % der Tourlänge reduzieren. Es lässt sich nicht
klar sagen, welche Methode besser funktioniert; dies scheint stark vom Problem abzuhängen.
Die Kombination der Methoden bringt fast immer eine weitere Verkürzung der Tour, jedoch keine
starke. Die Reihenfolge scheint keine Rolle zu spielen.


4c) Charakterisierung des Aufwands
----------------------------------

Das konvertieren zwischen den verschiedenen Speicherformaten der Touren dauert O(n).
Das Suchen nach der nächsten möglichen Modifikation muss alle n Knoten durchlaufen und
für jeden Knoten alle n möglichen Modifikations"richtungen" ausprobieren und vergleichen,
wobei das Berechnen einer Tourlänge auch O(n) braucht. Damit sind wir bei einer Gesamtlaufzeit
von O(n + n^2 * (n + T(n))) wobei T(n) die Komplexität für das durchführen einer Tour ist.
Bei der ersten Optimierung (Node insertion) ist T(n) = 1, aber bei der zweiten (2-Opt) ist
T(n) = O(n). Damit ergibt sich in beiden Fällen O(n^3) für das Suchen der nächsten
verbessernden Transformation. Es ist unbekannt wie viele solche Transaktionen es geben kann, aber
die Suche nach *allen* Transformationen dauert dann mindestens O(n^4).