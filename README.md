# matrixes
project for university MN


Układy równań liniowych
Macierze są stosowane praktycznie we wszystkich dziedzinach nauki takich jak na przykład elektronice, elektrodynamice, matematyce (np. teorii gier, geometrii analitycznej), grafice komputerowej, mechanice, badaniu wytrzymałości materiałów i konstrukcji, różnego typu symulacji, ekonomii (np. macierz wypłat), akustyce, fotonice, termodynamice, dynamice płynów etc. Używane są w celu uproszczenia rozwiązywania układów równań liniowych. Zatem niezależnie od dziedziny nauki, są one powszechnie wykorzystywane i stanowią podstawowe narzędzie matematyczne. Ponadto, z uwagi na coraz częstszą potrzebę rozwiązywania równań dla układów zawierających setki milionów niewiadomych bardzo ważnym jest, aby były opracowywane nowe metody mające na celu przyspieszenie wykonywania obliczeń. Zagadnienie te jest przedmiotem badań wielu ośrodków naukowych, gdyż rozwój wyżej wymienionych dziedzin jest od niego zależny.

Metody rozwiązania układów równań liniowych dzieli się na dwie klasy:
	Metody bezpośrednie (inaczej skończone) 
	Metody iteracyjne.
	
Pierwsza klasa metod pozwala na uzyskanie rozwiązania po skończonej (a nawet określonej) liczbie działań arytmetycznych a wyznaczone rozwiązanie obarczone jest tylko błędami zaokrągleń. Przykładami takich metod są między innymi: metoda wyznaczników Cramera, metoda eliminacji Gaussa, metoda faktoryzacji LU, metoda QR.

Druga klasa metod polega na wyznaczeniu ciągu wektorów x_0,x_1,x_2,… x_n zbieżnego do rozwiązania układu. Wyznaczone rozwiązanie obarczone jest nie tylko błędami zaokrągleń, lecz także błędem metody – zatem jest przybliżone. Jednakże dużą zaletą metod iteracyjnych jest fakt, iż pozwalają one wyznaczyć rozwiązanie z dowolną, z góry ustaloną dokładnością. Przykładami takich metod są między innymi: metoda Jacobiego, metoda Gaussa-Seidela, metoda najszybszego spadku czy metoda Czebyszewa.

Temat zagadnień

W pracy tej porównane będą metody iteracyjne Jacobiego i Gaussa-Seidla oraz metoda bezpośrednia - metoda faktoryzacji LU.  Porównywane będą one pod względem wydajności oraz rezultatów otrzymanych wyników (zastosowano normę drugą 〖|(|e|)|  〗_2= √(∑_(j=1)^n▒e_j^2 )). Układy równań, dla których wykonywane są obliczenia mają postać 

Ax=b,

gdzie
A – macierz systemowa,
b – wektor pobudzenia,
A – wektor rozwiązań reprezentujący szukaną wielkość fizyczną.
 
 
Zadanie A

Rozpatrywany był układ dla macierzy A o rozmiarze 963x963 posiadającej pięć diagonali: główną, z elementami równymi 13 oraz dwoma poniżej jak i powyżej głównej diagonali, z których każda zawierała elementy równe -1. Natomiast wektor b (o długości 963) zawierał elementy 
b_n=  sin⁡〖(n∙9)〗,n= 0,1,2,…963.

Zadanie B

