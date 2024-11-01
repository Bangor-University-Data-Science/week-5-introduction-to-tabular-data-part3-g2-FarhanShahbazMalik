import pandas as pd
# 1. Import Data Function
def import_data(filename: str) -> pd.DataFrame:
    """Imports data from an Excel or CSV file into a DataFrame."""
    if filename.endswith('.xlsx'):
        return pd.read_excel(filename)
    elif filename.endswith('.csv'):
        return pd.read_csv(filename)
    else:
        raise ValueError("File format not supported. Use .xlsx or .csv")

# 2. Filter Data Function
def filter_data(df: pd.DataFrame) -> pd.DataFrame:
    """Filters data by removing rows with missing CustomerID and negative Quantity or UnitPrice values."""
    df = df.dropna(subset=['CustomerID'])
    df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
    return df

# 3. Loyalty Customers Function
def loyalty_customers(df: pd.DataFrame, min_purchases: int) -> pd.DataFrame:
    """Identifies loyal customers based on a minimum purchase threshold."""
    customer_counts = df.groupby('CustomerID').size().reset_index(name='purchase_count')
    loyal_customers = customer_counts[customer_counts['purchase_count'] >= min_purchases]
    return loyal_customers

# 4. Quarterly Revenue Function
def quarterly_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Calculates total revenue per quarter."""
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['quarter'] = df['InvoiceDate'].dt.to_period('Q')
    df['revenue'] = df['Quantity'] * df['UnitPrice']
    quarterly_revenue = df.groupby('quarter')['revenue'].sum().reset_index(name='total_revenue')
    return quarterly_revenue

# 5. High Demand Products Function
def high_demand_products(df: pd.DataFrame, top_n: int) -> pd.DataFrame:
    """Identifies the top N products with the highest total quantity sold."""
    product_demand = df.groupby('StockCode')['Quantity'].sum().reset_index(name='total_quantity')
    high_demand = product_demand.sort_values(by='total_quantity', ascending=False).head(top_n)
    return high_demand

# 6. Purchase Patterns Function
def purchase_patterns(df: pd.DataFrame) -> pd.DataFrame:
    """Creates a summary showing the average quantity and average unit price for each product."""
    patterns = df.groupby('StockCode').agg(
        avg_quantity=('Quantity', 'mean'),
        avg_unit_price=('UnitPrice', 'mean')
    ).reset_index()
    return patterns

# 7. Answer Conceptual Questions Function
def answer_conceptual_questions() -> dict:
    """Provides answers to the conceptual questions in a dictionary format."""
    answers = {
        "Q1": {"A"},
        "Q2": {"B"},
        "Q3": {"A", "C"},
        "Q4": {"A", "B"},
        "Q5": {"A"}
    }
    return answers

