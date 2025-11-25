# insights.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Step 0: Load CSV
# -------------------------------
df = pd.read_csv("final_sentiment_output.csv")
print("Data Loaded Successfully!\n")
print(df.head())      # Top 5 rows
print(df.columns)     # Column names

# -------------------------------
# Step 1: Trader Sentiment Distribution
# -------------------------------
print("\n--- Trader Sentiment Distribution ---")
sentiment_counts = df['trader_sentiment'].value_counts()
print(sentiment_counts)

plt.figure(figsize=(6,4))
sns.countplot(x='trader_sentiment', data=df)
plt.xticks(rotation=45)
plt.title("Trader Sentiment Distribution")
plt.xlabel("Trader Sentiment")
plt.ylabel("Number of Trades")
plt.savefig("Trader_Sentiment_Distribution.png")
plt.show() 

# -------------------------------
# Step 2: Coin-wise Closed PnL Summary
# -------------------------------
print("\n--- Coin-wise Closed PnL Summary ---")
coin_summary = df.groupby('Coin')['Closed PnL'].agg(['mean','sum','count'])
print(coin_summary)

# Save to CSV
coin_summary.to_csv("Coinwise_Closed_PnL_Summary.csv")

# Coin-wise boxplot
plt.figure(figsize=(6,4))
sns.boxplot(x='Coin', y='Closed PnL', data=df)
plt.xticks(rotation=90)
plt.title("Closed PnL Distribution by Coin")
plt.xlabel("Coin")
plt.ylabel("Closed PnL")
plt.savefig("Coinwise_Closed_PnL_Boxplot.png")  # save plot
plt.show()

# -------------------------------
# Step 3: Sentiment-wise Closed PnL Summary
# -------------------------------

if 'trader_sentiment' in df.columns and 'Closed PnL' in df.columns:
    print("\n--- Closed PnL vs Trader Sentiment ---")
    sentiment_pnl_summary = df.groupby('trader_sentiment')['Closed PnL'].agg(['mean','sum','count'])
    print(sentiment_pnl_summary)
    
    # Save summary
    sentiment_pnl_summary.to_csv("Sentimentwise_Closed_PnL_Summary.csv")
    
    # Sentiment-wise boxplot
    plt.figure(figsize=(6,4))
    sns.boxplot(x='trader_sentiment', y='Closed PnL', data=df)
    plt.xticks(rotation=45)
    plt.title("Closed PnL vs Trader Sentiment")
    plt.xlabel("Trader Sentiment")
    plt.ylabel("Closed PnL")
    plt.savefig("Sentimentwise_Closed_PnL_Boxplot.png")  # save plot
    plt.show()
# -------------------------------
# Step 4: Optional Market Sentiment Analysis
# -------------------------------

if 'classification' in df.columns:
    print("\n--- Closed PnL vs Market Sentiment ---")
    market_summary = df.groupby('classification')['Closed PnL'].agg(['mean','sum','count'])
    print(market_summary)
    
    # Save summary
    market_summary.to_csv("Market_Classification_Closed_PnL.csv")
    
    # Market sentiment boxplot
    plt.figure(figsize=(6,4))
    sns.boxplot(x='classification', y='Closed PnL', data=df)
    plt.title("Closed PnL vs Market Sentiment")
    plt.xlabel("Market Classification (Fear/Greed)")
    plt.ylabel("Closed PnL")
    plt.savefig("Market_Classification_Boxplot.png")  # save plot
    plt.show()

    print("\n--- All Analysis Completed ---")