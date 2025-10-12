import sys
from pathlib import Path
import pandas as pd

# Make sure src is visible
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))
from data_loader import load_pro_league_data  # type: ignore
from data_cleaner import clean_data  # type: ignore

if __name__ == "__main__":
    # Build the absolute path safely
    raw_folder = Path(__file__).resolve().parent.parent / "Data" / "Raw"
    print(f"Looking in: {raw_folder}")

    # Check if folder exists
    if not raw_folder.exists():
        print("❌ Folder not found!")
        raise SystemExit()
    
    df = load_pro_league_data(raw_folder, multi_file=True)
    
    df = clean_data(df)
    print("✅ Data cleaned successfully!")
