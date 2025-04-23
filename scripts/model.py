"""Model"""

# Analyze results
def compare_xg_actual(df):
    df['xg_diff'] = df['expected_goals'] - df['goals_scored']
    return df.sort_values(by='xg_diff', ascending=False)
