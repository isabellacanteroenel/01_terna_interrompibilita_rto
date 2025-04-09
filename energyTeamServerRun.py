from extract_data import get_energy_team_server
from login import LoginBot
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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

wait = WebDriverWait(driver, 10)

for name in names_list:
    try:
        print(f"Trying to click on: {name}")
        elements = wait.until(EC.presence_of_all_elements_located(
    (By.TAG_NAME, "a")
))
        elements.click()


    except Exception as e:
        print(f"Could not click on '{name}': {e}")
        break

