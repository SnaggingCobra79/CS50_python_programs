import requests
import sys

try:
    responce = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=877ae6295438ac974741ed9c30b46b039e3f63758f1f6d003dc42c9b2733d101")
    content = responce.json()
    price_usd = float(content["data"]["priceUsd"])
    if len(sys.argv) != 2:
        sys.exit("Invalid Argument")
    try:
        amt = float(sys.argv[1])
    except ValueError:
        sys.exit("Invlaid Number of bitcoin")
    user = price_usd * amt
    print(f"${user:,.4f}")

except (requests.RequestException,requests.HTTPError):
    sys.exit("Cannot get the price")
