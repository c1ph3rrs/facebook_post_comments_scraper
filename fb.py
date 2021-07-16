from selenium import webdriver
from bs4 import BeautifulSoup
import urllib.request
import csv 
import pandas as pd
import time
from selenium.common.exceptions import NoSuchElementException  


def pages_data():


    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
    driver = webdriver.Chrome(options=options, executable_path=r'C:\Users\Ciphers\Documents\fbComments\chromedriver.exe')
    driver.get("https://m.facebook.com/Zara/photos/a.230803585906/10159165623555907/")
    # https://m.facebook.com/33331950906/posts/10159042278540907/?d=n
    # https://m.facebook.com/Zara/photos/a.230803585906/10159165623555907/

    driver.maximize_window()
    time.sleep(15)
    data = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(data, 'html.parser')

    postComment = []

    i = 0


    for i in range (100):
        time.sleep(2)
        try:

            btn = driver.find_element_by_xpath("(//a[contains(text(),'View more comments')])")
            btn.location_once_scrolled_into_view
            btn.click()
        
        except NoSuchElementException:
            print("not find")
            return


    data2 = driver.execute_script("return document.documentElement.outerHTML")
    soup2 = BeautifulSoup(data2, 'html.parser')

    for link in soup2.find_all('div', {'class' : '_2b06'}):
        

        time.sleep(1)

        


        coment_name_div = link.find('div', {'class': '_2b05'})

        comment_name = coment_name_div.text

        print(comment_name)

        comment_with_name = link.text

                
        if comment_name in comment_with_name:
            new_body = comment_with_name.replace(comment_name, "")
        else:
            new_body = comment_with_name

        print(new_body)


        print(i)
            
        i+=1
    

        postComment.append({
            'post_id' : i,
            'post_name':  comment_name,
            'post_comment' : new_body,
        })  

    return postComment

def save_data(data):
    with open('postComments.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, ['post_id', 'post_name', 'post_comment'])
        writer.writeheader()
        for row in data:
            writer.writerow(row)



# data = pages_data(category, action, city)

data = pages_data()
save_data(data)

# pages_data()