
def calculate_metrics(df):
    position = None
    entry_price = 0
    total_profit = 0
    trades = 0
    for index, row in df.iterrows():
        if row["signal"] == "BUY" and position is None:
            entry_price = row["close"]
            position = "LONG"
        elif row["signal"] == "SELL" and position == "LONG":
            profit = row["close"] - entry_price
            total_profit += profit
            trades += 1
            position = None
    return {"total_profit": total_profit, "trades": trades}
