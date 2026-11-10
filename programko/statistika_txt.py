def text_statistics(path):
    lines_total = 0
    lines_nonempty = 0
    words_total = 0
    chars_total = 0
    max_line_len = 0

    # Otevření souboru s kódováním UTF-8
    with open(path, 'r', encoding='utf-8') as file:
        # Zpracování po řádcích (bez použití read() nebo readlines())
        for line in file:
            lines_total += 1
            
            # Odstranění odřádkování na konci (funguje pro \n i \r\n)
            clean_line = line.rstrip('\r\n')
            
            # Kontrola neprázdného řádku (po ořezání bílých znaků)
            if clean_line.strip():
                lines_nonempty += 1
                
            # Počet slov na řádku
            words = clean_line.split()
            words_total += len(words)
            
            # Počet znaků bez konce řádku
            line_len = len(clean_line)
            chars_total += line_len
            
            # Aktualizace délky nejdelšího řádku
            if line_len > max_line_len:
                max_line_len = line_len

    return {
        "pocet_vsech_radku": lines_total,
        "pocet_neprazdnych_radku": lines_nonempty,
        "pocet_slov": words_total,
        "pocet_znaku": chars_total,
        "nejdelsi_radek": max_line_len
    }

if __name__ == "__main__":
    path = input("Zadejte cestu k textovému souboru: ").strip()

    try:
        stats = text_statistics(path)
        print("\n--- Výsledné statistiky ---")
        print(f"Počet všech řádků:          {stats['pocet_vsech_radku']}")
        print(f"Počet neprázdných řádků:    {stats['pocet_neprazdnych_radku']}")
        print(f"Počet slov:                  {stats['pocet_slov']}")
        print(f"Počet znaků (bez konec ř.): {stats['pocet_znaku']}")
        print(f"Délka nejdelšího řádku:     {stats['nejdelsi_radek']}")
    except FileNotFoundError:
        print(f"\nChyba: Soubor na cestě '{path}' nebyl nalezen. Zkontrolujte prosím název a cestu k souboru.")