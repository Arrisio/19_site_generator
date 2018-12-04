
def test_method():
    import requests

    r = requests.get('https://stackoverflow.com/')

    with open('tmp.txt', 'wb') as file:
        file.write(r.content)


test_method()
