import unittest
from main import compara_sume, cel_mai_lung_palindrom, ziua_saptamanii_cu_profit_maxim


"""
Teste funcționale

Partiționare de echivalență pentru metoda compara_sume
"""
# T1: lsita conține și alte elemente decât numere pare => ValueError
# T2: lista conține numai elemente pare => pare, suma tuturor elementelor
# T3: lista conține numai elemente impare => impare, suma tuturor elementelor
# T4: lista conție elemente pare și impare, dar cele impare au sumă mai mare => impare, suma celor impare
# T5: lista conție elemente pare și impare, dar cele pare cu sumă mai mare => impare, suma celor pare
# T6: lista conție elemente pare și impare cu sume egale => impare, suma celor pare
# T7: lista goala => ValueError

class TestComparaSumeFunctionalPartitionareEchivalenta(unittest.TestCase):

    def test_lista_contine_elemente_neintregi(self):
        # T1: lista conține elemente neîntregi
        with self.assertRaises(ValueError):
            compara_sume([1, 2, "abc", 3])

    def test_lista_numai_cu_elemente_pare(self):
        # T2: lista conține doar numere pare
        suma, cod = compara_sume([2, 4, 6])
        self.assertEqual(suma, 12)
        self.assertEqual(cod, 2)

    def test_lista_numai_cu_elemente_impare(self):
        # T3: lista conține doar numere impare
        suma, cod = compara_sume([1, 3, 5])
        self.assertEqual(suma, 9)
        self.assertEqual(cod, 1)

    def test_imparele_au_suma_mai_mare(self):
        # T4: suma imparelor e mai mare
        suma, cod = compara_sume([1, 2, 3, 5])
        self.assertEqual(suma, 9)
        self.assertEqual(cod, 1)

    def test_parele_au_suma_mai_mare(self):
        # T5: suma parelor e mai mare
        suma, cod = compara_sume([1, 2, 4, 6])
        self.assertEqual(suma, 12)
        self.assertEqual(cod, 2)

    def test_sume_egale(self):
        # T6: sumele sunt egale
        suma, cod = compara_sume([2, 3, 4, 6, 9])
        self.assertEqual(suma, 12)
        self.assertEqual(cod, 0)

    def test_lista_goala(self):
        # T7: lista este goală
        with self.assertRaises(ValueError):
            compara_sume([])


"""
Partiționare de echivalență pentru metoda cel_mai_lung_palindrom
"""

# T1: cuvântul conține și alte elemente decât litere => ValueError
# T2: cuvântul nu conține palindroame => prima literă a cuvântului 
# T3: cuvântul conține un palindrom (cel puțin două litere) => întoarce palindromul
# T4: cuvântul conține două sau mai multe palindroame, iar cele mai lungi au lungimea egală => primul palindrom din cele mai lungi
# T5: cuvântul conține două sau mai multe palindroame de lungi diferite, => cel mai lung palindrom
# T6: cuvântul este gol => ValueError
# T7: cuvântul conține palindroame dar unele litere din plaindrom sunt mari iar altele sunt mici => cel mai lung palindorm indiferent de tipul literelor

class TestCelMaiLungPalindrom(unittest.TestCase):
    
    # T1: conține alte caractere decât litere
    def test_caractere_nevalide(self):
        with self.assertRaises(ValueError):
            cel_mai_lung_palindrom("abc123")
    
    # T2: nu conține palindroame => returnează prima literă
    def test_fara_palindrom(self):
        self.assertEqual(cel_mai_lung_palindrom("abc"), "a")
    
    # T3: cuvântul conține un singur palindrom
    def test_un_palindrom(self):
        self.assertEqual(cel_mai_lung_palindrom("abccba"), "abccba")
    
    # T4: două palindroame egale ca lungime => returnează primul
    def test_doua_palindroame_egale(self):
        self.assertEqual(cel_mai_lung_palindrom("abccbaxyzyx"), "abccba")
    
    # T5: două palindroame, dar unul mai lung
    def test_doua_palindroame_inegale(self):
        self.assertEqual(cel_mai_lung_palindrom("abccbaxyyx"), "abccba")
    
    # T6: cuvânt gol
    def test_cuvant_gol(self):
        with self.assertRaises(ValueError):
            cel_mai_lung_palindrom("")
            
    # T7: plaindraoame construite cu combinații de litere mici și litere mari
    def test_palindroame_litere_mici_mari(self):
        self.assertEqual(cel_mai_lung_palindrom("Abccbaxyyx"), "Abccba")


"""
Partiționare de echivalență pentru ziua_saptamanii_cu_profit_maxim
"""

# T1: lista de prețuri conține altceva înafară de numere întregi 
# T2: lista de prețuri conține mai multe sau mai puține prețuri decât 7
# T3: profitul maxim este 0 în oricare zi => Luni, Luni, 0
# T4: toate zilele pot aduce profit diferit de 0 => Ziua de cumpărare, ziua de vânzare, profitul
# T5: Cel puțin două zilele pot aduce profit maximal egal => Prima zi de cumpărare, ziua de vânzare pentru prima zi, profitul

class TestZiuaSaptamaniiCuProfitMaxim(unittest.TestCase):
    
    def test_t1_elemente_neintregi(self):
        # T1: lista conține altceva decât numere întregi pozitive
        with self.assertRaises(ValueError):
            ziua_saptamanii_cu_profit_maxim([10, 12, 13, "a", 16, 15, 14])

    def test_t2_lungime_lista_invalida(self):
        # T2: lista nu conține exact 7 prețuri
        with self.assertRaises(ValueError):
            ziua_saptamanii_cu_profit_maxim([10, 12, 13, 15])

    def test_t3_fara_profit_posibil(self):
        # T3: prețurile scad și ca urmare  profitul maxim este 0
        rezultat = ziua_saptamanii_cu_profit_maxim([10, 9, 8, 7, 6, 5, 4])
        self.assertEqual(rezultat, ("Luni", "Luni", 0))

    def test_t4_profit_maxim_clar_diferit(self):
        # T4: toate zilele pot aduce profit diferit
        rezultat = ziua_saptamanii_cu_profit_maxim([10, 11, 12, 8, 14, 7, 15])
        self.assertEqual(rezultat, ("Sâmbătă", "Duminică", 8))

    def test_t5_profit_maxim_apare_de_mai_multe_ori(self):
        # T5: două perioade cu același profit maxim, alegem prima
        rezultat = ziua_saptamanii_cu_profit_maxim([10, 12, 10, 12, 10, 12, 10])
        self.assertEqual(rezultat, ("Luni", "Marți", 2))



if __name__ == "__main__":
    unittest.main()