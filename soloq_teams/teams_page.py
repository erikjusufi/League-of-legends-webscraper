from selenium import webdriver

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
file = open("page_probuilds_teams.txt", "w", encoding="utf-8")
driver.get("https://www.probuilds.net/teams")
file.write(driver.page_source)
driver.close()
file.close()