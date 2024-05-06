from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

header = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,vi;q=0.8"
}
url = "https://www.amazon.com/Aroma-Housewares-ARC-363-1NGB-Uncooked-Multicooker/dp/B01BUL7FJ6/ref=sr_1_8?crid=1MVYE6L5U62WZ&dib=eyJ2IjoiMSJ9.94WaEngoRyiJ7BY6A4ciAVzOlVsczO6qUipfF1e_VrlrRqaE1zLIKMR9iJOIWpEdekUsshsh0kKGJ6cPHZHbzcs9UeyGrP1xjUddpAcHtngbE6J8SxHozDTwDYb_0cI_EF1gUiQoutgYtyt5lvODEPqsgupi88QtITwhW9nQ2pDa0C5AUZW_O_OISJ4LObEmWM6jvT_vyrTTBf5JzvS9re_BVbYVhJUd2WtDbeqPzl0.Oh10Fayx5cAx7VaAZncPhGveAEvTCg2OpNEq4YuTuz4&dib_tag=se&keywords=rice%2Bcooker&qid=1715002661&sprefix=rice%2B%2Caps%2C132&sr=8-8&th=1"
response = requests.get(url, headers=header)

yc_web_page = response.content

soup = BeautifulSoup(yc_web_page, "lxml")
whole = soup.find(name="span", class_="a-price-whole").get_text()
fraction = soup.find(name="span", class_="a-price-fraction").get_text()
price = float(whole + fraction)

if price < 20.00:
  message = f"Product is now at {price}"
  with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    result = connection.login("tranminhhien14@gmail.com", "password")
    connection.sendmail(
        from_addr="tranminhhien14@gmail.com",
        to_addrs="tranminhhien14@gmail.com",
        msg=f"Subject:Amazon Price Alert!\n\n{url}.encode(utf-8)"
    )
