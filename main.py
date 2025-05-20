import requests #pip install requests

query = input("Enter what you want to search today: ") 
api = "ad1954015f1d4bc4aa397bd623050161" #newsapi.org
url = f"https://newsapi.org/v2/everything?q={query}&from=2025-04-18&sortBy=publishedAt&apiKey={api}" 

print(url)

r = requests.get(url)
data = r.json()
articles = data["articles"]

for index, article in enumerate(articles):
    print(index+1, article["title"], article["url"])
    print("\n*************************************\n")