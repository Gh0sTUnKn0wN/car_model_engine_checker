import httpx
import bs4
from variables import status_code, prompt


URL = "https://www.auto-data.net/en/results?search={search}"

if __name__ == "__main__":
    prompt()
    search = str(input()) 
    with httpx.Client() as client:
        resp = client.get(URL.format(search=search))
        
        if resp.status_code == 200:
            soup = bs4.BeautifulSoup(resp.text, features="lxml")
            
            for i in soup.find_all("span", {"class": "content"}):
                print(i.text)
                