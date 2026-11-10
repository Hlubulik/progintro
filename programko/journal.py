

FILE_PATH = "journal.txt"

def nacti_zaznamy():
    try:
        with open(FILE_PATH, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def pridej_zaznam(zaznam):
    with open(FILE_PATH, "a") as file:
        file.write(zaznam + "\n")

def add_entry():
    zaznam = input("Zadejte nový záznam: ")
    pridej_zaznam(zaznam)
    print("Záznam byl přidán.")

def list_entries():
    try:
        with open(FILE_PATH, "r") as file:
            zaznamy = file.readlines()
            if not zaznamy:
                print("Žádné záznamy nebyly nalezeny.")
            else:
                print("Seznam záznamů:")
                for index, zaznam in enumerate(zaznamy, start=1):
                    print(f"{index}. {zaznam.strip()}")
    except FileNotFoundError:
        print("Soubor s deníkem neexistuje.")

def search_entries():
    hledany_text = input("Zadejte text pro vyhledávání: ")
    try:
        with open(FILE_PATH, "r") as file:
            zaznamy = file.readlines()
            nalezene_zaznamy = [zaznam.strip() for zaznam in zaznamy if hledany_text in zaznam]
            if not nalezene_zaznamy:
                print("Žádné záznamy nebyly nalezeny.")
            else:
                print("Nalezené záznamy:")
                for index, zaznam in enumerate(nalezene_zaznamy, start=1):
                    print(f"{index}. {zaznam}")
    except FileNotFoundError:
        print("Soubor s deníkem neexistuje.")