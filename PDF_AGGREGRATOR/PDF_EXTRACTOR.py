import requests
from bs4 import BeautifulSoup

MASTER_URL = "https://www.rbi.org.in/commonman/English/scripts/MasterCircular.aspx"
resp = requests.get(MASTER_URL)
soup = BeautifulSoup(resp.text, "html.parser")

pdf_links = []
for link in soup.select("a"):
    href = link.get("href", "")
    if href.lower().endswith(".pdf"):
        pdf_links.append(href)

with open("basel_pdf_links.csv", "w") as f:
    for url in pdf_links:
        f.write(url + "\n")