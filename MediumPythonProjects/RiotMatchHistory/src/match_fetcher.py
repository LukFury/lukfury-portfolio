import os
import sys
import json
from pathlib import Path
from dotenv import load_dotenv

# Ensure imports work no matter how it's run
root_dir = Path(__file__).resolve().parents[1]
sys.path.append(str(root_dir))

from src.api_client import RiotAPI
from utils.logger import get_logger

# Dynamically resolve project directories
PROJECT_ROOT = root_dir
DATA_DIR = PROJECT_ROOT / "data" / "Raw_Matches"
LOG_DIR = PROJECT_ROOT / "logs"

logger = get_logger("match_fetcher", log_dir=LOG_DIR)

def fetch_and_save_player_matches(api: RiotAPI, game_name: str, tag_line: str, save_dir: Path = DATA_DIR):
    """High-level pipeline: get all recent matches and save them as JSON."""
    account = api.get_account_by_riot_id(game_name, tag_line)
    if not account:
        logger.error("Could not fetch account.")
        return

    puuid = account["puuid"]
    matches = api.get_match_ids_by_puuid(puuid, count=10)
    if not matches:
        logger.warning("No matches found.")
        return

    save_dir.mkdir(parents=True, exist_ok=True)
    for match_id in matches:
        data = api.get_match_details(match_id)
        if data:
            (save_dir / f"{match_id}.json").write_text(json.dumps(data, indent=2))
            logger.info(f"Saved {match_id}.json")

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("RIOT_API_KEY")
    if not api_key:
        raise ValueError("Missing RIOT_API_KEY in .env file")

    api = RiotAPI(api_key)
    fetch_and_save_player_matches(api, "LukFury", "EUW")
