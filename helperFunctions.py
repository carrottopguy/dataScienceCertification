import requests

def download_file(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f'file download successfully to {filename}')
    except requests.exceptions.RequestException as e:
        print(f'error downloading file: {e}')