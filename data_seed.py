import pandas as pd

def seed_portfolio():
    return pd.DataFrame([
        ["BIG","Hercules Metals",9.1,40],
        ["KDK","Kodiak Copper",9.0,35],
        ["AHR","Amarc Resources",8.9,35],
        ["STND","Standard Uranium",8.7,30],
    ], columns=["Ticker","Company","Score","Upside (x)"])
