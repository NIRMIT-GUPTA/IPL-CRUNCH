# IPL Cricket Analysis:
# BY --- NIRMIT GUPTA

-----

##  Table of Contents :
- 1.OVERVIEW
- 2.DIRECTORY LAYOUT
- 3.FILE DESCRIPTIONS
- 4.STEPS
- 5.TECHNOLOGY USED
- 6.EXPECTED OUTPUT

-----

### Overview

This project performs comprehensive statistical analysis on **Indian Premier League (IPL)** cricket data. 
The analysis examines three critical questions about IPL match outcomes:
1. **Toss Impact Analysis** - Does winning the coin toss actually influence match victory?
2. **Phase-Based Performance** - Which phase (powerplay, middle overs, death overs) is most crucial for winning?
3. **Player Performance Ranking** - Who are the top batters and bowlers across all 5 seasons?

-----

### Directory Layout
```
IPL-CRUNCH/
├── cricket_analysis.py              # Main analysis script
├── .gitattributes                   # Git LFS configuration
├── ipldata.csv                      # IPL ball-by-ball data (Git LFS, 70 MB)
├── requirements.txt                 # Python dependencies
├── README.md                        # This comprehensive guide
├── CRICKET_ANALYSIS_SUMMARY.md      # Executive summary
├── cricket_analysis_charts.png      # All charts in one file
└── charts/                          # Output visualizations folder
    ├── toss_win_rate.png           # Chart 1: Toss impact comparison
    ├── phase_analysis.png          # Chart 2: Phase-wise performance
    ├── top_batters.png             # Chart 3: Top 5 batters
    └── top_bowlers.png             # Chart 4: Top 5 bowlers
```

-----

### File Descriptions

#### `cricket_analysis.py` (Main Script)
- **Purpose:** Core analysis engine
- **Input:** ipldata.csv
- **Output:** 4 PNG charts + console analysis

#### `ipldata.csv` (Data File - Git LFS)
- **Rows:** 289,674 ball-level records
- **Size:** ~70 MB
- **Format:** Comma-separated values
- **Storage:** Git Large File Storage (LFS) AND GOOGLE DRIVE 
- **Status:** Stored on GitHub LFS server

#### `.gitattributes`
- **Purpose:** Tells Git which files to track with LFS
- **Content:** `*.csv filter=lfs diff=lfs merge=lfs -text`
- **Auto-created:** When you initialize Git LFS

#### `requirements.txt`
- **Purpose:** Lists all Python package dependencies
- **Format:** Package name and version constraints
- **Usage:** `pip install -r requirements.txt`

#### `README.md`
- **Purpose:** Complete project documentation (this file)

#### `CRICKET_ANALYSIS_SUMMARY.md`
- **Purpose:** Executive summary of findings
- **Best For:** Quick overview without reading full README

#### `charts/` Directory
- **Purpose:** Stores generated visualization PNG files
- **Auto-Created:** Script creates this folder if not present
- **Files Generated:** 4 professional-quality charts (300 DPI)

#### `cricket_analysis_charts.png`
- All charts in one file
-----

### STEPS TO FOLLLOW --- 

#### DOWNLOAD OR CLONE THIS REPOSITORY 
- (Use Git to clone (enables LFS automatic downloads))
- git clone https://github.com/NIRMIT-GUPTA/IPL-CRUNCH.git
- cd IPL-CRUNCH

#### READ THE "README.md" FILE (THIS FILE)

#### DATASET --- ".gitattributes" "ipldata.csv"

- THE DATASET NEEDED IS UPLOADED ON GIT LFS SERVER (FILE SIZE = 70 MB) SO GIT LFS IS A REQUIREMENT 
- USERS WITH LFS WILL SEE THE "ipldata.csv" ON CLONING OR DOWNLOADING THE REPOSITORY
- INSTALL GIT LFS FROM https://git-lfs.github.com/

- OR DOWNLOAD DATASET FROM GOOGLE DRIVE LINK --- https://drive.google.com/drive/folders/1K-eNDGQ4DNLX5JHkEt5fOnzzLh6QXypy?usp=drive_link
- OR FROM THE OFFICIAL WOOBLE IPL CRUNCH 26 HACKATHON PAGE
- OR GO TO THE REPOSITORY -> ipldata.csv -> FIND LFS DOWNLOAD LINK
- AND REPLACE THE POINTER FILE (1KB) WITH DATA FILE

#### MAKE SURE TO NAME THE DATASET FILE "ipldata.csv" AND PLACE IT IN SAME FOLDER AS THE SCRIPT AND IS ~70 MB

- ls -lh ipldata.csv
- INCORRECT: Shows ~1 KB or less
- git lfs install
- git lfs pull
- ls -lh ipldata.csv  # Should now be 70MB


#### SETUP REQUIREMENTS --- "requirements.txt" --- 
- pip install -r requirements.txt

#### RUN CODE --- "cricket_analysis.py" --- python cricket_analysis.py
- THIS WILL OUTPUT THE ANALYSIS IN TERMINAL AND MAKE A NEW FOLDER WILL 4 CHARTS IN THE SAME FOLDER 

#### CHARTS --- "charts/" 
- THE FOLDER YOU GET ON RUNNIG THE PYTHON CODE WHICH CONTAINS 4 CHARTS :
- toss_win_rate.png
- phase_analysis.png
- top_batters.png 
- top_bowlers.png
- ls charts/  # Shows 4 PNG files

#### DIRECT ANALYSIS --- "CRICKET_ANALYSIS_SUMMARY.md" "cricket_analysis_charts.png"--- 
- CONTAINS THE COMPLETE ANALYSIS AND FINDINGS OF THE DATASET AND THE CHARTS IN ONE FILE
- ANSWERS THE QUESTIONS FROM THE PROBLEM STATEMENT AND INTERPRETS THE CHARTS

-----

### Technologies Used

- **Python 3.7+**
- **Pandas 1.3.0+**
- **NumPy 1.20.0+**
- **Matplotlib 3.4.0+**
- **Seaborn 0.11.0+**
- **Git Large File Storage (LFS)** - Used: Store 70 MB CSV on GitHub

-----

### Expected Output

**Console Terminal:**
- Toss impact analysis results
- Phase-wise performance data
- Top 5 players lists
- Confirmation messages for each chart

**Files Under the Charts folder:**
- toss_win_rate.png 
- phase_analysis.png 
- top_batters.png 
- top_bowlers.png 

-----
