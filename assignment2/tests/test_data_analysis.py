import pytest
from assignment2.src.data_analysis import (
    total_sales,
    sales_by_region,
    sales_by_category,
    top_selling_product,
    profit_by_region,
    daily_sales,
)


@pytest.fixture
def sample_data():
    """
    Small synthetic dataset based on the Superstore structure.
    To make the tests predictable and easy to validate.
    """
    return [
        {
            "Order Date": "01/01/2025",
            "Region": "West",
            "Category": "Furniture",
            "Product Name": "Chair",
            "Sales": "100.00",
            "Quantity": "2",
            "Profit": "20.00",
        },
        {
            "Order Date": "01/01/2025",
            "Region": "West",
            "Category": "Technology",
            "Product Name": "Laptop",
            "Sales": "900.00",
            "Quantity": "1",
            "Profit": "150.00",
        },
        {
            "Order Date": "01/02/2025",
            "Region": "East",
            "Category": "Furniture",
            "Product Name": "Table",
            "Sales": "300.00",
            "Quantity": "3",
            "Profit": "50.00",
        },
        {
            "Order Date": "01/02/2025",
            "Region": "East",
            "Category": "Furniture",
            "Product Name": "Chair",
            "Sales": "200.00",
            "Quantity": "4",
            "Profit": "40.00",
        },
    ]

def test_total_sales(sample_data):
    assert total_sales(sample_data) == 100.00 + 900.00 + 300.00 + 200.00

def test_sales_by_region(sample_data):
    result = sales_by_region(sample_data)
    assert result["West"] == 100.00 + 900.00
    assert result["East"] == 300.00 + 200.00

def test_sales_by_category(sample_data):
    result = sales_by_category(sample_data)
    assert result["Furniture"] == 100.00 + 300.00 + 200.00
    assert result["Technology"] == 900.00

def test_top_selling_product(sample_data):
    # Chair has quantity 2 + 4 = 6 (highest)
    assert top_selling_product(sample_data) == "Chair"

def test_profit_by_region(sample_data):
    result = profit_by_region(sample_data)
    assert result["West"] == 20.00 + 150.00
    assert result["East"] == 50.00 + 40.00

def test_daily_sales(sample_data):
    result = daily_sales(sample_data)
    assert result["01/01/2025"] == 100.00 + 900.00
    assert result["01/02/2025"] == 300.00 + 200.00

def test_total_sales_handles_missing_sales_field():
    data = [{"Sales": "100"}, {"Sales": ""}]  # missing value
    with pytest.raises(ValueError):
        total_sales(data)