from flask import render_template, redirect, url_for, jsonify, request
from project import app

from urllib.error import URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pickle
import sys
sys.setrecursionlimit(10000)

#to save object in file
def saveObject(name,Object):
    name = str(name) + '.pkl'
    with open(name, 'wb') as f:
        pickle.dump(Object, f, pickle.HIGHEST_PROTOCOL)
#to load object with run code again
def loadObject(name):
    name = str(name) + '.pkl'
    with open(name, 'rb') as f:
        return pickle.load(f)               



#get all categories
def caeateCategories():
    categories = []
    url = "https://www.gsmarena.com/makers.php3"
    try:
        html = urlopen(url)
    except URLError as e:
            print(e.reason)
    soup = BeautifulSoup(html, 'lxml')
    outDiv = soup.find("div", {"class", "st-text"})
    all_links = outDiv.find_all("td")
    for link in all_links: 
        sub = link.find("a").get("href")
        url = "https://www.gsmarena.com/" + str(sub)  # category link
        category = ''.join([i for i in link.text[0:-8] if not i.isdigit()])  # file name
        print(category)
        categories.append({'url':url,'category':category})
    return categories

#get links for phone for its data
def phones(categories):
    categories_phone=[]
    for link in categories:
        try:
            phones = urlopen(link['url'])
            soupPhones = BeautifulSoup(phones, 'lxml')
            divPhones = soupPhones.find("div", {"class", "makers"})
            try:
              ulPhones=divPhones.find("ul")
            except AttributeError:
              continue
            phone_links = ulPhones.find_all("li")
            
            navDiv = soupPhones.find("div", {"class": "nav-pages"})
            if navDiv:
                AnotherPages = navDiv.find_all("a")
                for page in AnotherPages:
                    url = "https://www.gsmarena.com/" + str(page.get('href'))
                    print(url)
                    try:
                      Morephones = urlopen(url)
                      MoresoupPhones = BeautifulSoup(Morephones, 'lxml')
                      MoredivPhones = MoresoupPhones.find("div", {"class", "makers"})
                      try:
                        MoreulPhones=MoredivPhones.find("ul")
                      except AttributeError:
                        continue
                      Morephone_links = MoreulPhones.find_all("li")
                      for i in Morephone_links:
                          phone_links.append(i)
                    except :
                          continue
            tempArr=[]  
            for Phone_link in phone_links:
                Name=Phone_link.find("a").find('strong').find('span').string
                tempArr.append({'phoneName':Name})
            categories_phone.append({'category':link['category'],'phones':tempArr})
        except URLError as e:
            print(e.reason)
    return categories_phone




@app.route('/updateDB', methods=['GET'])
def updateDB():
    #categories = []
    categories = caeateCategories()
    #saveObject('categories',categories)
    #categories=loadObject('categories') 

    #categories_phone=[]
    categories_phone=phones(categories)
    #saveObject('categories_phone',categories_phone)
    #categories_phone=loadObject('categories_phone') 
    MobileInfo=[]

    from fonAPI import FonApi
    #key= '8b92be9f8d69b3494dafd73bddfbef61138a79982833eabc'
    fon = FonApi("8b92be9f8d69b3494dafd73bddfbef61138a79982833eabc")
    for category in categories_phone:
        for phone in category['phones']:
            device = phone['phoneName']           	
            phonesData = fon.getdevice(device)
            try:
                MobileInfo.append(phonesData)
            except:
                print (phonesData)
    
    

