import requests

API_KEY = "6656545dd7d1bc32cbe4119c18d164ba"
STOCK_SYMBOLS = ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN"]

def fetch_stock_history(symbol):
    url = (
        f"https://www.alphavantage.co/query"
        f"?function=TIME_SERIES_DAILY"
        f"&symbol={symbol}"
        f"&apikey={API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    try:
        time_series = data["Time Series (Daily)"]
        all_data = []

        for date, prices in time_series.items():
            row = {
                "symbol": symbol,
                "date": date,
                "open": float(prices["1. open"]),
                "high": float(prices["2. high"]),
                "low": float(prices["3. low"]),
                "close": float(prices["4. close"]),
                "volume": int(prices["5. volume"])
            }
            all_data.append(row)

        return all_data

    except Exception as e:
        print(f"❌ Failed to fetch data for {symbol}: {e}")
        return []
