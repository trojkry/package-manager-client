import requests


def search_packages(url, port):
    package = input("Zadejte balíčky oddělené čárkami: ")
    package = package.split(',')

    try:
        if not package:
            return {'error': 'No package provided.'}

        endpoint = f"{url}:{port}/packages/search"

        data = {'package': package}

        response = requests.post(endpoint, json=data)

        if response.status_code == 200:
            result = response.json()
            output = extract_output(result)
            return output
        else:
            return {'error': f'Failed to search for package. Status code: {response.status_code}'}
    except Exception as e:
        return {'error': str(e)}

def extract_output(results):
    output = ""
    for command, result in results.items():
        output += result.get('output', '') + "\n"
    return output.strip()

