import requests
import json

url = "http://81.2.233.94"


def install_packages(url, port):
    packages = input("Zadejte balíčky oddělené čárkami: ")
    packages = packages.split(',')

    try:
        if not packages:
            return {'error': 'No packages provided.'}

       
        endpoint = f"{url}:{port}/packages/install"

        data = {
            'packages': packages,
        }

        response = requests.post(endpoint, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            return {'error': f'Failed to install packages. Status code: {response.status_code}'}
    except Exception as e:
        return {'error': str(e)}
