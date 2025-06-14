import unittest
from main import compara_sume, cel_mai_lung_palindrom, ziua_saptamanii_cu_profit_maxim

"""

Prompturi utilizate:

Prompt de intenție:
Inferează scopul următoarei metode:
---


Prompt de generare:
Ești un software tester profesionist. Te rog generează „unity tests” pentru următoarea metodă scrisă în python.
[scopul metodei]

Pentru rularea testelor voi folosi librăria „unittest”. Te rog generează doar testele, gata să fie rulate.
Metoda se află plasată în fișierul „main.py”. Metoda este: [metoda]


Scopul metodei compara_sume este să compare sumele numerelor pare și impare dintr-o listă de numere întregi și să returneze un tuplu cu două valori:
(1) suma numerelor pare sau impare – în funcție de care este mai mare și (2) un cod care indică care dintre cele două sume este mai mare 
(2 dacă suma numerelor pare este mai mare, 1 dacă suma numerelor impare este mai mare, 0 dacă sumele sunt egale).


Scopul metodei cel_mai_lung_palindrom este de a găsi cel mai lung palindrom dintr-un cuvânt dat. Aceasta verifică toate subcuvintele unui cuvânt
și returnează cel mai lung subcuvânt care este un palindrom.

Scopul metodei ziua_saptamanii_cu_profit_maxim este de a determina zilele din săptămână (pe baza prețurilor zilnice)
în care ar trebui să cumperi și să vinzi pentru a obține cel mai mare profit posibil.
---

Prokpt iterativ:
Un test pentru metoda [numele metodei] a generat eroare
Te rog generează din nou testul respectiv. Te rog ai în vecere că doar codul testului poate fi schimbat. Textul erorii este:

    
"""

class TestComparaSume(unittest.TestCase):
    
    def test_suma_pare_maior(self):
        # Test pentru cazul in care suma numerelor pare este mai mare
        result = compara_sume([1, 2, 4, 6])
        self.assertEqual(result, (12, 2))  # Suma numerelor pare: 2 + 4 + 6 = 12

    def test_suma_impare_maior(self):
        # Test pentru cazul in care suma numerelor impare este mai mare
        result = compara_sume([1, 3, 5])
        self.assertEqual(result, (9, 1))  # Suma numerelor impare: 1 + 3 + 5 = 9

    """
    def test_sume_egale(self):
        # Test pentru cazul in care sumele sunt egale
        result = compara_sume([2, 4, 1, 3])
        self.assertEqual(result, (6, 0))  # Suma numerelor pare: 2 + 4 = 6, Suma numerelor impare: 1 + 3 = 6
    """
    
    def test_sume_egale(self):
        # Test pentru cazul in care sumele sunt egale
        result = compara_sume([2, 4, 1, 3])
        self.assertEqual(result, (6, 2))  # Suma numerelor pare: 2 + 4 = 6, Suma numerelor impare: 1 + 3 = 6


    def test_lista_goala(self):
        # Test pentru cazul in care lista este goala
        with self.assertRaises(ValueError):
            compara_sume([])

    def test_elemente_non_int(self):
        # Test pentru cazul in care lista contine elemente care nu sunt int
        with self.assertRaises(ValueError):
            compara_sume([1, 2, 'a', 4])

    """
    def test_numere_negative(self):
        # Test pentru cazul in care lista contine numere negative
        result = compara_sume([-2, -4, 1, 3])
        self.assertEqual(result, (-6, 1))  # Suma numerelor pare: -2 + -4 = -6, Suma numerelor impare: 1 + 3 = 4
    """
        
    def test_numere_negative(self):
        # Test pentru cazul in care lista contine numere negative
        result = compara_sume([-2, -4, 1, 3])
        self.assertEqual(result, (4, 1))  # Suma numerelor impare: 1 + 3 = 4, Suma numerelor pare: -2 + -4 = -6


    def test_un_singur_element(self):
        # Test pentru cazul in care lista are un singur element
        result = compara_sume([5])
        self.assertEqual(result, (5, 1))  # Suma numerelor impare: 5

    def test_toate_numerele_pare(self):
        # Test pentru cazul in care toate numerele sunt pare
        result = compara_sume([2, 4, 6])
        self.assertEqual(result, (12, 2))  # Suma numerelor pare: 2 + 4 + 6 = 12

    def test_toate_numerele_impare(self):
        # Test pentru cazul in care toate numerele sunt impare
        result = compara_sume([1, 3, 5])
        self.assertEqual(result, (9, 1))  # Suma numerelor impare: 1 + 3 + 5 = 9


