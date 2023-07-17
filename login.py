import requests

url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/"

user = input('[+] Enter Username :')
pasw = input('[+] Enter Password :')

head = { 
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language":
    "ar, en-US q = 0.9, en q = 0.8",
    "Content-Length":
    "303",
    "Content-Type":
    "application/x-www-form-urlencoded"
    "Cookies": "ig_nrcb = 1",
    "mid" = "Y7nuYAAEAAGyScgJVI0ggtRQpGNg",
    "ig_did" = "9A32D1B1-D4AF-47A1-9B50-914706FE6526",
    "csrftoken" = "TFU4rwkgJxX6AftKUC9NAHWZHyPineSp",
    "datr" = "PmUUZCKHPQoUcg32i12f0J6d",
    "dpr" = "2",
    "Origin":
    "https: // www.instagram.com",
    "Referer":
    "https: // www.instagram.com /",
    "Sec-Ch-Prefers-Color-Scheme":
    "light",
    "Sec-Ch-Ua":
    "Not.A/Brand",
    "v" = "8", "Chromium",
    "v" = "114", "Google Chrome",
    "v" = "114",
    "Sec-Ch-Ua-Full-Version-List":
    "Not.A/Brand",
    "v" = "8.0.0.0", "Chromium",
    "v" = "114.0.5735.198", "Google Chrome",
    "v" = "114.0.5735.198",
    "Sec-Ch-Ua-Mobile":
    "?1",
    "Sec-Ch-Ua-Platform":
    "Android",
    "Sec-Ch-Ua-Platform-Version":
    "6.0",
    "Sec-Fetch-Dest":
    "empty",
    "Sec-Fetch-Mode":
    "cors",
    "Sec-Fetch-Site":
    "same-origin",
    "Viewport-Width":
    "1226",
    "X-Asbd-Id":
    "129477",
    "X-Csrftoken":
    "TFU4rwkgJxX6AftKUC9NAHWZHyPineSp",
    "X-Ig-App-Id":
    "936619743392459",
    "X-Ig-Www-Claim":
    "0",
    "X-Instagram-Ajax":
    "1007846744",
    "X-Requested-With":
    "XMLHttpRequest",
}

data = {
    'username': '',
    'enc_password':  f'# PWD_INSTAGRAM_BROWSER:10:: {head}',
    'optIntoOneTap': 'false',
    'queryParams': '{}',
    'trustedDeviceRecords': '{}'

}

login = requests.post(url, headers=head, data=data).status_code 

print(login)