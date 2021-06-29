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
                text=''
                for i in range(len(p.text.strip())) :
                    if p.text.strip()[i]=='[':
                        break
                    else:
                        text+=p.text.strip()[i]
                if not text in all_p_has_citations:
                  all_p_has_citations.append(text)
                else: 
                    text=''
                    for i in range(len(p.text.strip())) :
                      if p.text.strip()[i]==']':
                        for j in range(i+1,len(p.text.strip())) :
                            if p.text.strip()[j]=='[':
                              break
                            else:
                                text+=p.text.strip()[j]
                        break
                    all_p_has_citations.append(text)
                                 

    return "\n\n".join(all_p_has_citations)





if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))
