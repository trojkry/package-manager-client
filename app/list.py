import requests

def list_packages(url, port):
    
    url = f"{url}:{port}/packages/list"
    response = requests.post(url)
    
    if response.status_code == 200:
        data = response.json()
        list_result = data.get("list_result", {})
        
        if list_result:
            output = list_result.get("output", "")
            return output.strip()
            
    return "Chyba při získávání seznamu balíčků."

def write_into_file(formatted_packages, filename):
    with open(filename, "w") as file:
        file.write(formatted_packages)
    print("Výstup byl zapsán do souboru " + filename +".txt")
