import requests


def remove_packages(url, port):
    packages = input("Zadejte balíčky oddělené čárkami: ")
    packages = packages.split(',')

    try:
        if not packages:
            return {'error': 'No packages provided.'}

        
        endpoint = f"{url}:{port}/packages/remove"

        data = {
            'packages': packages,
        }

        response = requests.post(endpoint, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            return {'error': f'Failed to remove packages. Status code: {response.status_code}'}


    except Exception as e:
        return {'error': str(e)}
