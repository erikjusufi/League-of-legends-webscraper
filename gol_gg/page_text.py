from selenium import webdriver

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
file = open("gol_gg_text.txt", "w", encoding="utf-8")
driver.get("https://gol.gg/teams/list/season-S12/split-Spring/tournament-ALL/")
file.write(driver.page_source)
driver.close()
file.close()