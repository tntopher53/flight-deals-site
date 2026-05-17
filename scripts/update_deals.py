import json
import os
from datetime import datetime

def get_deals():
    return [
        {
            "title": "New York to Orlando $69 One-Way",
            "price": "69",
            "link": "https://www.travelpayouts.com/your-link-here",
            "desc": "Great deal! Limited seats from NYC to Orlando.",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        {
            "title": "Los Angeles to Las Vegas $49",
            "price": "49",
            "link": "https://www.travelpayouts.com/your-link-here",
            "desc": "Super cheap weekend getaway to Las Vegas.",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        {
            "title": "Chicago to Miami $89",
            "price": "89",
            "link": "https://www.travelpayouts.com/your-link-here",
            "desc": "Excellent one-way fare.",
            "date": datetime.now().strftime("%Y-%m-%d")
        }
    ]

def save_deals():
    os.makedirs('data', exist_ok=True)
    deals = get_deals()
    with open('data/deals.json', 'w') as f:
        json.dump(deals, f, indent=2)
    print(f"✅ Saved {len(deals)} deals")

if __name__ == "__main__":
    save_deals()
