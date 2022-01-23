from selenium import webdriver

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
file = open("page.txt", "w", encoding="utf-8")
driver.get("https://www.probuilds.net/teams/details/189")
file.write(driver.page_source)

file.close()