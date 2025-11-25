import pandas as pd

# -------------------------------
# STEP 1: Load both CSV datasets
# -------------------------------
trader_data = pd.read_csv("historical_data.csv")
fgi_data = pd.read_csv("fear_greed_index.csv")

print("=== Trader Data Sample ===")
print(trader_data.head())

print("\n=== Fear & Greed Index Sample ===")
print(fgi_data.head())

# -------------------------------
# STEP 2: Convert timestamps to dates
# -------------------------------
# Your trader file timestamp column = "Timestamp"  (but it's too large)
# So we detect automatically:

def convert_timestamp(ts):
    ts = float(ts)
    # If timestamp is too large → it's in milliseconds
    if ts > 10**12:
        return pd.to_datetime(ts, unit="ms").date()
    # otherwise seconds
    return pd.to_datetime(ts, unit="s").date()

trader_data["date"] = trader_data["Timestamp"].apply(convert_timestamp)
fgi_data["date"] = pd.to_datetime(fgi_data["timestamp"], unit="s").dt.date

# -------------------------------
# STEP 3: Merge datasets on date
# -------------------------------
merged = pd.merge(trader_data, fgi_data, on="date", how="left")

# -------------------------------
# STEP 4: Trader sentiment logic
# -------------------------------
def analyze_trade(row):
    try:
        amount = float(row["Size USD"])
    except:
        amount = 0

    side = str(row["Side"]).upper()

    if side == "BUY" and amount > 100000:
        return "Bullish"
    elif side == "SELL" and amount > 100000:
        return "Bearish"
    else:
        return "Neutral"

merged["trader_sentiment"] = merged.apply(analyze_trade, axis=1)

# -------------------------------
# STEP 5: Combine sentiment with FGI
# -------------------------------
def final_sentiment(row):
    fgi = row["classification"]
    ts = row["trader_sentiment"]

    if ts == "Bullish" and fgi in ["Fear", "Extreme Fear"]:
        return "Contrarian Opportunity (Bullish)"

    elif ts == "Bearish" and fgi in ["Greed", "Extreme Greed"]:
        return "Contrarian Opportunity (Bearish)"

    elif ts == "Bullish":
        return "Market Bullish Bias"

    elif ts == "Bearish":
        return "Market Bearish Bias"

    else:
        return "Neutral Market"

merged["final_sentiment"] = merged.apply(final_sentiment, axis=1)

# -------------------------------
# STEP 6: Print results
# -------------------------------
print("\n=== Final Combined Sentiment ===")
print(
    merged[
        ["date", "Side", "Size USD", "trader_sentiment", "classification", "final_sentiment"]
    ].head(20)
)

# -------------------------------
# STEP 7: Save output
# -------------------------------
merged.to_csv("final_sentiment_output.csv", index=False)
print("\nSaved: final_sentiment_output.csv")
