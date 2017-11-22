from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
keywords=["ceo","CTO","founder","co founder","owner"]
driver = webdriver.Chrome(executable_path='/Users/allu/Desktop/selenium_drivers/chromedriver')
driver.get('https://www.linkedin.com/')
username = driver.find_element_by_id("login-email")
password = driver.find_element_by_id("login-password")
def connector():
    connect_list = driver.find_elements_by_class_name("button-secondary-medium")
    for list_item in connect_list:
        try:
            if(list_item.text == "Connect"):
                list_item.click()
                send_now_butt = driver.find_element_by_class_name("button-primary-large")
                send_now_butt.click()
                #print(list_item.text)
                time.sleep(1)
        except:
            print("fata fata re phata. Phir se phata re!")
            #print(list_item.text)
            time.sleep(1)
    print("Done")

username.send_keys("YOUR EMAIL ID HERE!")
password.send_keys("YOUR PASSWORD HERE!")
driver.find_element_by_id("login-submit").click()
for page_number in range(1,200):
    search_url = "https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22us%3A0%22%2C%22gb%3A0%22%2C%22us%3A84%22%2C%22au%3A0%22%2C%22ae%3A0%22%2C%22dz%3A0%22%2C%22dz%3A9337%22%5D&facetNetwork=%5B%22F%22%2C%22S%22%2C%22O%22%5D&keywords="+keywords[2]+"&origin=FACETED_SEARCH&page="+str(page_number)
    driver.get(search_url)
    for i in range(1,4):
        if(i==1):
            driver.execute_script("window.scrollTo(0, 0);")
            connector()
        else:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight/"+str(4-i)+");")
            connector()
    print("Page "+str(page_number)+" done.")


driver.quit()
