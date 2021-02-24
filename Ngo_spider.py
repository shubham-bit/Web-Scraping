# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:59:01 2020

@author: kshub
"""

import scrapy 
class Ngospider(scrapy.Spider):
    name = "Ngo"
    start_urls = [
        ''
        
        
]


def parse (self, response):
    page = response.url.split('/')
    filename = 'Ngo-%s.html' % page
    with open (filename, 'wb') as f:
        f.write(response.body) 
        