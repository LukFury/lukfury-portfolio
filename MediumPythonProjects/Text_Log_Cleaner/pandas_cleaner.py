"""
Text Log Cleaner using Pandas
--------------------------------
Cleans text logs by removing timestamps and system messages,
splits speaker and message for readability, and writes a
clean UTF-8 text file.

Author: Lukasz Basczask
Date: 2025-11-10
"""

import pandas as pd
import re
from pathlib import Path

# === CONFIGURATION ===

BASE_DIR = Path(__file__).parent

INPUT_FILE = BASE_DIR / "Logs" / "messy_log.txt"
OUTPUT_FILE = BASE_DIR / "Output" / "cleaned_raw_pandas.txt"

TIMESTAMP_REGEX = re.compile(
    r'\[?('
    r'(?:\d{4}|\d{2})[-/\.]\d{2}[-/\.](?:\d{4}|\d{2})'
    r'(?:[ T:-]*\d{2}:\d{2}:\d{2})?'
    r'|\d{2}:\d{2}:\d{2}'
    r')\]?'
)
SYSTEM_KEYWORDS = ['SYSTEM', 'SERVER', 'ERROR', 'ALERT', 'WARNING']

def filter_system_lines(df):
        # filter out system lines
    pattern = '|'.join(SYSTEM_KEYWORDS)
    df = df[~df['raw'].str.upper().str.contains(pattern)]
    return df

def remove_timestamps(df):
    df['cleaned'] = df['raw'].str.replace(TIMESTAMP_REGEX, '', regex=True)
    df['cleaned'] = (
        df['cleaned']
        .str.replace(r'\s+', ' ', regex=True)
        .str.strip(" -|:<>\n\t")
    )
    return df

def main():
    pd.set_option('display.max_colwidth', 50)

    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as file:
        
            lines = [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Error reading {INPUT_FILE}: {e}")
        return

    df = pd.DataFrame({'raw': lines})
    df = df.dropna()  
    df['raw'] = df['raw'].astype(str)

    # filter out system lines
    df = filter_system_lines(df)

    df = remove_timestamps(df)

    if df.empty:
        print("No valid log lines found after cleaning.")
        return

    # split speaker/message
    df[['speaker', 'message']] = df['cleaned'].str.split(pat=':', n=1, expand=True)
    df['speaker'] = df['speaker'].fillna('Unknown').str.strip(" <>[]-")
    df['message'] = df['message'].fillna('').str.strip()

    # reconstruct formatted string
    df['final'] = (
        '[' + df['raw'].str.extract(TIMESTAMP_REGEX)[0] + '] ' +
        df['speaker'].str.pad(15) + ': ' +
        df['message']
    )
    
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True) # ensure output dir exists
    
    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write('\n'.join(df['final']))
    except Exception as e:
        print(f"Error writing {OUTPUT_FILE}: {e}")

    print("\nSummary:")
    print(df[['speaker', 'message']].head(5))
    print(f"🧮 Total lines processed: {len(lines)}")
    print(f"✅ Valid lines kept: {len(df)}")


if __name__ == "__main__":
    main()
