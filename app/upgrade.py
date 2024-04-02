import requests
import settings

def upgrade_packages(url, port, packages):

    try:
        endpoint = f"{url}:{port}/packages/upgrade"

        data = {'packages': packages} if packages else {}

        response = requests.post(endpoint, json=data)

        if response.status_code == 200:
            result = response.json()
            success_message = result.get('success', '')

            if success_message:
                return success_message
            else:
                upgrade_output = result.get('output', '')
                return f"Upgrade output:\n{upgrade_output}"
        else:
            return "Failed to upgrade packages"  
    except Exception as e:
        return f'Error: {e}'  
