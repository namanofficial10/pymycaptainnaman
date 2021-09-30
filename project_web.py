#Project 2 : Web Scrapper Using BeautifulSoup4 and requests
from selenium import webdriver
import sqlite3

import time 

driver = webdriver.Firefox(executable_path = 'C:\\Users\\DELL\\InstaPy\\assets\\gecko\\v0.29.1\\geckodriver-v0.29.1-win64\\geckodriver.exe')

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/"

driver.get(oyo_url)

pg_n_l = driver.find_elements_by_css_selector("a.ListingPagination__pageContainer--page")



tpage = int(pg_n_l[-1].get_attribute("innerHTML"))

with open("oyo_data.csv","a") as f:
    f.write("name,address,price,rating")


for i in range(tpage):
    cpage = "https://www.oyorooms.com/hotels-in-bangalore/?page=" + str(i+1)

    driver.get(cpage)
    time.sleep(5)

    name = driver.find_elements_by_css_selector("h3.listingHotelDescription__hotelName")
    price = driver.find_elements_by_css_selector("span.listingPrice__finalPrice")
    address = driver.find_elements_by_css_selector("span.u-line--clamp-2")
    rating = driver.find_elements_by_css_selector("span.hotelRating__rating")

    
    print(len(name))
    print(len(price))
    print(len(address))
    print(len(rating))

    

    for j in range(len(name)):
        hname = name[j].get_attribute("innerHTML")
        haddress = address[j].get_attribute("innerHTML")
        try:
            hprice = "Rs." +  price[j].get_attribute("innerHTML")[1:]
        except Exception:
            hprice = "Sold Out"
        hrating = rating[j].get_attribute("innerHTML")[6:9]
        with open("oyo_data.csv","a") as f:
            try:
                f.write(f"\n {hname},{haddress},{hprice},{hrating}")
            except Exception as e:
                print(e)
    


driver.close()
