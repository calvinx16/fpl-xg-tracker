"""Visualize Results"""

# Import necessary packages
import matplotlib.pyplot as plt
import seaborn as sns

# Function to plot graph
def plot_top_xg_gap(df, top_n=10):
    top = df.head(top_n)
    plt.figure(figsize=(10, 6))
    sns.barplot(data=top, x='web_name', y='xg_diff', hue='web_name', legend=False)
    plt.title(f'Top {top_n} Players: xG - Actual Goals')
    plt.ylabel("xG Difference")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
