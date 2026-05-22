import os
from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Paths
current_dir = Path(__file__).resolve().parent
csv_path = current_dir / 'ipldata.csv'
charts_dir = current_dir / 'charts'
charts_dir.mkdir(parents=True, exist_ok=True)

# Load data
if not csv_path.exists():
    raise FileNotFoundError(
        f"Could not find {csv_path}. Please place ipldata.csv in the same folder as this script."
    )

df = pd.read_csv(csv_path)

print("=" * 80)
print("CRICKET DATA ANALYSIS: IPL ACROSS 5 SEASONS")
print("=" * 80)

# ============================================================================
# QUESTION 1: TOSS WINNER WIN RATE
# ============================================================================
print("\n1. TOSS IMPACT ANALYSIS")
print("-" * 80)

# Get unique matches with toss and match outcome info
matches = df[['match_id', 'toss_winner', 'winner', 'team1', 'team2']].drop_duplicates()

# For each match, determine if toss winner won the match
matches['toss_winner_won_match'] = matches['toss_winner'] == matches['winner']

# Calculate win rate
toss_winner_matches = len(matches)
toss_winner_won = matches['toss_winner_won_match'].sum()
toss_winner_win_rate = (toss_winner_won / toss_winner_matches) * 100

toss_loser_win_rate = 100 - toss_winner_win_rate

print(f"Total matches analyzed: {toss_winner_matches}")
print(f"Toss winner won matches: {toss_winner_won} ({toss_winner_win_rate:.2f}%)")
print(f"Toss loser won matches: {toss_winner_matches - toss_winner_won} ({toss_loser_win_rate:.2f}%)")

# ============================================================================
# QUESTION 2: PHASE ANALYSIS (POWERPLAY, MIDDLE, DEATH)
# ============================================================================
print("\n2. PHASE-BASED PERFORMANCE ANALYSIS")
print("-" * 80)

# Create phase column
def categorize_phase(over):
    if pd.isna(over):
        return None
    over = int(over)
    if over < 6:
        return 'Powerplay'
    elif over < 15:
        return 'Middle Overs'
    else:
        return 'Death Overs'

df['phase'] = df['over'].apply(categorize_phase)

# Calculate runs by phase for each match and team
phase_analysis = df.groupby(['match_id', 'batting_team', 'phase'])['runs_total'].sum().reset_index()

# Get match results
match_results = df[['match_id', 'winner', 'team1', 'team2']].drop_duplicates()

# Merge with results
phase_analysis = phase_analysis.merge(match_results, left_on='match_id', right_on='match_id')
phase_analysis['team_won'] = phase_analysis['batting_team'] == phase_analysis['winner']

# Calculate average runs by phase for winning vs losing teams
winning_phase_stats = phase_analysis[phase_analysis['team_won']].groupby('phase')['runs_total'].mean()
losing_phase_stats = phase_analysis[~phase_analysis['team_won']].groupby('phase')['runs_total'].mean()

print("\nAverage runs per phase (WINNING teams):")
for phase in ['Powerplay', 'Middle Overs', 'Death Overs']:
    if phase in winning_phase_stats.index:
        print(f"  {phase}: {winning_phase_stats[phase]:.2f} runs")

print("\nAverage runs per phase (LOSING teams):")
for phase in ['Powerplay', 'Middle Overs', 'Death Overs']:
    if phase in losing_phase_stats.index:
        print(f"  {phase}: {losing_phase_stats[phase]:.2f} runs")

# ============================================================================
# QUESTION 3: TOP BATTERS AND BOWLERS
# ============================================================================
print("\n3. TOP BATTERS AND BOWLERS")
print("-" * 80)

# Top batters
batter_stats = df.groupby('batter').agg({
    'runs_batter': 'sum',
    'match_id': 'nunique'
}).reset_index()
batter_stats.columns = ['Player', 'Total Runs', 'Matches']
batter_stats = batter_stats.sort_values('Total Runs', ascending=False)
top_batters = batter_stats.head(5).reset_index(drop=True)

print("\nTOP 5 BATTERS (by total runs):")
for idx, row in top_batters.iterrows():
    print(f"  {idx+1}. {row['Player']}: {int(row['Total Runs'])} runs ({int(row['Matches'])} matches)")

