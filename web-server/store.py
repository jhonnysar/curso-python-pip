import requests

def get_Categories():
    r=requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    categories= r.json()
    for categori in categories:
        print(categori['name'])