from selenium import webdriver
from selenium.webdriver.common.by import By
import time

get = webdriver.Edge()


get.get("file:///C:/Users/King_Abdul/Music/Qari Abu Bakr al-Shatri")

get.find_element(By.LINK_TEXT, "010056.mp3")
time.sleep(300)
