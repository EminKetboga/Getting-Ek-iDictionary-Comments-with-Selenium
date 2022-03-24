from selenium import webdriver
import random
import time

browser = webdriver.Firefox()

url = "https://eksisozluk.com/mustafa-kemal-ataturk--34712?p="
pageCount = 1
liste = []
yazı_sayısı = 1
while pageCount <= 3:
    randomPage = random.randint(1,2267)
    newUrl = url + str(randomPage)
    browser.get(newUrl)

    elements = browser.find_elements_by_css_selector('.content')
    for elemet in elements:
        liste.append(elemet.text)

    pageCount += 1
    time.sleep(10)

with open("100 İnsanın Atatürk Hakkında Düşüncler.txt","w",encoding = "UTF-8") as file:
    for i in liste:
        file.write(str(yazı_sayısı) + ". İnsan ------------------------------------------" + "\n")
        file.write(i + "\n")
        yazı_sayısı += 1
browser.close()


