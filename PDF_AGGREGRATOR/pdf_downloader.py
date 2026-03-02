import os
import requests

with open("basel_pdf_links.csv") as f:
    for line in f:
        url = line.strip()
        filename = url.split("/")[-1]
        r = requests.get(url)
        with open(os.path.join("./RAG/PDFS", filename), "wb") as out:
            out.write(r.content)