import pandas as pd
from pathlib import Path

def load_pro_league_data(raw_folder: str | Path, multi_file: bool = False) -> pd.DataFrame:
    raw_folder = Path(raw_folder)

    if multi_file:
        # Collect all CSVs (only at top level, adjust glob("**/*.csv") if nested)
        csv_files = list(raw_folder.glob("*.csv"))
        if not csv_files:
            raise FileNotFoundError(f"No CSV files found in {raw_folder}")

        print(f"Loading {len(csv_files)} CSV files...")
        # Use generator comprehension so pandas handles the concat efficiently
        df = pd.concat(
            (pd.read_csv(f, low_memory=False) for f in csv_files),
            ignore_index=True
        )
        print(f"Combined dataframe shape: {df.shape}")
        return df

    else:
        file_path = raw_folder / "2025_LoL_esports_match_data_from_OraclesElixir.csv"
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        print(f"Loading single file: {file_path.name}")
        return pd.read_csv(file_path, low_memory=False)