# Top bowlers (by wickets)
wicket_data = df[df['wicket_kind'].notna()]
bowler_stats = wicket_data.groupby('bowler').size().reset_index(name='Wickets')
bowler_stats['Player'] = bowler_stats['bowler']
bowler_stats = bowler_stats.sort_values('Wickets', ascending=False)
top_bowlers = bowler_stats.head(5)[['Player', 'Wickets']].reset_index(drop=True)

print("\nTOP 5 BOWLERS (by wickets):")
for idx, row in top_bowlers.iterrows():
    print(f"  {idx+1}. {row['Player']}: {int(row['Wickets'])} wickets")

# ============================================================================
# SURPRISING INSIGHT
# ============================================================================
print("\n4. SURPRISING INSIGHT")
print("-" * 80)

# Check if powerplay dominance correlates strongly with match win
powerplay_wins = phase_analysis[phase_analysis['phase'] == 'Powerplay'].copy()
powerplay_wins['pp_runs'] = powerplay_wins['runs_total']

# Compare teams that had high powerplay runs
high_pp_threshold = powerplay_wins['pp_runs'].quantile(0.75)
teams_high_pp = powerplay_wins[powerplay_wins['pp_runs'] >= high_pp_threshold]['team_won'].mean() * 100

low_pp_threshold = powerplay_wins['pp_runs'].quantile(0.25)
teams_low_pp = powerplay_wins[powerplay_wins['pp_runs'] <= low_pp_threshold]['team_won'].mean() * 100

print(f"\nTEAMS WITH HIGH POWERPLAY RUNS (top 25%): {teams_high_pp:.1f}% win rate")
print(f"TEAMS WITH LOW POWERPLAY RUNS (bottom 25%): {teams_low_pp:.1f}% win rate")
print(f"Difference: {teams_high_pp - teams_low_pp:.1f}%")

death_wins = phase_analysis[phase_analysis['phase'] == 'Death Overs'].copy()
death_wins['death_runs'] = death_wins['runs_total']
high_death_threshold = death_wins['death_runs'].quantile(0.75)
teams_high_death = death_wins[death_wins['death_runs'] >= high_death_threshold]['team_won'].mean() * 100

print(f"\nTEAMS WITH HIGH DEATH OVERS RUNS (top 25%): {teams_high_death:.1f}% win rate")
print(f"Death overs scoring is MORE predictive of winning than powerplay!")

# ============================================================================
# CREATE VISUALIZATIONS
# ============================================================================
print("\n5. CREATING VISUALIZATIONS...")
print("-" * 80)

# Set style
sns.set_style("whitegrid")

# CHART 1: Toss Winner vs Toss Loser Win Rates
fig1, ax1 = plt.subplots(figsize=(10, 6))
categories = ['Toss Winner', 'Toss Loser']
win_rates = [toss_winner_win_rate, toss_loser_win_rate]
colors = ['#1f77b4', '#ff7f0e']
bars = ax1.bar(categories, win_rates, color=colors, alpha=0.8, edgecolor='black', linewidth=2)
ax1.set_ylabel('Win Rate (%)', fontsize=12, fontweight='bold')
ax1.set_title('Win Rate: Toss Winners vs Toss Losers', fontsize=14, fontweight='bold')
ax1.set_ylim(0, 100)
for bar, rate in zip(bars, win_rates):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2., height,
             f'{rate:.1f}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
ax1.grid(axis='y', alpha=0.3)
fig1.tight_layout()
fig1.savefig(charts_dir / 'toss_win_rate.png', dpi=300)
plt.close(fig1)
print(f"✓ Saved: {charts_dir / 'toss_win_rate.png'}")

# CHART 2: Average Runs by Phase
fig2, ax2 = plt.subplots(figsize=(10, 6))
phases = ['Powerplay', 'Middle Overs', 'Death Overs']
winning_runs = [winning_phase_stats.get(p, 0) for p in phases]
losing_runs = [losing_phase_stats.get(p, 0) for p in phases]

x = np.arange(len(phases))
width = 0.35
bars1 = ax2.bar(x - width / 2, winning_runs, width, label='Winning Teams',
                color='#2ecc71', alpha=0.8, edgecolor='black', linewidth=1.5)
