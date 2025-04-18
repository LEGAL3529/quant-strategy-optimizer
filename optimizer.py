
import pandas as pd
from strategy import apply_strategy
from metrics import calculate_metrics

def optimize_strategy(data_path, param_range):
    best_result = {"params": None, "profit": -float("inf")}
    for ema_period in param_range:
        df = pd.read_csv(data_path, parse_dates=["timestamp"])
        df["ema_period"] = ema_period
        df = apply_strategy(df, ema_period)
        result = calculate_metrics(df)
        if result["total_profit"] > best_result["profit"]:
            best_result["params"] = ema_period
            best_result["profit"] = result["total_profit"]
    return best_result

if __name__ == "__main__":
    best = optimize_strategy("data/sample_data.csv", range(5, 30))
    print("✅ Best EMA Period:", best["params"])
    print("💰 Max Profit:", best["profit"])
