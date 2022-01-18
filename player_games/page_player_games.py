from selenium import webdriver

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
file = open("page.txt", "w", encoding="utf-8")
driver.get("https://www.probuilds.net/pros/details/6416")
file.write(driver.page_source)
driver.close()
file.close()