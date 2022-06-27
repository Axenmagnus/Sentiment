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

from spacy_langdetect import LanguageDetector
from WebbsScrape import ArticleFetch
from datetime import date
url="https://www.google.com/search?q=ericsson&biw=1440&bih=719&sxsrf=ALiCzsZxadn_z8_8rEjksk-Vq4mgzvngFw%3A1655816720043&source=lnt&tbs=cdr%3A1%2Ccd_min%3A9%2F15%2F2021%2Ccd_max%3A9%2F15%2F2021&tbm=nws"

drag=date(2020, 9, 15)#Instantiation #When to start article fetch
push=date(2020, 9, 16)#Instantiation
enddate=date.today()

company="ericsson-company"
ArticleFetch(company,drag,push,url,enddate)

def ValidityCheck(company,text):
    Bool=True
    
    if len(text)<100:
        Bool=False
        #Making sure article actually contains information
    company=company.replace("company","")
    if company not in text:
        Bool=False
    
    
    
    
    return Bool