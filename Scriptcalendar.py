import requests
from bs4 import BeautifulSoup

url = "https://www.investing.com/economic-calendar/"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

events = []
event_rows = soup.find_all("tr", class_="js-event-item")
for row in event_rows:
    event = {
        "name": row.find("td", class_="event").text.strip(),
        "date": row.find("td", class_="time").text.strip(),
        "description": row.find("td", class_="impact").text.strip()
    }
    events.append(event)

for event in events:
    print("Event:", event["name"])
    print("Date:", event["date"])
    print("Description:", event["description"])
    print("-" * 40)