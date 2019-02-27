from bs4 import BeautifulSoup


def read_file():
    file = open('test.html')
    data = file.read()
    file.close()
    return data

soup = BeautifulSoup(read_file(),'lxml')


# example  -- direct


# print(soup.get_text())
# print(soup.find_all("div", class_="listing-address"))





# toup = soup.find_all("div", class_="listing-address")

# for tp in toup.find_all('a'):
# 	print(tp.find_all("a", class_="actionLinkClient"))


# land owner

for div in soup.findAll('div', attrs={'class':'listing-address'}):
    # print(div.find('a')['href'])
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
    # print(div.find('a')['href'])
    print(div.contents[0])




print("\n\n\n")

print("this land Price\n\n\n")


for div in soup.findAll('p', attrs={'class':'listingPrice'}):
    # print(div.find('a')['href'])
    print(div.contents[0])



print("\n\n\n")









