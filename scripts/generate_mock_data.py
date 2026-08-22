import os
import random
from datetime import datetime, timedelta
import pandas as pd

# Define realistic synthetic categories and vendors
SYNTHETIC_VENDORS = {
    "Groceries": ["Grocery Store #104", "Local Supermarket", "Organic Market"],
    "Dining": ["Corner Cafe", "Downtown Bistro", "Taco Stand", "Burger Joint"],
    "Transport": ["Metro Transit", "City Ride", "Fuel Station #42"],
    "Utilities": ["Electric Co", "City Water Dept", "Internet Provider"],
    "Entertainment": ["Cinemaplex", "Streaming Service", "Bookstore"],
    "Shopping": ["Department Store", "Tech Outlet", "Apparel Shop"]
}

def generate_synthetic_transactions(num_records: int = 100) -> pd.DataFrame:
    records = []
    end_date = datetime.now()
    start_date = end_date - timedelta(days=90)

    for i in range(num_records):
        # Pick a random category and vendor
        category = random.choice(list(SYNTHETIC_VENDORS.keys()))
        vendor = random.choice(SYNTHETIC_VENDORS[category])
        
        # Generate random date in the last 90 days
        random_days = random.randint(0, 90)
        txn_date = (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")
        
        # Generate realistic amount based on category
        if category == "Groceries":
            amount = round(random.uniform(25.0, 180.0), 2)
        elif category == "Dining":
            amount = round(random.uniform(8.0, 65.0), 2)
        elif category == "Utilities":
            amount = round(random.uniform(45.0, 150.0), 2)
        else:
            amount = round(random.uniform(10.0, 120.0), 2)

        records.append({
            "transaction_id": f"TXN-{1000 + i}",
            "date": txn_date,
            "vendor": vendor,
            "amount": amount,
            "suggested_category": category,
            "account_type": random.choice(["Checking", "Credit Card"])
        })

    df = pd.DataFrame(records)
    return df.sort_values(by="date", ascending=False)

if __name__ == "__main__":
    df = generate_synthetic_transactions(150)
    
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    output_path = "data/synthetic_transactions.csv"
    
    df.to_csv(output_path, index=False)
    print(f"Generated {len(df)} synthetic transactions at '{output_path}'")