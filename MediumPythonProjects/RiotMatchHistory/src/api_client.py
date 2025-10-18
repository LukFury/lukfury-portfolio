import requests
from utils.logger import get_logger

logger = get_logger("api_client")

class RiotAPI:
    """
    A lightweight wrapper around Riot's REST API.
    Handles authentication, requests, and simple error handling.
    """

    def __init__(self, api_key: str, region: str = "europe"):
        self.api_key = api_key
        self.base = f"https://{region}.api.riotgames.com"

    def _get(self, endpoint: str, params: dict | None = None):
        """Internal helper for GET requests with logging."""
        if params is None:
            params = {}
        
        url = f"{self.base}{endpoint}"
        headers = {"X-Riot-Token": self.api_key}
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=10)
            resp.raise_for_status()
            logger.info(f"✅  {endpoint} - {resp.status_code}")
            return resp.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"❌  {endpoint} failed: {e}")
            return None
        
    # ------------------- Actual API Calls -------------------

    def get_account_by_riot_id(self, game_name: str, tag_line: str):
        """Return account data using Riot ID."""
        endpoint = f"/riot/account/v1/accounts/by-riot-id/{game_name}/{tag_line}"
        return self._get(endpoint)

    def get_match_ids_by_puuid(self, puuid: str, count: int = 10, start: int = 0):
        """Fetch a list of match IDs for a given player."""
        endpoint = f"/lol/match/v5/matches/by-puuid/{puuid}/ids"
        params = {"start": start, "count": count}
        return self._get(endpoint, params)

    def get_match_details(self, match_id: str):
        """Get detailed data for a specific match."""
        endpoint = f"/lol/match/v5/matches/{match_id}"
        return self._get(endpoint)