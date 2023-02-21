import requests as re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t


states = [
    "Edo", 'Akwa Ibom', 'Cross River',
    "Delta", 'Ondo', 'Ogun',
    'Lagos', 'Osun', "Ekiti",
    'Oyo', 'Kogi', 'kwara',
    'Kaduna', 'Taraba', 'Benue',
    'Imo', 'Abia'
]

# for i in states:
edge = webdriver.Edge()
edge.get("https://www.abujagalleria.com/Results.html?cx=partner-pub-7086333065234471%3Adp36oruqja1&cof=FORID%3A10&ie=UTF-8&q=Oyo+State+Abuja+liaison+office&sa=Search+AbujaGalleria%21&siteurl=www.abujagalleria.com%2FAgencies_and_Organizations%2FState_Liaison_Offices3.html&ref=www.abujagalleria.com%2FAgencies_and_Organizations%2FState_Liaison_Offices2.html&ss=16528j123327920j8")
loo = edge.find_element(By.ID, 'gs_cb50')
loo.click()
obj = edge.find_element(By.ID, 'gsc-i-id1')
obj.click()
obj.send_keys(f"Lagos State Abuja liaison office")
fin = edge.find_element(By.TAG_NAME, 'button')
fin.click()
t.sleep(10)
com = edge.find_element(By.ID, "___gcse_1")
edge.fullscreen_window()
com.screenshot(f"Lagos.png")

edge.quit()
