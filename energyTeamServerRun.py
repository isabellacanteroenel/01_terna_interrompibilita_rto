from extract_data import get_energy_team_server
from login import LoginBot
from selenium.webdriver.common.by import By
import time


names_list = get_energy_team_server()

print(get_energy_team_server)
bot = LoginBot(
    url="http://80.76.69.149:8080/datascope/login.do",
    username="mirko",
    password="energyteam"
)
bot.open_page()
bot.login()
driver = bot.driver


for name in names_list:
    try:
        print(f"Trying to click on: {name}")
        link = driver.find_element(By.NAME, name)
        link.click()
        time.sleep(2)

    except Exception as e:
        print(f"Could not click on '{name}': {e}")
        break
