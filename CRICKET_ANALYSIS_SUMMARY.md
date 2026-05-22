# IPL Cricket Analysis: Key Findings (5 Seasons)
### BY --- NIRMIT GUPTA 

## Question 1: Does Winning the Toss Actually Help?

### Answer: **Almost No Advantage**

- |   **Outcome**   |**Win Rate**|
- | **Toss Winner** |   50.49 %  |
- | **Toss Loser**  |   49.51 %  |

**Finding:** Winning the toss provides virtually no advantage. The win rates are nearly identical—flipping a coin would be just as predictive. Despite the strategic advantage of choosing to bat or field first, the actual impact on match outcomes is negligible.

## Question 2: Which Phase Matters Most for Winning?

### Answer: **All Three Phases Matter**

#### Average Runs Scored by Winning vs Losing Teams:

- |         **Phase**         | **Winning Teams** | **Losing Teams** | **Difference** |
- | **Powerplay (Overs 1-6)** |       51.29       |       45.48      |   +5.81 runs   |
- | **Middle Overs (7-15)**   |       74.33       |       66.49      |   +7.84 runs   |
- | **Death Overs (16-20)**   |       47.24       |       43.52      |   +3.72 runs   |

### Key Insight: **Death Overs Are Most Predictive**

- Teams scoring in the **top 25%** during death overs: **56.8% win rate**
- Teams scoring in the **top 25%** during powerplay: **63.3% win rate**

**Answer:** While powerplay scoring correlates more strongly with winning, middle overs show the biggest absolute difference (+7.84 runs). Winners maintain composure and consistency throughout the innings, not just explosive starts or finishes.

## Question 3: Top 5 Batters and Bowlers (5 Seasons)

### Top 5 Batters (by Total Runs)

- | **Rank** |  **Player**     | **Total Runs** | **Matches** |
- |    1     |  Virat Kohli    |     9,050      |    268      |
- |    2     |  Rohit Sharma   |     7,269      |    271      |
- |    3     |  Shikhar Dhawan |     6,769      |    221      |
- |    4     |  David Warner   |     6,567      |    184      |
- |    5     |  KL Rahul       |     5,680      |    145      |

### Top 5 Bowlers (by Wickets)

- | **Rank** |    **Player**     | **Wickets** |
- |    1     | Yuzvendra Chahal  |    238      |
- |    2     | Bhuvneshwar Kumar |    231      |
- |    3     | Sunil Narine      |    223      |
- |    4     | Dwayne Bravo      |    207      |
- |    5     | Jasprit Bumrah    |    207      |

## The Surprising Insight

**"Death overs batting is a better predictor of match victory than powerplay aggression—yet winning teams consistently outscore losers in ALL three phases."**

The data reveals that while explosive powerplay starts grab attention, sustained middle-overs performance is what separates champions from also-rans. Winners don't just bat differently in any one phase; they execute better across the entire innings.


## Visualizations Guide

### Chart 1: Toss Win Rate Comparison
**File:** `toss_win_rate.png`
**Interpretation:**
- Nearly identical bar heights (~50% each) indicate no toss advantage
- Equal bars suggest toss is random/neutral factor
- Any significant difference would indicate toss impact

### Chart 2: Phase-Wise Performance Analysis
**File:** `phase_analysis.png`
**Interpretation:**
- Green bars consistently higher = Winners score more in ALL phases
- Largest gap = Most important phase for victory
- Pattern shows consistency importance
- Middle overs have the largest gap (+7.84 runs)
- Winning teams don't dominate just one phase
- Consistent performance across phases wins matches

### Chart 3: Top 5 Batters by Total Runs
**File:** `top_batters.png`
**Interpretation:**
- Longer bars = More runs across 5 seasons
- Virat Kohli (9,050 runs)
- Significant gaps show performance hierarchy

### Chart 4: Top 5 Bowlers by Wickets
**File:** `top_bowlers.png`
**Interpretation:**
- Longer bars = More wickets across 5 seasons
- Yuzvendra Chahal leads with 238 wickets
- Tight clustering shows competitive bowling
