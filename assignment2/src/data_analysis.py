import csv
from functools import reduce
from typing import List, Dict, Any
from collections import defaultdict

def load_csv(path:str) -> List[Dict]:
    """
    Loads the Superstore CSV and returns a list of row dictionaries.
    Assumes headers match standard Superstore column names.
    """
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        data = list(reader)
    return data

def total_sales(data: List[Dict[str, Any]]) -> float:
    """
    Total 'Sales' across the dataset
    using map + reduce
    """
    sales_values = map(lambda row: float(row["Sales"]), data)
    return reduce(lambda a,b: a + b, sales_values, 0.0)

def sales_by_region(data: List[Dict]) -> Dict[str, float]:
    """
    Group by Region and sum Sales.
    """
    result = defaultdict(float)
    for row in data:
        region = row["Region"]
        sale = float(row["Sales"])
        result[region] += sale
    return dict(result)

def sales_by_category(data: List[Dict]) -> Dict[str, float]:
    """
    Group by Category and sum Sales.
    """
    result = defaultdict(float)
    for row in data:
        cat = row["Category"]
        sale = float(row["Sales"])
        result[cat] += sale
    return dict(result)
    
def top_selling_product(data: List[Dict]) -> str:
    """
    Product with highest total Quantity sold.
    Using map + reduce.
    """
    # aggregate quantities by product
    qmap = defaultdict(int)
    for row in data:
        qmap[row["Product Name"]] += int(float(row["Quantity"]))

    # find max by quantity
    return max(qmap.items(), key=lambda x: x[1])[0]

def profit_by_region(data: List[Dict]) -> Dict[str, float]:
    """
    Group by region and sum Profit.
    """
    result = defaultdict(float)
    for row in data:
        region = row["Region"]
        profit = float(row["Profit"])
        result[region] += profit
    return dict(result)
    
def daily_sales(data: List[Dict[str, Any]]) -> Dict[str, float]:
    """
    Group total Sales by Order Date.
    Order Date format: MM/DD/YYYY or similar.
    """
    result = defaultdict(float)
    for row in data:
        day = row["Order Date"]
        sale = float(row["Sales"])
        result[day] += sale
    return dict(result)

    
def run_all_analysis(path: str):
    """
    Loads dataset and prints all analysis results.
    This is the required 'print outputs to console'.
    """
    data = load_csv(path)

    print("\n=== Superstore Sales Analysis ===\n")

    print(f"Total Sales: {total_sales(data):,.2f}\n")

    print("Sales by Region:")
    for region, value in sales_by_region(data).items():
        print(f"  {region}: {value:,.2f}")

    print("\nSales by Category:")
    for cat, value in sales_by_category(data).items():
        print(f"  {cat}: {value:,.2f}")

    print(f"\nTop Selling Product (by Quantity): {top_selling_product(data)}")

    print("\nProfit by Region:")
    for region, value in profit_by_region(data).items():
        print(f"  {region}: {value:,.2f}")

    print("\nDaily Sales:")
    for day, value in list(daily_sales(data).items())[:10]:  # preview first 10
        print(f"  {day}: {value:,.2f}")

    print("\n=== End of Analysis ===\n")