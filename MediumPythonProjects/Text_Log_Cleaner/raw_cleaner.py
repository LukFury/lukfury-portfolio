from typing import Optional, List
import re

INPUT_FILE = 'MediumPythonProjects/Text_Log_Cleaner/Logs/messy_log.txt'
OUTPUT_FILE = 'MediumPythonProjects/Text_Log_Cleaner/Logs/cleaned_raw.txt'

TIMESTAMP_REGEX = re.compile(
    r'\[?('
    r'(?:\d{4}|\d{2})[-/\.]\d{2}[-/\.](?:\d{4}|\d{2})'  # YYYY-MM-DD or DD-MM-YYYY
    r'(?:[ T:-]*\d{2}:\d{2}:\d{2})?'                     # optional time
    r'|\d{2}:\d{2}:\d{2}'                                # or time only
    r')\]?'
)


SYSTEM_KEYWORDS = ['SYSTEM', 'SERVER', 'ERROR', 'ALERT', 'WARNING']

def is_system_line(line: str) -> bool:
    upper = line.upper()
    return any(keyword in upper for keyword in SYSTEM_KEYWORDS)

def clean_line(line: str) -> Optional[str]:
    timestamp_match = TIMESTAMP_REGEX.search(line)
    if not timestamp_match or not timestamp_match.group(1):
        return None

    timestamp = timestamp_match.group(1)
    rest = TIMESTAMP_REGEX.sub("", line)
    rest = re.sub(r'\s+', ' ', rest).strip(" -|:<>\n\t")

    if ":" in rest:
        parts = rest.split(":", 1)
        speaker = parts[0].strip(" <>[]-")
        message = parts[1].strip()
    else:
        speaker = "Unknown"
        message = rest.strip()

    return f"[{timestamp}] {speaker:15}: {message}"


def main() -> None:
    cleaned_lines: List[str] = []
    with open(INPUT_FILE, 'r', encoding='utf-8') as file:
        for raw_line in file:
            line = raw_line.strip()
            if not line or is_system_line(line):
                continue
            cleaned = clean_line(line)
            if cleaned:
                cleaned_lines.append(cleaned)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as out:
        out.write("\n".join(cleaned_lines))

    print(f"✅ Cleaned log written to: {OUTPUT_FILE}")
    print(f"🧹 {len(cleaned_lines)} lines cleaned and formatted.")

if __name__ == "__main__":
    main()
