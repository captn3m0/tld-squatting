from bs4 import BeautifulSoup
import re
import yaml
import csv
from math import floor,log10
import http.client

def parse_row(soup):
    table = soup.find("tbody")

    for row in table.find_all("tr"):
        if len(row.find_all("td")) < 5:
            continue
        status = row.select_one(".label").text
        tld_element = row.select_one("td:nth-child(3) a")
        tld_match = re.search(r"xn--[\w-]+", tld_element["href"])
        tld = tld_match.group() if tld_match else tld_element.text[1:]
        icon_type_mapping = {
            "fa-users": "unrestricted",
            "fa-lock": "restricted",
            "fa-registered": "brand",
            "fa-exclamation": "semi-restricted",
        }  # Add more mappings as needed
        icon_class = row.select_one(".fa")["class"][1]
        tld_type = icon_type_mapping.get(icon_class, "unknown")
        domain_count = int(
            row.select_one("td.right:nth-child(8)").text.replace(",", "")
        )
        domain_count_approx = 10**(floor(log10(domain_count)))
        owner = row.select_one("td:nth-child(5)").text.strip()
        if "Identity Digital Inc." in owner:
            owner = "Donuts"
        if "Charleston Road Registry" in owner:
            owner = "Google"
        if "Amazon Registry" in owner:
            owner = "Amazon"

        yield {
            "status": status,
            "tld": tld,
            "type": tld_type,
            "domain_count": domain_count_approx,
            "owner": owner
        }

if __name__ == "__main__":
    with open('ntld.html', 'r') as f:
        html = f.read()
    soup = BeautifulSoup(html, "html.parser")

    # Parse the response
    tlds = list(parse_row(soup))
    tlds = sorted(tlds, key=lambda x: x["tld"])
    # Write domain counts (1-10, 10-100, and so on. We note the lower count)
    with open("_data/domain_count.yml", "w") as f:
        yaml.dump({row["tld"]: row["domain_count"] for row in tlds}, f)
    # Write other tld information
    with open("_data/ntld.csv", "w") as f:
        writer = csv.DictWriter(
            f, fieldnames=["tld", "status", "type", "owner"], extrasaction="ignore"
        )
        writer.writeheader()
        for row in tlds:
            writer.writerow(row)
