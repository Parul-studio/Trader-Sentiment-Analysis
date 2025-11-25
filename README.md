# Trader Sentiment Analysis

This project performs a comprehensive analysis of trader sentiments and closed PnL (Profit and Loss) for various cryptocurrencies. The analysis provides insights into trading behavior, market trends, and sentiment-driven performance.

## Features

* **Trader Sentiment Distribution**
  Visualizes the distribution of trader sentiment (Bullish, Bearish, Neutral) across all trades using bar charts.

* **Coin-wise Closed PnL Analysis**
  Calculates mean, total, and count of closed PnL for each coin and visualizes it using boxplots.

* **Sentiment-wise Closed PnL Analysis**
  Compares closed PnL across trader sentiments, with summary statistics and boxplots for clear insights.

* **Optional Market Sentiment Analysis**
  If the dataset contains a `classification` column (e.g., Fear/Greed), it provides analysis and visualizations of closed PnL vs market sentiment.

* **Automatic Saving of Results**
  All summaries are saved as CSV files, and all plots are saved as PNG images for reference.

## Requirements

* Python 3.x
* pandas
* matplotlib
* seaborn

Install the required packages with:


pip install pandas matplotlib seaborn


## How to Run

Run the analysis script from the project directory:


py insights_combined.py


### Steps performed by the script:

1. Loads the CSV dataset.
2. Generates summary tables for trader sentiment, coin-wise PnL, and optional market sentiment.
3. Creates visualizations for each summary.
4. Saves all summaries as CSV files and plots as PNG images.

**Note:**

* Coin-wise boxplots may appear congested if there are many coins.
* Plots are displayed sequentially; close the current plot window to view the next.
* Optional analysis runs only if the `classification` column exists in the dataset.

## Author

**Parul Gautam**
GitHub: [https://github.com/Parul-studio](https://github.com/Parul-studio)


