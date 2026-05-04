import requests
import json

API_KEY = 'API_KEY'

def get_news():
    global articles
    topic = input("What news would you like to see? ")
    
    url = f'https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}'
    
    response = requests.get(url)
    data = response.json()
    
    articles = data.get('articles', [])
    
    print(f"\n--- Top 5 news about {topic} ---\n")

def main():
    while True:
        get_news()
        for article in articles[:5]:
            print(f"- {article['title']}")
            print(f"  Source: {article['source']['name']}")
            print(f"  Published at: {article['publishedAt']}\n")
            print("-" * 30,"\n")
        b = input("Would you like to see more news? (yes/no)").strip().lower()    
        if b != 'yes':
            break

if __name__ == "__main__":
    main()
