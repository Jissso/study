import requests

def fetch_data(url):
    try:
        headers = {
            'Content-Type': 'application/json',
            'Set-Cookie': 'ak_bmsc=F4A3A3B13C36728F9DCE2F91790A63F5~000000000000000000000000000000~YAAQUxXai3KBHfCPAQAAuq+59RjgdYbBOqOVCgFCDGpmjNMAyCt9lIPKFk8omGsqdCy0qv/DrGA/EbouZQhFl5Qii5ATCVAeAsHI08ppdpCwU11u+e2ibCAjPsZVtiWWQjL0fKA5sKE8JlmD1Nj/IaM6wZPS84hZklrjlsCNA4kTbaINhgLcWxzoXRw5NIN7kNdQyuU2pIHZeORccR1p0uMHqWSSDWBS/OszGGOFA+U9USDYATWFPcp8li9ZGmWfh6tCQM6us7kF3b47grE+LSQHRm7xxwH3rgLPsMjXZpvuT7Gk87Yt/6MX7ViukaBIimS89VTZHE5/nbgIa2rIeefZt6t/ELs7yiMji0UjQ+4MeHwA7QamLuDd8D5anNn7w+bjzaP89ll5kQ==; Domain=.afl.com.au; Path=/; Expires=Sat, 08 Jun 2024 04:42:18 GMT; Max-Age=7200; HttpOnly',
            'X-Media-Mis-Token': '43242eda8c2fdd6d153c6929193fa5f9'
        }

        # Send a GET request to the URL
        response = requests.get(url, headers=headers)
        
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        
        # Return the response content
        return response.text
    
    except requests.exceptions.RequestException as e:
        # Print any error messages to stderr
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":

    fixed_variable = "014"

    # Loop through rounds 1 to 13
    for year in range(2023, 2024):
        year_str = f"{year:02}"  # Format the round number as a two-digit string

        for round_num in range(1, 30):
            round_str = f"{round_num:02}"  # Format the round number as a two-digit string
            
            for match in range(1, 10):
                match_str = f"{match:02}"  # Format the round number as a two-digit string

                # Construct the URL
                url = f"https://api.afl.com.au/cfs/afl/playerStats/match/CD_M{year_str}{fixed_variable}{round_str}{match_str}"
                data = fetch_data(url)
                
                if data:
                    print(f"Data for round {round_str}:")
                    print(data)
                    print("\n" + "="*80 + "\n")