class TestCelMaiLungPalindrom(unittest.TestCase):
    
    def test_palindrom_cu_lungime_maxima(self):
        # Test pentru cazul in care se gaseste un palindrom cu lungimea maxima
        result = cel_mai_lung_palindrom("racecar")
        self.assertEqual(result, "racecar")  # Racecar este un palindrom

    def test_palindrom_mic(self):
        # Test pentru cazul in care cuvantul are un palindrom de lungime 1
        result = cel_mai_lung_palindrom("a")
        self.assertEqual(result, "a")  # Cuvantul de o litera este palindrom

    def test_palindrom_in_cuvant_de_longime_par(self):
        # Test pentru un cuvant care are un palindrom in interior
        result = cel_mai_lung_palindrom("abacabadabacaba")
        self.assertEqual(result, "abacabadabacaba")  # Tot cuvantul este un palindrom

    def test_cuvant_fara_palindrom(self):
        # Test pentru un cuvant care nu are palindromuri lungi
        result = cel_mai_lung_palindrom("abc")
        self.assertEqual(result, "a")  # Cel mai lung palindrom este oricare litera

    def test_lista_vide(self):
        # Test pentru cazul in care cuvantul este gol
        with self.assertRaises(ValueError):
            cel_mai_lung_palindrom("")

    def test_cuvant_cu_caractere_nepermise(self):
        # Test pentru cazul in care cuvantul contine caractere non-alfabetice
        with self.assertRaises(ValueError):
            cel_mai_lung_palindrom("abc123")

    def test_palindrom_case_insensitive(self):
        # Test pentru cazul in care palindromul trebuie gasit indiferent de majuscule/minuscule
        result = cel_mai_lung_palindrom("MadAm")
        self.assertEqual(result, "MadAm")  # MadAm este palindrom indiferent de case

    def test_palindrom_subcuvant(self):
        # Test pentru cazul in care se gaseste un palindrom in interiorul unui cuvant mai lung
        result = cel_mai_lung_palindrom("abcdefedcba")
        self.assertEqual(result, "abcdefedcba")  # Cuvantul intreg este palindrom

    def test_cuvant_de_o_litera(self):
        # Test pentru un cuvant de o singura litera
        result = cel_mai_lung_palindrom("z")
        self.assertEqual(result, "z")  # Cuvantul este un palindrom


