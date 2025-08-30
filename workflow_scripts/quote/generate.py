import random
import urllib.parse

# Load quotes
with open("quotes.txt", "r", encoding="utf-8") as file:
    quotes = [q.strip() for q in file if q.strip()]  # Remove empty lines

# Pick a random quote
quote = random.choice(quotes)

# URL-encode the quote for use in the image URL
encoded_quote = urllib.parse.quote(quote)

# Build image markdown
quote_image_md = f"![Quote](https://rest.apitemplate.io/c2977b23db95f3a0@1dn1PF3B/image.png?Quote.text={encoded_quote})\n"

# Read existing README
with open("README.md", "r", encoding="utf-8") as file:
    readme = file.readlines()

# Replace between <!--QUOTE-START--> and <!--QUOTE-END-->
new_readme = []
inside = False
for line in readme:
    if "<!--QUOTE-START-->" in line:
        inside = True
        new_readme.append(line)
        new_readme.append(quote_image_md)
    elif "<!--QUOTE-END-->" in line:
        inside = False
        new_readme.append(line)
    elif not inside:
        new_readme.append(line)

# Save README
with open("README.md", "w", encoding="utf-8") as file:
    file.writelines(new_readme)
