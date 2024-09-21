from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import smtplib
import driver
import chromedriver_autoinstaller
from email.message import EmailMessage

def emailAlert():
    user = "boris.atan.dev@gmail.com"
    password = "zsyh oqig vtyg hqwz" # app password
    content = "Излязъл e спорта и/или чуждите езици."

    server = smtplib.SMTP("smtp@gmail.com", 50000)
    server.starttls()

    server.login(user, password)
    server.sendmail(user, user, content)
    # "yavor.atanassov1@gmail.com"
    

def websiteMan():
    # url to open and initializing web driver
    url = "https://deos.mu-sofia.bg/"
    chromedriver_autoinstaller.install()

    options = webdriver.ChromeOptions()
    service = Service()

    options.add_argument("headless")
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    # finding all items with the sub-menu class tag and all list items within them
    menus = driver.find_elements(By.CLASS_NAME, "sub-menu")
    listItems = []
    for i in menus:
        listItems += i.find_elements(By.TAG_NAME, "li")
    # listItems - all list items within these unordered lists
    return len(listItems)



if __name__ == "__main__":
    amountOfLinks = websiteMan()
    emailAlert()


# TODO check amount != 70
# 