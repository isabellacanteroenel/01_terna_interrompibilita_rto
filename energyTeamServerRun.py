from login import login
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = login()

for name in ["energyTeam"]:
    # Click on the "Energy Team" link
    energy_team_link = driver.find_element(By.LINK_TEXT, name)
    print(name)
    energy_team_link.click()
    time.sleep(2)  # Wait for the page to load

