import json
import os
from datetime import datetime

def get_deals():
    return [
        {
            "title": "New York to Orlando $69 One-Way",
            "price": "69",
            "link": "https://economybookings.tpx.gr/WhPRsumA",
            "desc": "Great limited time deal. Book fast!",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        {
            "title": "Los Angeles to Las Vegas $49",
            "price": "49",
            "link": "https://economybookings.tpx.gr/WhPRsumA",
            "desc": "Perfect weekend getaway deal.",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        {
            "title": "Chicago to Miami $89",
            "price": "89",
            "link": "https://economybookings.tpx.gr/WhPRsumA",
            "desc": "Excellent one-way fare available now.",
            "date": datetime.now().strftime("%Y-%m-%d")
        }
    ]

def save_deals():
    os.makedirs('data', exist_ok=True)
    deals = get_deals()
    with open('data/deals.json', 'w') as f:
        json.dump(deals, f, indent=2)
    print(f"✅ Updated {len(deals)} deals at {datetime.now()}")

if __name__ == "__main__":
    save_deals()
