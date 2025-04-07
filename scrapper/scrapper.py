import requests
from bs4 import BeautifulSoup

def webscrap(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to Scrap. Status code: {response.status_code}")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')


    headings = soup.find_all('h2')
    for heading in headings:
        print(heading.get_text())


if __name__ == "__main__":
    url = input("Enter your URL:",)
    webscrap(url)