import requests
from bs4 import BeautifulSoup





def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_results = soup.findAll('a',title='Wikipedia:Citation needed')
    return len(all_results)

def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_p = soup.findAll('p')
    all_p_has_citations=[]
    for p in all_p:
        has_citations =p.findAll('a',title='Wikipedia:Citation needed')
        if len(has_citations)>0:
            for i in has_citations:
                all_p_has_citations.append(p.text.strip()) 

    return "\n\n".join(all_p_has_citations)





if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))