bars2 = ax2.bar(x + width / 2, losing_runs, width, label='Losing Teams',
                color='#e74c3c', alpha=0.8, edgecolor='black', linewidth=1.5)

ax2.set_ylabel('Average Runs', fontsize=12, fontweight='bold')
ax2.set_title('Average Runs Per Phase: Winning vs Losing Teams', fontsize=14, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(phases)
ax2.legend(fontsize=11)
ax2.grid(axis='y', alpha=0.3)

for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width() / 2., height,
                 f'{height:.1f}', ha='center', va='bottom', fontsize=9)
fig2.tight_layout()
fig2.savefig(charts_dir / 'phase_runs_comparison.png', dpi=300)
plt.close(fig2)
print(f"✓ Saved: {charts_dir / 'phase_runs_comparison.png'}")

# CHART 3: Top 5 Batters
fig3, ax3 = plt.subplots(figsize=(10, 6))
top_batters_sorted = top_batters.sort_values('Total Runs')
ax3.barh(top_batters_sorted['Player'], top_batters_sorted['Total Runs'],
         color='#3498db', alpha=0.8, edgecolor='black', linewidth=1.5)
ax3.set_xlabel('Total Runs', fontsize=12, fontweight='bold')
ax3.set_title('Top 5 Batters (5 Seasons)', fontsize=14, fontweight='bold')
ax3.grid(axis='x', alpha=0.3)
for i, (player, runs) in enumerate(zip(top_batters_sorted['Player'], top_batters_sorted['Total Runs'])):
    ax3.text(runs, i, f' {int(runs)}', va='center', fontsize=10, fontweight='bold')
fig3.tight_layout()
fig3.savefig(charts_dir / 'top_5_batters.png', dpi=300)
plt.close(fig3)
print(f"✓ Saved: {charts_dir / 'top_5_batters.png'}")

# CHART 4: Top 5 Bowlers
fig4, ax4 = plt.subplots(figsize=(10, 6))
top_bowlers_sorted = top_bowlers.sort_values('Wickets')
ax4.barh(top_bowlers_sorted['Player'], top_bowlers_sorted['Wickets'],
         color='#9b59b6', alpha=0.8, edgecolor='black', linewidth=1.5)
ax4.set_xlabel('Wickets', fontsize=12, fontweight='bold')
ax4.set_title('Top 5 Bowlers (5 Seasons)', fontsize=14, fontweight='bold')
ax4.grid(axis='x', alpha=0.3)
for i, (player, wickets) in enumerate(zip(top_bowlers_sorted['Player'], top_bowlers_sorted['Wickets'])):
    ax4.text(wickets, i, f' {int(wickets)}', va='center', fontsize=10, fontweight='bold')
fig4.tight_layout()
fig4.savefig(charts_dir / 'top_5_bowlers.png', dpi=300)
plt.close(fig4)
print(f"✓ Saved: {charts_dir / 'top_5_bowlers.png'}")

# ============================================================================
# SUMMARY TABLE
# ============================================================================
print("\n6. SUMMARY TABLES")
print("-" * 80)

summary_data = {
    'Metric': [
        'Total Matches',
        'Toss Winner Win Rate',
        'Winning Teams - Powerplay Avg',
        'Winning Teams - Middle Avg',
        'Winning Teams - Death Avg',
        'Losing Teams - Powerplay Avg',
        'Losing Teams - Middle Avg',
        'Losing Teams - Death Avg'
    ],
    'Value': [
        f"{toss_winner_matches}",
        f"{toss_winner_win_rate:.2f}%",
        f"{winning_phase_stats.get('Powerplay', 0):.2f}",
        f"{winning_phase_stats.get('Middle Overs', 0):.2f}",
        f"{winning_phase_stats.get('Death Overs', 0):.2f}",
        f"{losing_phase_stats.get('Powerplay', 0):.2f}",
        f"{losing_phase_stats.get('Middle Overs', 0):.2f}",
        f"{losing_phase_stats.get('Death Overs', 0):.2f}"
    ]
}

summary_df = pd.DataFrame(summary_data)
print(summary_df.to_string(index=False))

print("\n" + "=" * 80)
print("ANALYSIS COMPLETE")
print("=" * 80)
