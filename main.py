from app import list, install, remove, search, update, upgrade, settings
import json

port = settings.PORT

# Načte config
def load_config(filename="config.json"):
    with open(filename, "r") as file:
        config = json.load(file)
    return config

# Načte config pro zápis
def save_config(config, filename="config.json"):
    with open(filename, "w") as file:
        json.dump(config, file, indent=4)
# Přidá server do configu
def add_server(name, url):
    new_server = {"name": name, "url": url}
    config["servers"].append(new_server)
    save_config(config)
# Vypíš servery v configu
def list_servers():
    for index, server in enumerate(config["servers"], start=1):
        print(f"{index}. {server['name']} - {server['url']}")
# Ukáže hlavní menu
def show_menu():
    print("Vyberte možnost:")
    print("1. Přidat nový server")
    print("2. Zvolit existující server")
    print("3. Ukončit program")
# Ukáže nabídku s operacemi
def show_menu_operations():
    print("Vyberte možnost:")
    print(selected_server["url"])
    print("1. Výpis nainstalovaných balíčků")
    print("2. Instalace balíčků")
    print("3. Odinstalace balíčků")
    print("4. Vyhledat balíček na serveru")
    print("5. Update repozitáře balíčků")
    print("6. Upgrade balíčků")


    choice = input("Vaše volba: ")
    match choice:
        case "1":
            packages = list.list_packages(selected_server["url"], port)
            print(packages)
            print("Přeješ si uloživ výstup do souboru txt? (y/n)")
            choice = input("Vaše volba: ")
            match choice:
                case "y":
                    filename = input("Název souboru: ")
                    list.write_into_file(packages, filename)
        case "2":
            print(install.install_packages(selected_server["url"], port))
        case "3":
            print(remove.remove_packages(selected_server["url"], port))
        case "4":
            print(search.search_packages(selected_server["url"], port))
        case "5":
            print(update.update_packages(selected_server["url"], port))
        case "6":
            print(upgrade.upgrade_packages(selected_server["url"], port))
        


config = load_config()
servers = config.get("servers", [])

while True:
    show_menu()
    choice = input("Vaše volba: ")

    if choice == "1":
        name = input("Zadejte název nového serveru: ")
        url = input("Zadejte URL nového serveru: ")
        add_server(name, url)
        print("Nový server byl úspěšně přidán.")
    elif choice == "2":
        print("Seznam dostupných serverů:")
        list_servers()
        selection = input("Zvolte číslo serveru pro použití: ")
        try:
            selection_index = int(selection) - 1
            if 0 <= selection_index < len(servers):
                selected_server = servers[selection_index]
                print(f"Byl vybrán server: {selected_server['name']}")
                show_menu_operations()
            else:
                print("Neplatná volba.")
        except ValueError:
            print("Neplatný vstup. Zadejte číslo.")
    elif choice == "3":
        print("Ukončuji program.")
        break
    else:
        print("Neplatná volba. Zadejte číslo možnosti z nabídky.")
