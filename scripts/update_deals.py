import json
import os
from datetime import datetime

# Fallback deals in case RSS fails
def get_fallback_deals():
    return [
        {
            "title": "New York to Orlando $69 One-Way",
            "price": "69",
            "link": "https://www.travelpayouts.com/your-link-here",
            "desc": "Great limited time deal from NYC.",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        {
            "title": "Los Angeles to Las Vegas $49",
            "price": "49",
            "link": "https://www.travelpayouts.com/your-link-here",
            "desc": "Super cheap weekend getaway.",
            "date": datetime.now().strftime("%Y-%m-%d")
        }
    ]

def save_deals(deals):
    os.makedirs('data', exist_ok=True)
    with open('data/deals.json', 'w') as f:
        json.dump(deals, f, indent=2)
    print(f"✅ Saved {len(deals)} deals")

if __name__ == "__main__":
    print("Starting deal update...")
    deals = get_fallback_deals()
    save_deals(deals)
    print("✅ Update completed successfully")
