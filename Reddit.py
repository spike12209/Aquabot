'''
Created on Oct 14, 2017

@author: Tyler-OC
'''
from bs4 import BeautifulSoup
import requests
import re
import time

class Reddit:
    
    products_url = "https://www.reddit.com/r/buildapcsales/"
    
    def getPage(self, url):
        request = None
        while True:
            request = requests.get(url)
            if request.status_code == 200:
                break
            else:
                print("Failed Response!")
            time.sleep(1)
        soup = BeautifulSoup(request.text, 'html.parser')
        return soup
    
    def getProducts(self, soup):
        div = soup.find("div", {"class" : "sitetable linklisting"})
        things = div.find_all("div", class_=re.compile(" thing"))
        products = {}
        for thing in things:
            product = thing.find("p", {"class" : "title"})
            url = product.find("a", {"class" : "title may-blank outbound"})
            product = product.getText()
            if url:
                url = url["href"]
                products[product] = url
        return products