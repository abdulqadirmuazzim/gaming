from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

dri = webdriver.Chrome()
dri.get("https://selectorshub.com")
dri.find_element(By.LINK_TEXT, 'Chrome').click()

# try:
#     element = WebDriverWait(dri, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
#     )
# finally:
#     dri.quit()
