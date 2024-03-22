import httpx
import bs4
from variables import status_code, prompt, check_for_loop_done, check_status_code


URL = "https://www.auto-data.net/en/results?search={search}"

def result_save_done():
    result_save.write("Output saved" + "\n") 

if __name__ == "__main__":
    result_save = open("Old_results.txt" ,"a")
    if result_save == FileNotFoundError:
        open("Old_results.txt", "a")
    prompt()
    
    search = str(input()) 
    with httpx.Client() as client:
        resp = client.get(URL.format(search=search))
        error_message = check_status_code(resp)
        if error_message:
            print("Error with collecting site code(200)!")
        if resp.status_code == status_code():
            soup = bs4.BeautifulSoup(resp.text, features="lxml")
            
            result_list = []
            
            for i in soup.find_all("span", {"class": "content"}):
                result_save.write(search + " = " + i.text + "\n")
                result_list.append(i.text)
                print(i.text)
                
            iterator = iter(result_list)
            check_for_loop_done(iterator, result_save_done())
