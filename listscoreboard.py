import requests
import bs4
import json

url = 'https://www.espn.com/soccer/team/stats/_/id/359'
r = requests.get(url)
soup = bs4.BeautifulSoup(r.text, 'lxml')

table = soup.find("table", class_="Table")
rows = table.find_all(class_=["Table__TBODY", "Table__THEAD"])

# print(rows)

rows = iter(rows)
header_1 = [td.text for td in next(rows).find_all('td') if td.text]
header_2 = [td.text for td in next(rows).find_all('td') if td.text]
header = header_1[:2] + header_2 + header_1[-2:]
# print(header)
for row in rows:
    print(row)
    data = [td.text for td in row.find_all('td') if td.text]
    json.dumps(data)
