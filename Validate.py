import re

email = input("What's your email ? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|gov|net|ac|kmitl|th)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")