Porównane zostały metody iteracyjne rozwiązywania układów równań liniowych – tj. metoda Jacobiego oraz Gaussa-Seidla. Z uwagi na fakt, iż wyznaczają one rozwiązanie z góry ustaloną dokładnością – dokładność ta została określona jako wartość normy błędu rezydualnego nie większa niż 10^(-9).
Program zwrócił poniższe wartości dla danych wejściowych:
![alt text](https://github.com/[KrasodomskaAnna]/[matrixes]/blob/[main]/chart_1.png?raw=true)
Wykres 1. Porównanie metod iteracyjnych układów równań liniowych Jacobiego oraz Gaussa-Seidla pod względem liczby potrzebnych iteracji oraz czasu trwania obliczeń dla układu opisanego w zadaniu A.
![alt text](https://github.com/[KrasodomskaAnna]/[matrixes]/blob/[main]/J_res_err_b.png?raw=true)
Wykres 2. Wykres wartości błędu rezydualnego dla kolejnych iteracji dla metody Jacobiego dla układu opisanego w zadaniu A.
![alt text](https://github.com/[KrasodomskaAnna]/[matrixes]/blob/[main]/GS_res_err_b.png?raw=true)
Wykres 3. Wykres wartości błędu rezydualnego dla kolejnych iteracji dla metody Gaussa-Seidla dla układu opisanego w zadaniu A.


Zauważalne jest, iż znajdowanie rozwiązania metodą Gaussa-Seidla trwa o ok 30% szybciej niż metodą Jacobiego. Podobna zależność dotyczy liczby iteracji. Dużo krótszy czas wykonania, jak i liczba iteracji dla metody Gaussa-Seidla jest zgodny z oczekiwaniami, gdyż wspomniany algorytm jest modyfikacją algorytmu Jacobiego polegającą na tym, iż do wyznaczania kolejnych wartości wektora rozwiązania wykorzystuje się obliczone dotychczas wartości (również te z bieżącej iteracji – zatem najbardziej „aktualne”). Zauważalna jest przez to także różnica w wartości błędu rezydualnego na powyższych wykresach – dla metody Jacobiego wartość błędu wynosi niewiele ponad 0 (niezauważalnie dla oka ludzkiego na powyższych wykresach) od iteracji = 5, natomiast dla metody Gaussa-Seidla już od iteracji = 4. W metodzie Jacobiego natomiast wykorzystywany jest w całości wektor uzyskany w wyniku poprzedniej iteracji. Ze względu na fakt, iż jedyną różnicą w działaniu wymienionych metod dla macierzy gęstych jest ta wspomniana, oczekiwane było skrócenie czasu obliczeń (nawet pomimo dodatkowego kosztu poniesionego poprzez wywołanie drugiej pętli for – jak zaimplementowano - lub rozbiciu jej na dwa warunki if). W powyższym przypadku zastosowanie metody Gaussa-Seidla spowodowało przyspieszenie obliczeń o ok 33%.


Zadanie C

Po zmianie wartości, które zawiera główna diagonala macierzy A na 3, wartość błędu rezydualnego dla obydwu metod iteracyjnych zaczyna rosnąć – a w związku z tym oddalać się od wartości rzeczywistej. Oznacza to, iż doszło do rozbieżności. Zbieżność obu analizowanych metod, jak również innych metod iteracyjnych zależy od własności macierzy A. Należy zauważyć, iż
	Jacobi zbiega się, jeżeli promień symetralny macierzy D^(-1) (L+U)<1, a macierz A jest diagonalnie dominująca
	Gauss-Seidel zbiega się, jeżeli macierz A jest symetryczna i dodatnio określona oraz jest diagonalnie dominująca |a_ii |> ∑_(j≠i)▒|a_ij | .
Z uwagi na fakt, iż w pewnym momencie wykonywany algorytm, którego rozwiązanie nie zbiega należy przerwać, w wywołaniu funkcji przekazywany jest parametr określający po której iteracji zostanie zwrócony komunikat "seem to be math.inf". Dla zadanego problemu ustawiono ten parametr na 10^2 (co jest wystarczające dla zadanego problemu).
Program zwrócił poniższe wartości dla danych wejściowych po wykonaniu modyfikacji wartości na głównej diagonali macierzy A:
![alt text](https://github.com/[KrasodomskaAnna]/[matrixes]/blob/[main]/chart_2.png?raw=true)
Wykres 4. Porównanie metod iteracyjnych układów równań liniowych Jacobiego oraz Gaussa-Seidla pod względem liczby potrzebnych iteracji oraz czasu trwania obliczeń dla układu opisanego w zadaniu C.
![alt text](https://github.com/[KrasodomskaAnna]/[matrixes]/blob/[main]/J_res_err_c.png?raw=true)
Wykres 5. Wykres wartości błędu rezydualnego dla kolejnych iteracji dla metody Jacobiego dla układu opisanego w zadaniu C.
![alt text](https://github.com/[KrasodomskaAnna]/[matrixes]/blob/[main]/GS_res_err_c.png?raw=true)
Wykres 6. Wykres wartości błędu rezydualnego dla kolejnych iteracji dla metody Gaussa-Seidla dla układu opisanego w zadaniu C.
Zauważamy zatem, iż warunek zbieżności jest niespełniony, oraz, że wartość błędu rezydualnego rośnie wykładniczo dla obydwu metod.

Zadanie D
Z uwagi na fakt, iż nie otrzymano poprawnego rozwiązania równania dla obydwu metod iteracyjnych – tj. Jacobiego i Gaussa-Seidla, użyto metodę bezpośrednią – metodę faktoryzacji LU w celu znalezienia rozwiązania. Dla metody faktoryzacji LU udało się uzyskać rozwiązanie, gdyż problem rozbieżności nie występuje w przypadku metod bezpośrednich rozwiązywania układów równań liniowych. Jednakże metody bezpośrednie lepiej stosować, gdy metody iteracyjne zawiodą, gdyż metody te wiążą się z dużo większą złożonością obliczeniową, co również skutkuje znacząco dłuższym czasem wykonywania. Należy jednak zauważyć, iż metody bezpośrednie umożliwiają wyznaczenie dokładnego rozwiązania.
Program zwrócił poniższe wartości dla danych wejściowych po wykonaniu modyfikacji wartości na głównej diagonali macierzy A:
![alt text](https://github.com/[KrasodomskaAnna]/[matrixes]/blob/[main]/chart_3.png?raw=true)
Wykres 7. Czas trwania obliczeń oraz wartość normy błędu rezydualnego przy zastosowaniu metody faktoryzacji LU dla układu opisanego w zadaniu C.
Wartość błędu rezydualnego jest różna od zera z uwagi na zaokrąglenia, które występują w trakcie działania programu i są ściśle związane z ograniczoną liczbą bitów, na których można zapisać liczbę zmiennoprzecinkową. Z uwagi na to, iż wartość ta jest pomijalnie niska, wyznaczone rozwiązanie może zostać uznane za dokładne.
Zadanie E
Dla macierzy A opisanej w zadaniu A zostały zaprezentowane wyniki porównania iteracyjnych – Jacobiego i Gaussa-Seidla oraz metody bezpośredniej – faktoryzacji LU. Porównanie te zostało przeprowadzone pod kątem złożoności czasowej w zależności od liczby niewiadomych N (zatem od rozmiaru macierzy A) dla N= {100,500,1000,2000,3000,4000,5000}.
Wyniki porównania metod rozwiązywania układów równań liniowych:
![alt text](https://github.com/[KrasodomskaAnna]/[matrixes]/blob/[main]/zadanie_e.png?raw=true)
Wykres 8. Porównanie czasów wykonania algorytmów Jacobiego, Gaussa-Seidla oraz faktoryzacji LU układów liniowych o różnej liczbie niewiadomych N. 

Dla układów równań, w których liczba niewiadomych jest niewielka (N ≤ 1000) czasy trwania metod iteracyjnych jak i metody bezpośredniej są podobne, jednak już po przekroczeniu tej granicy różnica staje się bardzo szybko coraz mocniej znacząca. Czas wykonania metody faktoryzacji LU jest znacząco mniejszy niż metod bezpośrednich z uwagi na zastosowane usprawnienie obliczania jej (jeżeli wartość  L[j,k]=0, to U[j,i] nie ulegnie zmianie – zatem można pominąć ostatnią pętlę for). Z uwagi na fakt, iż algorytmy były porównywane dla macierzy, której większość wartości pól to 0, usprawnienie te przyniosło bardzo dobry rezultat. 
Wyniki porównania metod rozwiązywania układów równań liniowych bez zastosowania usprawnienia:
![alt text](https://github.com/[KrasodomskaAnna]/[matrixes]/blob/[main]/500_bez_usprawnien.png?raw=true)
Wykres 9. Porównanie czasów wykonania algorytmów Jacobiego, Gaussa-Seidla oraz faktoryzacji LU (bez zastosowania usprawnienia) układów liniowych o różnej liczbie niewiadomych N. 
![alt text](https://github.com/[KrasodomskaAnna]/[matrixes]/blob/[main]/3000_bez_usprawnien.png?raw=true)
Wykres 10. Porównanie czasów wykonania algorytmów Jacobiego, Gaussa-Seidla oraz faktoryzacji LU (bez zastosowania usprawnienia) układów liniowych o różnej liczbie niewiadomych N. 

Bez zastosowania wspomnianego usprawnienia czas obliczeń dla faktoryzacji LU rośnie gwałtownie w górę. Należy zauważyć, że już dla N=500 czas faktoryzacji LU (bez usprawnienia) wynosi ponad 14 s, gdzie dla obydwu metod iteracyjnych nie przekracza on 2s, natomiast dla N=3000 dla faktoryzacji LU czas wynosi ponad 3000s (50 min), gdzie czas dla metod iteracyjnych jest znikomy.
Porównując algorytmy iteracyjne należy zauważyć, że dla zwiększającej się liczby niewiadomych, coraz bardziej znaczące jest wykorzystanie w obliczeniach dotychczas obliczonych wartości (a nie tych z poprzedniej iteracji). Można oczekiwać, że dla coraz większych N różnica ta będzie coraz bardziej znacząca.
Podsumowanie
Należy zauważyć, że metody iteracyjne są znacznie szybsze (jeśli nie stosuje się usprawnienia dla faktoryzacji LU dla pustych pól macierzy), a dokładność obliczonych przez nie wyników można z góry ustalić. W związku z tym dla macierzy, które spełniają warunek zbieżności lepiej jest stosować metody iteracyjne. Dla macierzy niespełniających tego warunku jedynym poprawnym wyborem metody wyznaczenia rozwiązania jest zastosowanie wybranej metody bezpośredniej. Natomiast warto zauważyć, iż dla wspomnianego wcześniej prostego usprawnienia obliczeń, metoda faktoryzacji LU pozwala na znacznie szybsze wyznaczenie rozwiązania dla zadanej macierzy (której wartości były w dużej mierze równe 0).
Źródła
Ratajczak T. (2006), Metody numeryczne: przykłady i zadania, Wydawnictwo Politechniki Gdańskiej
https://wazniak.mimuw.edu.pl/index.php?title=MN08
https://pg.edu.pl/documents/1103764/59866917/url_metody_J_GS.pdf
https://www.naukowiec.org/wiedza/matematyka/macierze_603.html
https://courses.physics.illinois.edu/cs357/sp2020/notes/ref-9-linsys.html
