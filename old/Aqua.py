'''
Created on Oct 14, 2017

@author: Tyler-OC
'''
from Discord_API import Discord
from Database import database
from Reddit import Reddit
import time

discord = Discord()
Data = database()
Red = Reddit()


count = 0
while True:
    Page = Red.getPage("https://www.reddit.com/r/buildapcsales/")
    Products = Red.getProducts(Page)
    
    
    
    for product in Products:
        if "[monitor]" in product.lower():
            if Data.CheckProduct(product):
                print("Product in database!")
            else:
                Data.newProduct(product)
                Message = "There is a new Product to Check out! \n" + product
                discord.sendMessage(Message)
    
    print("Waiting")
    time.sleep(60)
