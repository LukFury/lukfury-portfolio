import pandas as pd
import re
from pathlib import Path
from collections import Counter
import json

log_file = Path("MiniPythonProjects/Syntax_Speed_Builder/Json_Cleaning_1/unclean_log.txt")
pattern = r"\[(.*?)\]\s+(\w+)\s+–\s+(.*)"

# initialize your counter
level_counts = Counter()

# open and read file line by line
with log_file.open("r", encoding="utf-8") as f:
    for line in f:
        match = re.match(pattern, line)
        if match:
            _, level, _ = match.groups()
            # 👇 increment your counter here
            level_counts[level] += 1

# preview your results
json.dump(level_counts, open("MiniPythonProjects/Syntax_Speed_Builder/Json_Cleaning_1/summary.json", "w"), indent=4)
print(level_counts)
