def obchod():
    sklad = {   "chlieb": [1.49, 10],
        "mlieko": [0.99, 15],
        "maslo": [2.20, 5],
        "kava": [5.49, 8],
        "jablka": [1.89, 15],
        "quapka": [3.99, 12]}
    
    kosik = {}
    
    print("Čau, vitaj v mojom obchode!")
    
    while True:
        print("\n--- AKTUÁLNY STAV SKLADU ---")
        for tovar, info in sklad.items():
            print(f"{tovar} - cena: {info[0]} € | na sklade: {info[1]} ks")
        print("-" * 30)
        
        volba = input("Čo chceš kúpiť? (napíš 'koniec' pre ukončenie): ").strip().lower()
        
        if volba == "koniec":
            break
            
        if volba not in sklad:
            print("Prepáč, toto nemáme.\n")
            continue
            
        zostava = sklad[volba][1]
        if zostava == 0:
            print("Sorry bro toto je už vypredané\n")
            continue
            
        mnozstvo_str = input(f"Koľko kusov chceš? (dostupné: {zostava}): ")
         
        if not mnozstvo_str.isdigit():
            print("fratello musíš zadať číslo väčšie ako 0!\n")
            continue
            
        mnozstvo = int(mnozstvo_str)
        
        if mnozstvo <= 0:
            print("fratello musíš zadať číslo väčšie ako 0!\n")
            continue
            
        if mnozstvo > zostava:
            print("Prepáč toľko kusov nie je na sklade.\n")
            continue
            
        sklad[volba][1] -= mnozstvo
        
        if volba in kosik:
            kosik[volba] += mnozstvo
        else:
            kosik[volba] = mnozstvo
            
        print("Pridané do košíka!\n")
   
    print("\n" + "=" * 30)
    print("          TVOJ KOŠÍK          ")
    print("=" * 30)

    if not kosik:
        print("Košík je prázdny.")
    else:
        celkova_suma = 0
        for tovar, ks in kosik.items():
            cena = sklad[tovar][0]
            spolu = cena * ks
            celkova_suma += spolu
            print(f"- {tovar}: {ks} ks x {cena} € = {spolu:.2f} €")

        print("-" * 30)
        print(f"Celková cena  zľavy: {celkova_suma:.2f} €")
        
        zlava = celkova_suma * 0.10
        finalna_suma = celkova_suma - zlava
        
        print(f"Zľava (10%): -{zlava:.2f} €")
        print(f"CENA PO ZĽAVE: {finalna_suma:.2f} €")
        print("=" * 30)

if __name__ == "__main__":
    obchod()
