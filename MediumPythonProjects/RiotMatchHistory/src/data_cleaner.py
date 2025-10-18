import json
import sys
import pandas as pd
from pathlib import Path

root_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(root_dir))

def extract_player_stats(match_json, player_name):
    participants = match_json.get("info", {}).get("participants", [])
    for p in participants:
        if (
            p.get("summonerName", "").lower() == player_name.lower()
            or p.get("riotIdGameName", "").lower() == player_name.lower()
        ):
            return {
                "matchId": match_json.get("metadata", {}).get("matchId"),
                "champion": p.get("championName"),
                "kills": p.get("kills"),
                "deaths": p.get("deaths"),
                "assists": p.get("assists"),
                "damage": p.get("totalDamageDealtToChampions"),
                "gold": p.get("goldEarned"),
                "win": p.get("win"),
            }
    return None


player_name = "LukFury"
PROJECT_ROOT = Path(__file__).resolve().parents[1]
print(f"Project root resolved to: {PROJECT_ROOT}")

DATA_DIR = PROJECT_ROOT / "data" / "Raw_Matches"
OUTPUT_DIR = PROJECT_ROOT / "data" / "Processed"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df = pd.DataFrame(
    filter(
        None,
        [
            extract_player_stats(json.loads(f.read_text()), player_name)
            for f in DATA_DIR.glob("*.json")
        ],
    )
)

output_path = OUTPUT_DIR / "match_summary.csv"
df.to_csv(output_path, index=False, encoding="utf-8")

print(f"✅ Saved {len(df)} matches for {player_name} → {output_path}")
print(df.head())
