import psycopg2

def load_to_postgres(data_list):
    if not data_list:
        return

    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="abdul756",
        host="localhost",  # or remote IP
        port="5432"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS stock_history (
            symbol TEXT,
            date DATE,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            volume BIGINT,
            PRIMARY KEY (symbol, date)
        )
    """)

    for data in data_list:
        cur.execute("""
            INSERT INTO stock_history (symbol, date, open, high, low, close, volume)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (symbol, date) DO NOTHING
        """, (
            data["symbol"],
            data["date"],
            data["open"],
            data["high"],
            data["low"],
            data["close"],
            data["volume"]
        ))

    conn.commit()
    cur.close()
    conn.close()
