import requests

def update_packages(url, port):
    try:
        endpoint = f"{url}:{port}/packages/update"

        
        response = requests.post(endpoint)

        
        if response.status_code == 200:
            result = response.json()
            update_output = result.get('update_result', {}).get('output', '')
            show_upgradable_output = result.get('show_upgradable_result', {}).get('output', '')
            
            
            formatted_output = f"Update result:\n{update_output}\n\nShow upgradable result:\n{show_upgradable_output}"
            return formatted_output
        else:
            return "Failed to update packages" 
    except Exception as e:
        return f'Error: {e}'  
