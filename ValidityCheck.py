#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 20:41:56 2022

@author: magnusaxen
"""

'''
Here specifically we assert ourself that articles contain information about the company 
in question.

We need also check the articles indeed contain sufficent information, and is in the correct
language.


'''

from langdetect import detect

from datetime import date
#url="https://www.google.com/search?q=ericsson&biw=1440&bih=719&sxsrf=ALiCzsZxadn_z8_8rEjksk-Vq4mgzvngFw%3A1655816720043&source=lnt&tbs=cdr%3A1%2Ccd_min%3A9%2F15%2F2021%2Ccd_max%3A9%2F15%2F2021&tbm=nws"

#drag=date(2020, 9, 15)#Instantiation #When to start article fetch
#push=date(2020, 9, 16)#Instantiation
##enddate=date.today()

#company="ericsson-company"


def ValidityCheck(company,text,tempurl):
    Bool=True
    
    #Checking its of sufficient size
    if len(text)<100:
        Bool=False
        
    #Making sure article actually contains information about the company
    company=company.replace("-company","")
    if company not in text:
        Bool=False
    
    #Check that the article is from their own website
    #If it is, discard it as it might be biased
    if tempurl.contains(str("www."+company)): # That is www.ericsson for instance
        Bool=False

    #Check its of the correct language
    if detect(text)!="en":
        Bool=False
    
    
    
    return Bool