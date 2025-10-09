import re
import os

EMAIL_REGEX = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
PHONE_REGEX = r'\+?\d[\d -]{8,}\d'

raw_file = 'MiniPythonProjects/Email_and_Phone_Extractor/fake_contacts_with_text.txt'
output_file = 'MiniPythonProjects/Email_and_Phone_Extractor/extracted_contacts.txt'

def extract_emails_and_phones(text: str) -> tuple[list[str], list[str]]:
    try:
        emails: list[str] = re.findall(EMAIL_REGEX, text)
        phones: list[str] = re.findall(PHONE_REGEX, text)
        return emails, phones
    except re.error as e:
        print(f"Regex error: {e}")
        return [], []

def main():
    #----File Handling----
    if not os.path.exists(raw_file):
        print(f"Input file {raw_file} does not exist.")
        return

    try:
        with open(raw_file, 'r') as file:
            text = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return
        
    #----Extraction----
    emails, phones = extract_emails_and_phones(text)
    all_contacts = sorted(set(e.strip() for e in emails + phones if e.strip()))
    
    if not all_contacts:
        print("No contacts found.")
        return
    
    #----fIle Writing----
    try:
        with open(output_file, 'w') as file:
            file.write('\n'.join(all_contacts))
    except Exception as e:
        print(f"Error writing to file: {e}")
        return
        
    print(f'Extracted {len(all_contacts)} unique contacts to {output_file}')

if __name__ == '__main__':
    main()
