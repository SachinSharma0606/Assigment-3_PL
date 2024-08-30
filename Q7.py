import re
from collections import defaultdict

def extract_emails(file_path):
    email_pattern = r'^[a-zA-Z0-9_.+$%-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$'
    email_regex = re.compile(email_pattern)

    # Initialize a defaultdict to store usernames by domain
    domain_usernames = defaultdict(list)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if email_regex.fullmatch(line):
                    username, domain = line.split('@', 1)
                    domain_usernames[domain].append(username)
                else:
                    print(f"Invalid email format: {line}")
    
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    return dict(domain_usernames)

file_path = 'C:\\Users\\acer\\Desktop\\Programs\\Assignment-3PL\\E_mail_dataset.txt'
email_domains = extract_emails(file_path)

if email_domains:
    print(email_domains)