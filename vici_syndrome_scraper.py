import random
from bs4 import BeautifulSoup
import requests

wiki_url = requests.get("https://en.wikipedia.org/wiki/List_of_syndromes").text
soup = BeautifulSoup(wiki_url, "html.parser")
syndromes = soup.find_all("ol")

urls = []
all_ols = soup.find_all("ol")
for li in all_ols: #test with soup.find_all("ol")
    all_a = li.find_all("a")
    for a in all_a:
        try:
            if "href" in a.attrs:
                url = a.get("href")
                urls.append(url)
        except:
            pass
#print(urls)

def gen_cindy(urls, numero=1):
    out = []
    delim = " \n"
    for i in range(numero):
        out.append("wikipedia.org/" + random.choice(urls))
    return delim.join(out)
print(gen_cindy(urls, 4))

#print(soup.li.a)
##links = soup.find_all("li a ", href=True)


# no_tags = remove_tags(syndromes)
# print(no_tags)

