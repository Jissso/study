import requests
import json
import pandas as pd

url = "https://api.afl.com.au/cfs/afl/playerStats/match/CD_M20240141001"

headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'if-none-match': 'W/"67b31d531149f3aac9c5251d1f2bb840"',
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
  'Cookie': 'ak_bmsc=AACE4CED39F1D57B0414057E5D7CCA54~000000000000000000000000000000~YAAQPINHaMlBuISPAQAAd3j6iRcN0iCMympbDBKvWY6Yzb3+k8v9x3Ir1jCWMX7U1QPj+tCaamd7O0DD9/mf7US4S9jwID319uQJepXDbKlVxAsDTCltnMT11Tsjdxr3HyTC+h0T/plCAxEhtnM1sKw868X7tsn0/D+b6gZbH2G3pdLjaqDtj01zqfMtXSJ17sEeG7Q82U1teONTjjsZpiFVeLaYwjT1vSSZ7oo0ey8q/6FEwqJQvICfpFFC1/2ymQ1PqfZPcAlJDJsVsLdFmgtFdjL7RfxgMOaid98W2tPrDcOqX3hybSF3wTtkmxjz6mv7VrwUjbd8O+5uOObaITU8BLtnJz6PebqzFUZHVGxm7Ldc5C5VKgRQ; bm_sv=A1F2847F92DCC54437B01F777BE114B6~YAAQPINHaClHuISPAQAAurD6iRcB3jNEgcHI3GoZ0okQZ76HC0mXFSBa7xvX5iW3YtuZJvOC+e2AuusgRSZhTVe/VmtgccVrR1X/ZwX4D7v/AAI6mKlYIqCtcxSdoGBawU/948z3eNqvgQU2f0AhDNC0QY/1EUpfvKb4mvz9z5UGp3NCprdM8R/ua2ZZgmxzCq4P8GNKZE5NpPHTW8Y4/QUngLVGqllKsJH2FcGf1pxy9LUmptAQ31RsbxUanc9l~1'
}

r = requests.get(url, headers=headers)

playerstats = r.json()

df = pd.json_normalize(playerstats)

df.columns

df = pd.json_normalize(playerstats['homeTeamPlayerStats'])

non_extendStats_col = [col for col in df.columns if not 'extendedStats' in col]
playerStat_col = [col for col in df.columns if 'playerStats' in col]
df = df[playerStat_col]
df.columns