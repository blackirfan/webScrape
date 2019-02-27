from bs4 import BeautifulSoup
import requests
import json

def crawl_kompas(url):
    
    result = []
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    
    #find paging page 
    paging = soup.find_all("div",{'class':'bot-prevnext-results'})
    paging_link = paging[0].find_all('a',{'class':'botNext-results'})
    last_page = int([item.get('href').split('/')[-1] for item in paging_link][-1])

    #looping through paging
    for i in range(1,last_page):
        print(url+str(i)) 
        for div in soup.findAll('div', attrs={'class':'listing-address'}):
                print(div.find('a').contents[0])

        print("\n\n\n")

        print("this land location\n\n\n")

            # land location


        for div in soup.findAll('div', attrs={'class':'listing-address'}):
                # print(div.find('a')['href'])
                print(div.contents[0])



        print("\n\n\n")

        print("this land Area\n\n\n")


        for div in soup.findAll('p', attrs={'class':'listingAcres'}):
                
                print(div.contents[0])
                 # print(div.find('a')['href'])




        print("\n\n\n")

        print("this land Price\n\n\n")


        for div in soup.findAll('p', attrs={'class':'listingPrice'}):
                # print(div.find('a')['href'])
                print(div.contents[0])



        print("\n\n\n")

            #wrap in dictionary 
        news_dict['id']=idx
        news_dict['url'] = url_news
        news_dict['title'] = title_news
        news_dict['content'] = news_content
        result.append(news_dict)
         
    return result

url = 'https://www.landandfarm.com/search/AL/Barbour-County-land-for-sale/'
crawl  = crawl_kompas(url)
# with open("kompas.json","w") as f:
#     json.dump(crawl,f)