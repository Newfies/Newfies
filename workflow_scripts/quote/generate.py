import random
import urllib.parse
import requests
import os

# Paths
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
readme_path = os.path.join(repo_root, "README.md")
res_dir = os.path.join(repo_root, "res")
os.makedirs(res_dir, exist_ok=True)
quote_image_path = os.path.join(res_dir, "quote.png")
quotes_file_path = os.path.join(os.path.dirname(__file__), "quotes.txt")

# Load quotes
with open(quotes_file_path, "r", encoding="utf-8") as file:
    quotes = [q.strip() for q in file if q.strip()]

# Pick a random quote
quote = random.choice(quotes)

# URL-encode the quote for APITemplate
encoded_quote = urllib.parse.quote(quote)
api_url = f"https://rest.apitemplate.io/c2977b23db95f3a0@j6p7MT5g/image.png?Quote.text={encoded_quote}"

# Download the image
response = requests.get(api_url)
if response.status_code == 200:
    with open(quote_image_path, "wb") as f:
        f.write(response.content)
else:
    raise Exception(f"Failed to fetch image: {response.status_code}")

# Build markdown for README
quote_image_md = f"![Quote](res/quote.png)\n"

# Read existing README
with open(readme_path, "r", encoding="utf-8") as file:
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

# Save updated README
with open(readme_path, "w", encoding="utf-8") as file:
    file.writelines(new_readme)

print(f"Updated quote: {quote}")
