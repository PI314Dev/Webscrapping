"""
Webscrape les descriptions allociné
La recherche s'est arretée à la page 20 inclus donc il faut reprendre à la page 21 pour les deux
en modifiant le range(1, 20) en mettent range(21, 30) par exemple


"""
import requests
from bs4 import BeautifulSoup

from time import sleep

import csv
#from scraper_page import scrape_page
import random

from time import sleep

def scrape_allocine(url):
    response = requests.get(
        url=url,
    )
    
    print(url)
	
    soup = BeautifulSoup(response.content, 'html.parser')
    titles=soup.find_all("a", {"class": "meta-title-link"})
    
    descriptions=soup.find_all('div', {'class':'synopsis'})
    descriptions_result=[]
    titles_result=[]
    
    for title in titles:
        titles_result.append(title.text)
    
    for description in descriptions:
        descriptions_result.append(description.find("div").text)
        
    return titles_result, descriptions_result


for k in range(51, 100):  
    
#https://www.allocine.fr/films/genre-13024/?page=2    films romance  
#https://www.allocine.fr/films/genre-13025/?page=2    films action 


    if k%10==0:
        sleep(60)
    
    titles, descriptions=scrape_allocine("https://www.allocine.fr/films/genre-13025/?page="+str(k))
    
    with open('descriptions_action.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        for i in range(len(descriptions)):
            writer.writerow([titles[i], descriptions[i]])
            
        random_time=random.randint(1, 5)
        print(random_time)
        
        sleep(5+random_time)
