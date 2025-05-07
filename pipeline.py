from extract import fetch_stock_history
from load import load_to_postgres

SYMBOLS = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"]

def run_pipeline():
    for symbol in SYMBOLS:
        data_list = fetch_stock_history(symbol)
        load_to_postgres(data_list)
        print(f"✅ Loaded {len(data_list)} records for {symbol}")

if __name__ == "__main__":
    run_pipeline()
