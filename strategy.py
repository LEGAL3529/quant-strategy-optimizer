
import pandas as pd

def apply_strategy(df, ema_period):
    df["ema"] = df["close"].ewm(span=ema_period, adjust=False).mean()
    df["signal"] = "HOLD"
    df.loc[df["close"] > df["ema"], "signal"] = "BUY"
    df.loc[df["close"] < df["ema"], "signal"] = "SELL"
    return df
