import requests

coin = input("Enter cryptocurrency (bitcoin, ethereum, dogecoin): ").lower()

url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin}&vs_currencies=usd,inr"

response = requests.get(url)
data = response.json()

if coin in data:
    print("\nCryptocurrency Price")
    print("--------------------")
    print("Name:", coin.title())
    print("Price (USD): $", data[coin]["usd"])
    print("Price (INR): ₹", data[coin]["inr"])
else:
    print("Cryptocurrency not found!")
