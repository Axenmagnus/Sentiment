#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 20:42:56 2022

@author: magnusaxen
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 17:28:23 2021
@author: magnusaxen
"""

# importing the library
import urllib.request
from bs4 import BeautifulSoup as soup
from newspaper import Article
from datetime import date
from DateChanger import DateChanger,CompanyChange
url="https://www.google.com/search?q=ericsson&biw=1440&bih=719&sxsrf=ALiCzsZxadn_z8_8rEjksk-Vq4mgzvngFw%3A1655816720043&source=lnt&tbs=cdr%3A1%2Ccd_min%3A9%2F15%2F2021%2Ccd_max%3A9%2F15%2F2021&tbm=nws"

drag=date(2020, 9, 15)#Instantiation #When to start article fetch
push=date(2020, 9, 16)#Instantiation
enddate=date.today()
userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"


# #gfg = BeautifulSoup(request.urlopen(initialString).read())
headers={'User-Agent':userAgent,} 
# request=urllib.request.Request(url,None,headers) #The assembled request


# response = urllib.request.urlopen(request)

# data = response.read() # The data u need



# import requests
 #Intended for easy gathering of articles for company for various dates.   

# #url = 'https://www.google.com/'
# r = requests.get(url)
# print(r.text)

def ArticleFetch(company,drag,push,url,endDate):
    url=CompanyChange(company,url)
    drag,push,url=DateChanger(drag,push,url)
    
    while drag!=endDate:
        request=urllib.request.Request(url,None,headers) #The assembled request
        response = urllib.request.urlopen(request)
        page_html=response.read()
        response.close()
        page_soup=soup(page_html,"html.parser")
        containers = page_soup.findAll("div", {"class": "xuvV6b BGxR7d"})
        
        for i in range(5):
            article=containers[i]
            container=containers[0]
            #print(container==article)
            #c=article.a
        
            contianer=container.a
            #print(container==article)
            #print(contianer)
            for a in article.find_all('a', href=True):
                print (a['href'])
                temp_url=(a['href'])
                #Here we may attain the articles.
                # download and parse article
                article = Article(temp_url)
                article.download()
                article.parse()
                 
                # print article text
                #print(article.text)
        
        drag,push,url=DateChanger(drag,push,url)
        
    
    
    return company




    
    
    






    
    