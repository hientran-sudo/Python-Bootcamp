from selenium import webdriver
from selenium.webdriver.common.by import By
#setting Selenium web driver
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.amazon.com/Aroma-Housewares-ARC-363-1NGB-Uncooked-Multicooker/dp/B01BUL7FJ6/ref=sr_1_8?crid=1MVYE6L5U62WZ&dib=eyJ2IjoiMSJ9.94WaEngoRyiJ7BY6A4ciAVzOlVsczO6qUipfF1e_VrlrRqaE1zLIKMR9iJOIWpEdekUsshsh0kKGJ6cPHZHbzcs9UeyGrP1xjUddpAcHtngbE6J8SxHozDTwDYb_0cI_EF1gUiQoutgYtyt5lvODEPqsgupi88QtITwhW9nQ2pDa0C5AUZW_O_OISJ4LObEmWM6jvT_vyrTTBf5JzvS9re_BVbYVhJUd2WtDbeqPzl0.Oh10Fayx5cAx7VaAZncPhGveAEvTCg2OpNEq4YuTuz4&dib_tag=se&keywords=rice%2Bcooker&qid=1715002661&sprefix=rice%2B%2Caps%2C132&sr=8-8&th=1")

price = driver.find_element(By.CLASS_NAME, value="a-price-whole")
price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price}.{price_cents}")
driver.close()
driver.quit()
