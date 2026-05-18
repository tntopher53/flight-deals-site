import feedparser
import json
import os
from datetime import datetime

# Real legitimate flight deal RSS feeds
RSS_FEEDS = [
    "https://www.theflightdeal.com/feed/",           # The Flight Deal (very good)
    "https://www.fly4free.com/feed/",                # Fly4free
    # Add more later if you want
]

def load_existing_deals():
    if os.path.exists('data/deals.json'):
        try:
            with open('data/deals.json', 'r') as f:
                return json.load(f)
        except:
            return []
    return []

def save_deals(deals):
    os.makedirs('data', exist_ok=True)
    # Keep only the 20 most recent deals
    with open('data/deals.json', 'w') as f:
        json.dump(deals[:20], f, indent=2)
    print(f"✅ Saved {len(deals[:20])} real deals at {datetime.now()}")

def fetch_real_deals():
    existing = load_existing_deals()
    new_deals = []
    
    for url in RSS_FEEDS:
        print(f"Fetching from: {url}")
        try:
            feed = feedparser.parse(url)
            
            for entry in feed.entries[:10]:  # Limit per source
                title = entry.title[:120]
                
                deal = {
                    "title": title,
                    "price": "Check Price",   # Hard to auto-extract price reliably
                    "link": entry.link,
                    "desc": entry.get("summary", "")[:250] or "Great flight deal found!",
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "source": url.split('/')[2]
                }
                
                # Avoid duplicates
                if not any(d.get('link') == deal['link'] for d in existing + new_deals):
                    new_deals.append(deal)
        except Exception as e:
            print(f"Error fetching {url}: {e}")
    
    # Combine new + old deals
    all_deals = new_deals + existing
    save_deals(all_deals)

if __name__ == "__main__":
    print("Starting real flight deals update...")
    fetch_real_deals()
