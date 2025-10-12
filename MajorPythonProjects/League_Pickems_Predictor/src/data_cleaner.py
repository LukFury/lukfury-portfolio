import pandas as pd
import yaml
from pathlib import Path
from datetime import datetime
from time import perf_counter

def clean_data(df: pd.DataFrame, config_path: str | Path | None = None) -> pd.DataFrame:
    """
    Cleans the dataframe using parameters from config.yaml.
    Logs every step to a timestamped log file in the configured log directory.
    """
    start = perf_counter()
    
    # 🔍 Auto-locate config if not provided
    if config_path is None:
        project_root = Path(__file__).resolve().parent.parent
        config_path = project_root / "config" / "config.yaml"

    cfg = yaml.safe_load(Path(config_path).read_text())

    # 📂 Build absolute paths
    project_root = Path(__file__).resolve().parent.parent
    log_dir = project_root / Path(cfg["paths"]["log_dir"])
    output_path = project_root / Path(cfg["paths"]["cleaned_output"])
    key_columns = cfg["columns"]["key_columns"]
    date_col = cfg["columns"]["date_column"]
    verbose = cfg["settings"]["verbose"]

    # 🛠 Ensure directories exist
    log_dir.mkdir(parents=True, exist_ok=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 🧾 Create a new log file
    log_file = log_dir / f"clean_log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    def log(msg: str):
        if verbose:
            print(msg)
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(msg + "\n")

    start_rows = len(df)
    log(f"🧽 Starting clean — initial rows: {start_rows}")

    # 1️⃣ Drop duplicates
    before = len(df)
    df = df.drop_duplicates()
    log(f"Removed duplicates: {before - len(df)}")

    # 2️⃣ Remove incomplete rows
    if "datacompleteness" in df.columns:
        before = len(df)
        removed_rows = df.loc[df["datacompleteness"] != "complete", key_columns]
        if not removed_rows.empty:
            log(f"Dropped incomplete rows (partial): {len(removed_rows)}")
        df = df[df["datacompleteness"] == "complete"]
        log(f"Rows removed (partial): {before - len(df)}")

    # 3️⃣ Convert 'date' to datetime
    if date_col in df.columns:
        df[date_col] = pd.to_datetime(df[date_col], errors=cfg["settings"]["date_parse_errors"])
        log(f"Converted '{date_col}' column to datetime")

    # 4️⃣ Enforce numeric types where possible
    numeric_converted = 0
    for col in df.columns:
        try:
            old_type = df[col].dtype
            df[col] = pd.to_numeric(df[col])
            if df[col].dtype != old_type:
                numeric_converted += 1
        except (ValueError, TypeError):
            pass
    log(f"Columns converted to numeric: {numeric_converted}")

    # 5️⃣ Drop rows missing key identifiers
    before = len(df)
    missing_keys = df[df[key_columns].isna().any(axis=1)]
    if not missing_keys.empty:
        log(f"Dropped rows missing key IDs: {len(missing_keys)}")
    df = df.dropna(subset=key_columns, how="any")
    log(f"Rows removed (missing keys): {before - len(df)}")

    # 6️⃣ Final summary + CSV export
    df.to_csv(output_path, index=cfg["settings"]["index"])
    removed_total = start_rows - len(df)
    log(f"✅ Cleaned dataframe: {df.shape[0]} rows, {df.shape[1]} columns")
    log(f"📉 Total rows removed: {removed_total} ({removed_total/start_rows:.2%} data loss)")
    log(f"✅ Saved cleaned data → {output_path}")

    if verbose:
        print(f"✅ Cleaned data saved to: {output_path}")

    log(f"⏱ Cleaning completed in {perf_counter() - start:.2f} seconds")
    return df
