import re

input_file = 'MiniPythonProjects/Chat_Log_Sanitizer/medium_mess_chat.txt'
output_file = 'MiniPythonProjects/Chat_Log_Sanitizer/sanitized_chat_log.txt'

SYSTEM_KEYWORDS = ['SYSTEM', 'SERVER', 'ERROR', 'ALERT', 'WARNING']

def is_system_line(line: str) -> bool:
    try:
        return any(word in line.upper() for word in SYSTEM_KEYWORDS)
    except Exception as e:
        print(f"Error checking system line: {e}")
        return False

TIMESTAMP_REGEX = re.compile(
    r'\[?('
    r'(?:\d{4}|\d{2})[-/\.]\d{2}[-/\.](?:\d{4}|\d{2})'  # YYYY-MM-DD or DD-MM-YYYY
    r'(?:[ T:-]*\d{2}:\d{2}:\d{2})?'                     # optional time
    r'|\d{2}:\d{2}:\d{2}'                                # or time only
    r')\]?'
)

def main():
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(output_file, 'w', encoding='utf-8') as out:
        for line in lines:
            if is_system_line(line):
                continue

            clean_line = TIMESTAMP_REGEX.sub('', line).strip()
            clean_line = re.sub(r'^[A-Za-z0-9_]+:\s*', '', clean_line)

            if clean_line:
                out.write(clean_line + '\n')

if __name__ == '__main__':
    main()