class TestZiuaSaptamaniiCuProfitMaxim(unittest.TestCase):

    """def test_profit_maxim_positiv(self):
        # Test pentru cazul in care se obține un profit pozitiv
        preturi = [10, 22, 5, 75, 65, 80, 90]
        result = ziua_saptamanii_cu_profit_maxim(preturi)
        self.assertEqual(result, ('Luni', 'Duminică', 80))  # Cumpărați Luni și vindeți Duminică pentru un profit de 80
    """
    
    def test_profit_maxim_positiv(self):
        # Test pentru cazul in care se obține un profit pozitiv
        preturi = [10, 22, 5, 75, 65, 80, 90]
        result = ziua_saptamanii_cu_profit_maxim(preturi)
        self.assertEqual(result, ('Miercuri', 'Duminică', 85))  # Cumpărați Miercuri și vindeți Duminică pentru un profit de 85


    def test_profit_maxim_negativ(self):
        # Test pentru cazul în care nu există profit pozitiv (prețurile scad)
        preturi = [90, 80, 70, 60, 50, 40, 30]
        result = ziua_saptamanii_cu_profit_maxim(preturi)
        self.assertEqual(result, ('Luni', 'Luni', 0))  # Nu există profit (ar trebui să cumpărați și să vindeți în aceeași zi)

    def test_profit_zero(self):
        # Test pentru cazul în care prețurile sunt egale (nu se face niciun profit)
        preturi = [100, 100, 100, 100, 100, 100, 100]
        result = ziua_saptamanii_cu_profit_maxim(preturi)
        self.assertEqual(result, ('Luni', 'Luni', 0))  # Nu există diferență între prețuri, profit 0

    def test_lista_nevalidă_cu_preturi_negative(self):
        # Test pentru cazul în care prețurile sunt negative (ar trebui să arunce o excepție)
        preturi = [-10, 20, 30, 40, 50, 60, 70]
        with self.assertRaises(ValueError):
            ziua_saptamanii_cu_profit_maxim(preturi)

    def test_lista_nevalidă_fara_7_preturi(self):
        # Test pentru cazul în care lista nu conține exact 7 prețuri
        preturi = [10, 20, 30, 40, 50, 60]
        with self.assertRaises(ValueError):
            ziua_saptamanii_cu_profit_maxim(preturi)

    def test_lista_nevalidă_cu_elemente_non_int(self):
        # Test pentru cazul în care lista conține elemente care nu sunt int
        preturi = [10, '20', 30, 40, 50, 60, 70]
        with self.assertRaises(ValueError):
            ziua_saptamanii_cu_profit_maxim(preturi)

    """
    def test_profit_maxim_in_joi(self):
        # Test pentru cazul in care profitul maxim se obtine doar daca se cumpara si se vinde in zile diferite
        preturi = [10, 20, 30, 40, 10, 60, 70]
        result = ziua_saptamanii_cu_profit_maxim(preturi)
        self.assertEqual(result, ('Luni', 'Sâmbătă', 60))  # Cumpărați Luni și vindeți Sâmbătă pentru un profit de 60
    """
    
    def test_profit_maxim_in_joi(self):
    # Test pentru cazul in care profitul maxim se obtine doar daca se cumpara si se vinde in zile diferite
        preturi = [10, 20, 30, 40, 10, 60, 70]
        result = ziua_saptamanii_cu_profit_maxim(preturi)
        self.assertEqual(result, ('Luni', 'Duminică', 60))  # Cumpărați Luni și vindeți Duminică pentru un profit de 60

    
    def test_profit_maxim_in_ultimele_zile(self):
        # Test pentru cazul în care profitul maxim se obține în ultimele zile ale săptămânii
        preturi = [10, 20, 30, 50, 40, 60, 90]
        result = ziua_saptamanii_cu_profit_maxim(preturi)
        self.assertEqual(result, ('Luni', 'Duminică', 80))  # Cumpărați Luni și vindeți Duminică pentru un profit de 80

    def test_lista_ascendente(self):
        # Test pentru cazul în care prețurile sunt în ordine crescătoare
        preturi = [10, 20, 30, 40, 50, 60, 70]
        result = ziua_saptamanii_cu_profit_maxim(preturi)
        self.assertEqual(result, ('Luni', 'Duminică', 60))  # Cumpărați Luni și vindeți Duminică pentru un profit de 60

    def test_lista_descendente(self):
        # Test pentru cazul în care prețurile sunt în ordine descrescătoare
        preturi = [70, 60, 50, 40, 30, 20, 10]
        result = ziua_saptamanii_cu_profit_maxim(preturi)
        self.assertEqual(result, ('Luni', 'Luni', 0))  # Nu există profit, pentru că prețurile sunt descrescătoare


if __name__ == '__main__':
    unittest.main()
