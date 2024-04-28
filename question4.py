import re

def convert_price_format(description):

    price_pattern = r'\b(\d+(\.\d{1,2})?)\b'
    
    replacement_format = 'USD \\1'
    
    standardized_description = re.sub(price_pattern, replacement_format, description)
    
    return standardized_description

descriptions = [
    "Smartphone with a price of $599.99 and 128GB memory",
    "Cotton t-shirt at 25.50 dollars in medium size",
    "Stainless steel kitchen knife set for 49.95 USD"
]

for description in descriptions:
    standardized_description = convert_price_format(description)
    print("Original description:", description)
    print("Standardized description:", standardized_description)
    print()
