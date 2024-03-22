import httpx
import bs4
from variables import status_code, prompt


URL = "https://www.auto-data.net/en/results?search={search}"

if __name__ == "__main__":
    result_save = open("Old_results.txt" ,"a")
    if result_save == FileNotFoundError:
        open("Old_results.txt", "a")
    prompt()
    search = str(input()) 
    with httpx.Client() as client:
        resp = client.get(URL.format(search=search))
        
        if resp.status_code == status_code():
            soup = bs4.BeautifulSoup(resp.text, features="lxml")
            
            for i in soup.find_all("span", {"class": "content"}):
                result_save.write(search + " = " + i.text + "\n")
                print(i.text)
            
            result_save.write("Output saved" + "\n")
                