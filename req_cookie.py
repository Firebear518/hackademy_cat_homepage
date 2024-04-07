'''
Title: req_cookie.py
Author: Jaeho Jeon 2024-01-25
'''
import requests

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

request_checker(url='http://localhost:3000/page-babo.php', random_4char='6GcT')