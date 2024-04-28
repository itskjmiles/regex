import re

def extract_value(text, key):
    pattern = r'\b{}:\s*([^;]+)'.format(key)

    match = re.search(pattern, text)

    if match:
        return match.group(1)
    else:
        return None

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"

occupation = extract_value(text, "Occupation")

if occupation:
    print("Occupation:", occupation)
else:
    print("Occupation not found")
