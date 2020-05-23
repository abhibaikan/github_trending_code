# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:05:13 2020

@author: ab
"""

import requests
from bs4 import BeautifulSoup as bs
import pprint

url=input("enter github url:" )

def get_trending_repo():
    
    r = requests.get(url)
    
    if r.status_code != 200:
        print("error")

    
    html_content = r.content
    
    dom = bs(html_content, 'html.parser')
    
    t_repo=dom.select('article.Box-row h1')
    
    trending_repo=[]
    
    for  i in t_repo:
        href_link=i.a.attrs["href"]
        repo = {"label": href_link,
                 "link" :"https://github.com{}".format(href_link) }
        trending_repo.append(repo)
    return trending_repo
        

if __name__ == '__main__':
    print("scriping started")
    rps=get_trending_repo()
    pprint.pprint(rps)

    