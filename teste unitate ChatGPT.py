"""

Prompt utilizat:

Ești un software tester profesionist. Te rog generează „unity tests” pentru următoarea metodă scrisă în python.
Pentru rulare voi folosi librăria „unittest”. Te rog generează doar testele, gata să fie rulate.
Metoda se află plasată în fișierul „main.py”. Metoda este: [metoda]
    
"""

import unittest
from main import compara_sume, cel_mai_lung_palindrom, ziua_saptamanii_cu_profit_maxim

class TestComparaSume(unittest.TestCase):

    def test_lista_normala(self):
        result = compara_sume([1, 2, 3, 4, 5, 6])
        self.assertEqual(result, (12, 2))  # suma_pare = 2 + 4 + 6 = 12, suma_impare = 1 + 3 + 5 = 9

    def test_lista_impare(self):
        result = compara_sume([1, 3, 5, 7])
        self.assertEqual(result, (16, 1))  # suma_impare = 1 + 3 + 5 + 7 = 16, suma_pare = 0

    def test_lista_pare(self):
        result = compara_sume([2, 4, 6, 8])
        self.assertEqual(result, (20, 2))  # suma_pare = 2 + 4 + 6 + 8 = 20, suma_impare = 0

    def test_lista_goala(self):
        with self.assertRaises(ValueError) as context:
            compara_sume([])
        self.assertEqual(str(context.exception), "Lista de numere nu poate fi goală.")

    def test_lista_contine_elemente_neintregi(self):
        with self.assertRaises(ValueError) as context:
            compara_sume([1, 2, '3', 4])
        self.assertEqual(str(context.exception), "Toate elementele din listă trebuie să fie numere întregi.")

    def test_lista_de_un_singur_element(self):
        result = compara_sume([1])
        self.assertEqual(result, (0, 1))  # suma_pare = 0, suma_impare = 1

    def test_lista_contine_numere_negative(self):
        result = compara_sume([-1, -2, -3, -4])
        self.assertEqual(result, (-4, 1))  # suma_impare = -1 + -3 = -4, suma_pare = -2 + -4 = -6

    def test_lista_numere_mixed(self):
        result = compara_sume([1, -2, 3, -4])
        self.assertEqual(result, (0, 1))  # suma_impare = 1 + 3 = 4, suma_pare = -2 + -4 = -6


class TestCelMaiLungPalindrom(unittest.TestCase):

    def test_cuvant_palindrom(self):
        result = cel_mai_lung_palindrom("ababa")
        self.assertEqual(result, "ababa")  # Palindromul cel mai lung este "ababa"

    def test_cuvant_fara_palindrom(self):
        result = cel_mai_lung_palindrom("abcde")
        self.assertEqual(result, "a")  # Cuvântul cel mai lung palindrom este "a"

    def test_cuvant_mai_multe_palindroame(self):
        result = cel_mai_lung_palindrom("banana")
        self.assertEqual(result, "anana")  # Cel mai lung palindrom este "anana"

    def test_cuvant_goala(self):
        with self.assertRaises(ValueError) as context:
            cel_mai_lung_palindrom("")
        self.assertEqual(str(context.exception), "Cuvântul nu poate fi gol.")

    def test_cuvant_contine_caractere_non_litere(self):
        with self.assertRaises(ValueError) as context:
            cel_mai_lung_palindrom("ab1cd")
        self.assertEqual(str(context.exception), "Toate caracterele trebuie să fie litere din alfabet.")

    def test_cuvant_unu_caracter(self):
        result = cel_mai_lung_palindrom("a")
        self.assertEqual(result, "a")  # Cuvântul are doar un caracter, deci este palindromul cel mai lung

    def test_cuvant_palindrom_mic(self):
        result = cel_mai_lung_palindrom("racecar")
        self.assertEqual(result, "racecar")  # Palindromul cel mai lung este "racecar"

    def test_cuvant_palindrom_mare(self):
        result = cel_mai_lung_palindrom("Aibohphobia")
        self.assertEqual(result, "Aibohphobia")  # Palindromul cel mai lung este "Aibohphobia"

    def test_palindrom_cu_litere_mari_si_mici(self):
        result = cel_mai_lung_palindrom("Aba")
        self.assertEqual(result, "Aba")  # Palindromul cel mai lung este "Aba", indiferent de litere mari

    def test_cuvant_palindrom_interior(self):
        result = cel_mai_lung_palindrom("abcdefghgfedcba")
        self.assertEqual(result, "abcdefghgfedcba")  # Palindromul cel mai lung este întreg cuvântul


class TestZiuaSaptamaniiCuProfitMaxim(unittest.TestCase):

    def test_preturi_normale(self):
        result = ziua_saptamanii_cu_profit_maxim([10, 20, 15, 25, 30, 35, 40])
        self.assertEqual(result, ('Luni', 'Duminică', 30))  # Cumpărarea se face luni, vânzarea duminică, profit 30

    def test_preturi_inordine_descrescatoare(self):
        result = ziua_saptamanii_cu_profit_maxim([100, 90, 80, 70, 60, 50, 40])
        self.assertEqual(result, ('Luni', 'Luni', 0))  # Nu există profit, cumpărarea și vânzarea se fac în aceleași zile

    def test_preturi_inordine_ascendenta(self):
        result = ziua_saptamanii_cu_profit_maxim([10, 20, 30, 40, 50, 60, 70])
        self.assertEqual(result, ('Luni', 'Duminică', 60))  # Cumpărarea se face luni, vânzarea duminică, profit 60

    def test_preturi_egale(self):
        result = ziua_saptamanii_cu_profit_maxim([50, 50, 50, 50, 50, 50, 50])
        self.assertEqual(result, ('Luni', 'Luni', 0))  # Nu există profit, prețurile sunt egale pe toată săptămâna

    def test_preturi_non_valide_mai_putin_de_7(self):
        with self.assertRaises(ValueError) as context:
            ziua_saptamanii_cu_profit_maxim([10, 20, 15, 25, 30, 35])  # doar 6 prețuri
        self.assertEqual(str(context.exception), "Este nevoie de 7 prețuri, câte unul pentru fiecare zi a săptămânii.")

    def test_preturi_non_valide_negativ(self):
        with self.assertRaises(ValueError) as context:
            ziua_saptamanii_cu_profit_maxim([10, -5, 15, 25, 30, 35, 40])  # un preț negativ
        self.assertEqual(str(context.exception), "Toate elementele din lista de prețuri trebuie să fie numere întregi mai mari ca 0.")

    def test_preturi_non_valide_non_int(self):
        with self.assertRaises(ValueError) as context:
            ziua_saptamanii_cu_profit_maxim([10, 20, '15', 25, 30, 35, 40])  # un preț nu este întreg
        self.assertEqual(str(context.exception), "Toate elementele din lista de prețuri trebuie să fie numere întregi mai mari ca 0.")

    def test_preturi_mixed(self):
        result = ziua_saptamanii_cu_profit_maxim([10, 20, 5, 15, 25, 35, 50])
        self.assertEqual(result, ('Luni', 'Duminică', 40))  # Cumpărarea luni, vânzarea duminică, profit 40

    def test_preturi_invalide_lista_golă(self):
        with self.assertRaises(ValueError) as context:
            ziua_saptamanii_cu_profit_maxim([])  # listă goală
        self.assertEqual(str(context.exception), "Este nevoie de 7 prețuri, câte unul pentru fiecare zi a săptămânii.")


if __name__ == '__main__':
    unittest.main()
