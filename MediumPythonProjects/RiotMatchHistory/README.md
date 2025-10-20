# 🎮 Riot Match History ETL Pipeline

A modular ETL (Extract–Transform–Load) pipeline in Python that fetches League of Legends match data from the Riot Games API, stores raw JSONs, and transforms them into clean CSVs for quick analysis and visualization.

---

## 🧩 Overview

This repo automates end-to-end match data handling for a given player:

- Extract: Call Riot’s API to get a player’s account, recent match IDs, and full match details
- Transform: Parse raw JSON files and normalize the most useful player stats
- Load: Write a tidy CSV dataset you can use in pandas, Excel, or BI tools

It’s intentionally small, readable, and easy to extend.

---

## 📦 Project Structure

```
RiotMatchHistory/
├─ src/
│  ├─ api_client.py       # Riot API wrapper (GET helpers + endpoints)
│  ├─ match_fetcher.py    # Orchestrates: account → match IDs → raw JSONs
│  ├─ data_cleaner.py     # Reads raw JSONs → writes processed CSV
│  └─ main.py             # (placeholder) wire modules or CLI in future
│
├─ utils/
│  ├─ logger.py           # Centralized console+file logging
│  └─ cache_handler.py    # (placeholder) caching for future work
│
├─ data/
│  ├─ Raw_Matches/        # Saved raw match JSONs
│  └─ Processed/          # Cleaned CSV outputs
│
├─ tests/
│  └─ test_api_client.py  # Quick sanity checks for API calls
│
├─ .env                   # Your Riot API key (not committed)
└─ README.md              # You’re reading it
```

---

## ⚙️ Features

- ✅ Simple, modular ETL layout (extract/transform/load)
- ✅ Clean logging to both console and file (per-day log files)
- ✅ `.env`-based secret management for your API key
- ✅ Easy to tweak for other regions and fields

---

## 🚀 Quickstart

### 1) Prerequisites

- Python 3.10+
- A valid Riot API key (developer portal)

### 2) Install dependencies

Using PowerShell on Windows:

```powershell
# (Optional) Create and activate a virtual environment
py -m venv .venv ; .\.venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt
```

If you don’t want a venv, you can directly install:

```powershell
pip install requests python-dotenv pandas
```

### 3) Add your API key

Create a `.env` file at the project root:

```
RIOT_API_KEY=your_api_key_here
```

### 4) Fetch recent matches (Extract)

By default, `src/match_fetcher.py` fetches the last 10 matches for the Riot ID `LukFury#EUW` and saves each match as JSON under `data/Raw_Matches/`.

Run:

```powershell
python .\src\match_fetcher.py
```

Want a different player or tag? Open `src/match_fetcher.py` and change the two values in the last line:

```
fetch_and_save_player_matches(api, "YourGameName", "YourTag")
```

You can also change the region when initializing the API client (default is `europe`, which is correct for Match-V5 in EU):

```
api = RiotAPI(api_key, region="americas" | "asia" | "europe")
```

### 5) Clean and aggregate (Transform + Load)

`src/data_cleaner.py` scans `data/Raw_Matches/`, extracts the stats for a given `player_name`, and writes a CSV to `data/Processed/match_summary.csv`.

Run:

```powershell
python .\src\data_cleaner.py
```

Change the player by editing the `player_name` variable near the top of `src/data_cleaner.py`.

---

## 📄 Output

- Raw JSONs: `data/Raw_Matches/*.json`
- Processed CSV: `data/Processed/match_summary.csv`
- Logs: `logs/YYYY-MM-DD.log`

Example rows from the processed CSV in this repo:

```
matchId,champion,kills,deaths,assists,damage,gold,win
EUW1_7559534087,Xerath,4,12,7,19419,9309,False
EUW1_7561782052,Swain,8,11,11,29337,14331,False
EUW1_7563438041,Darius,7,9,5,35082,15503,True
…
```

---

## 🧠 Tech Stack

- Python
- Requests (HTTP client)
- Pandas (data wrangling)
- python-dotenv (config via `.env`)
- Logging (built-in)

---

## 🧱 Design Notes

- Extract: `RiotAPI` in `src/api_client.py` wraps Riot endpoints with simple error handling and logging.
- Transform: `src/data_cleaner.py` picks your player’s row from each match’s `participants` and builds a compact, analysis-ready table.
- Load: Data lands in `data/Processed/` as CSV.

Future-friendly:

- `utils/cache_handler.py` and `src/main.py` are placeholders for caching and a unified CLI/flow (e.g., Airflow/Prefect) if you want to scale this into a bigger pipeline.

---

## 🧩 Tips & Troubleshooting

- Missing API key: ensure `.env` contains `RIOT_API_KEY` and you’ve restarted the shell or reloaded the environment.
- 403 errors: your key may be expired or you’re hitting rate limits. Regenerate the key in the Riot developer portal.
- Region routing: Match-V5 uses “regional routes” like `europe`, `americas`, `asia` for match endpoints. Choose the one that matches your account’s routing.
- Logs: check the latest file in `logs/` for detailed error messages.

---

## 📈 Next ideas

- Add CLI args to `match_fetcher.py` (player, tag, count)
- Expand `data_cleaner.py` with more features (vision, CS, items, runes)
- Add caching to reduce API calls and improve speed
- Wire into an orchestration tool or GitHub Actions for scheduled runs

---

Made with 💙 for data workflows and LoL stats.

