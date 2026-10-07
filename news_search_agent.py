# News Search Agent with Loop

import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("NEWS_API_KEY")

print("Welcome to News Search Agent")
print("Type exit to stop")

while True:
    topic = input("\nEnter news topic: ")

    if topic.lower() == "exit":
        print("Thank you for using News Search Agent.")
        break

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"

    response = requests.get(url)
    data = response.json()

    if data["status"] == "ok":
        articles = data["articles"]

        if len(articles) == 0:
            print("No news found.")
        else:
            print("\nTop 5 News:\n")

            for article in articles[:5]:
                print("Title:", article["title"])
                print("Source:", article["source"]["name"])
                print("Published:", article["publishedAt"])
                print("Link:", article["url"])
                print("-" * 50)

    else:
        print("Error:", data["message"])
