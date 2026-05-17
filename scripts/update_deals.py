import json
import os
from datetime import datetime

# Sample deals - later we will pull from RSS or manual sources
def generate_sample_deals():
    return [
        {
            "title": "New York to Orlando $69 One-Way",
            "price": "69",
            "link": "https://www.travelpayouts.com/your-link-here",
            "desc": "Great deal! Limited seats available. Book fast.",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        {
            "title": "Los Angeles to Las Vegas $49",
            "price": "49",
            "link": "https://www.travelpayouts.com/your-link-here",
            "desc": "Super cheap weekend getaway.",
            "date": datetime.now().strftime("%Y-%m-%d")
        },
        {
            "title": "Chicago to Miami $89",
            "price": "89",
            "link": "https://www.travelpayouts.com/your-link-here",
            "desc": "Excellent one-way fare from Chicago.",
            "date": datetime.now().strftime("%Y-%m-%d")
        }
    ]

def save_deals():
    os.makedirs('data', exist_ok=True)
    deals = generate_sample_deals()
    
    with open('data/deals.json', 'w') as f:
        json.dump(deals, f, indent=2)
    
    print(f"✅ Updated deals.json with {len(deals)} deals at {datetime.now()}")

if __name__ == "__main__":
    save_deals()
