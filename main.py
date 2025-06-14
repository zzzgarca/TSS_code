def compara_sume(lista_numere: list) -> tuple[str, int]:
    """
    Primește o listă de numere întregi și returnează:
    - un mesaj care indică dacă suma numerelor pare sau impare este mai mare,
      sau dacă sumele sunt egale, împreună cu valoarea sumei mai mari;
    - un cod numeric care indică una din următoarele:
        - 2 dacă suma numerelor pare este mai mare
        - 1 dacă suma numerelor impare este mai mare
        - 0 dacă sumele sunt egale

    Întoarce eroare dacă lista conține elemente care nu sunt întregi.
    """
    if not all(isinstance(element, int) for element in lista_numere):
        raise ValueError("Toate elementele din listă trebuie să fie numere întregi.")
        
    if lista_numere == []:
        raise ValueError("Lista de numere nu poate fi goală.")

    suma_pare = 0
    suma_impare = 0

    for numar in lista_numere:
        if numar % 2 == 0:
            suma_pare += numar
        else:
            suma_impare += numar

    if suma_pare > suma_impare:
        return suma_pare, 2
    elif suma_impare > suma_pare:
        return suma_impare, 1
    else:
        return suma_pare, 0



def cel_mai_lung_palindrom(cuvant: str) -> str:
    """
    Primește un cuvânt și returnează cel mai lung palindrom conținut în cuvânt.
    Întoarce eroare dacă cuvântul conține alte caractere decât litere.
    """
    
    if cuvant =='':
        raise ValueError("Cuvântul nu poate fi gol.")

    
    if len(cuvant) == 1:
        return cuvant

    litere_mici = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
        'u', 'v', 'w', 'x', 'y', 'z'
    )
    litere_mari = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    )

    if not all(caracter in litere_mici or caracter in litere_mari for caracter in cuvant):
        raise ValueError("Toate caracterele trebuie să fie litere din alfabet.")

    lungime_maxima = 1
    palindrom_maxim = cuvant[0]

    for inceput in range(len(cuvant) - 1):
        for sfarsit in range(inceput + 1, len(cuvant)):
            inversat = []
            for pozitie in range(sfarsit, inceput - 1, -1):
                inversat.append(cuvant[pozitie].lower())
            inversat = ''.join(inversat)

            subcuvant = cuvant[inceput:sfarsit + 1].lower()
            forma_originala=cuvant[inceput:sfarsit + 1]
            if len(subcuvant) > lungime_maxima and subcuvant == inversat:
                lungime_maxima = len(subcuvant)
                palindrom_maxim = forma_originala

    return palindrom_maxim




def ziua_saptamanii_cu_profit_maxim(preturi_zilnice: list[int]) -> str:
    """
    Returnează ziua din săptămână în care cumpărarea ar fi generat 
    cel mai mare profit, vânzând într-o zi ulterioară.

    Parametri:
        preturi_zilnice (list[int]): Listă de 7 prețuri corespunzătoare celor 7 zile ale săptămânii.

    Returnează:
        str: Un mesaj care indică ziua optimă de cumpărare și vânzare, împreună cu profitul maxim.
    """
    if not all(isinstance(element, int) and element > 0 for element in preturi_zilnice):
        raise ValueError("Toate elementele din lista de prețuri trebuie să fie numere întregi mai mari ca 0.")
    
    if len(preturi_zilnice) != 7:
        raise ValueError("Este nevoie de 7 prețuri, câte unul pentru fiecare zi a săptămânii.")
        
    zilele_saptamanii = ('Luni', 'Marți', 'Miercuri', 'Joi', 'Vineri', 'Sâmbătă', 'Duminică')
    
    profit_maxim = 0
    zi_cumparare = 0
    zi_vanzare = 0

    for i in range(len(preturi_zilnice) - 1):  # zi de cumpărare
        for j in range(i + 1, len(preturi_zilnice)):  # zi de vânzare
            profit = preturi_zilnice[j] - preturi_zilnice[i]
            if profit > profit_maxim:
                profit_maxim = profit
                zi_cumparare = i
                zi_vanzare = j
    
    return (zilele_saptamanii[zi_cumparare], zilele_saptamanii[zi_vanzare], profit_maxim)
