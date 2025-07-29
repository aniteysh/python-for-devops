import re

sample_text = """
Contact us at support@example.com or sales@company.org.
Call 123-456-7890 or (555) 123-4567 for assistance.
This is an urgent request, please respond ASAP.
Normal message here.
Another urgent issue: email urgent@help.com or call 999-888-7777.
"""

def extract(sample_text):
    valid_email_addresses = re.findall(r'[a-zA-Z0-9_+.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', sample_text)
#   How it works:
#   [a-zA-Z0-9_.+-]+ matches the username part (letters, numbers, and some symbols).
#   @ is the literal at symbol.
#   [a-zA-Z0-9-]+ matches the domain name.
#   \. is a literal dot.
#   [a-zA-Z0-9-.]+ matches the domain extension.
    valid_phone_number = re.findall(r'\b(?:\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})\b', sample_text)
#   How it works:
#   \d{3}-\d{3}-\d{4} matches numbers like 123-456-7890.
#   \(\d{3}\) \d{3}-\d{4} matches numbers like (555) 123-4567.
#   (?: ... ) is a non-capturing group to combine both patterns.
#   \b ensures word boundaries (so we don’t match inside other words).    
    lines_containing_urgent = ""
    each_line = sample_text.splitlines()
    for line in each_line:
        if r'urgent' in line:
            lines_containing_urgent += line+"\n"

    return lines_containing_urgent


print(extract(sample_text))
