"""Main Script"""

# Load scripts
from scripts.data_loader import fetch_fpl_data
from scripts.visualization import plot_top_xg_gap

# Run main
def main():
    df = fetch_fpl_data()

    # Simulate expected_goals - TEST ONLY
    df['expected_goals'] = df['goals_scored'] + (df['minutes'] / 1000)

    df['xg_diff'] = df['expected_goals'] - df['goals_scored']
    df_sorted = df.sort_values(by='xg_diff', ascending=False)

    plot_top_xg_gap(df_sorted, top_n=10)

if __name__ == "__main__":
    main()
