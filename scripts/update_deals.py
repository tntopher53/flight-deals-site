import feedparser
import json
import os
from datetime import datetime

# Good public RSS feeds for flight deals (add more later)
RSS_FEEDS = [
    "https://theflightdeal.com/feed/",
    "https://www.fly4free.com/feed/",
    # "https://secretflying.com/feed/"  # You can add more
]

def load_existing_deals():
    if os.path.exists('data/deals.json'):
        with open('data/deals.json', 'r') as f:
            return json.load(f)
    return []

def save_deals(deals):
    os.makedirs('data', exist_ok=True)
    with open('data/deals.json', 'w') as f:
        json.dump(deals[:30], f, indent=2)   # Keep only latest 30
    print(f"✅ Saved {len(deals)} deals at {datetime.now()}")

def fetch_deals():
    existing = load_existing_deals()
    new_deals = []
    
    for url in RSS_FEEDS:
        print(f"Fetching from: {url}")
        feed = feedparser.parse(url)
        
        for entry in feed.entries[:8]:   # Limit per source
            deal = {
                "title": entry.title[:100],
                "price": "N/A",   # We extract later if needed
                "link": entry.link,
                "desc": entry.get("summary", "")[:200] or entry.get("description", "")[:200],
                "date": datetime.now().strftime("%Y-%m-%d"),
                "source": url
            }
            # Avoid duplicates
            if not any(d['link'] == deal['link'] for d in existing + new_deals):
                new_deals.append(deal)
    
    # Combine and save
    all_deals = new_deals + existing
    save_deals(all_deals)

if __name__ == "__main__":
    fetch_deals()

if __name__ == "__main__":
    save_deals()
