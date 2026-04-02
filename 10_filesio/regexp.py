import re

# Example string
text = "Contact us at support@example.com or sales@example.org."

# Regular expression pattern for email addresses
pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# Find all matches
emails = re.findall(pattern, text)

print(emails)  # Output:
