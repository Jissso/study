import requests

url = "https://api.afl.com.au/cfs/afl/matchItem/CD_M20240141007"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'if-none-match': 'W/"8a4fed526522c94a965f31ea42b5249d"',
  'origin': 'https://www.afl.com.au',
  'priority': 'u=1, i',
  'referer': 'https://www.afl.com.au/',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
  'x-media-mis-token': '02e19b55b073f50c011307ec21b7e4ff',
  'Cookie': 'ak_bmsc=4CEB1E7B9B1541568C91EE77E634ED25~000000000000000000000000000000~YAAQ8u/AF3WY7ICPAQAA6URckBfbL2lZQtflPbnwDi/rkgfCew4q3Frf8cGlKubzPE/yci0vJig4D7fzepYdo6iJ5DPsKy8AZqYpZq3IO7clsaBE047CsgKpYtpTK4yfa3mEnzBMMssEHWIal1CgAniWkWeeqydzBLSTIaO5nDGg3ezCcKaJr988xB/b+VbYSCH9ZwmLG6WCQGDm98d6ebBSoidtXD/TrDLWbvo1HfUsfHXsJRoU5o7di+rtBijS/MhG2d6DhiTqqiACoj5ayP3W7yXreBi6hqgu2JRZz7SuXxVteJzERZZld3ioJKIHcbT+FO+j/bxYj/MsRnskKPs1zRb0Y6Wdq94VYZJYAIC7Rda7nhof/4+9'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
