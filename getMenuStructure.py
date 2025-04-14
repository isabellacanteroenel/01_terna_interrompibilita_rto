from extract_data import get_energy_team_server
from login import LoginBot
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Step 1: Login
bot = LoginBot(
    url="http://80.76.69.149:8080/datascope/login.do",
    username="mirko",
    password="energyteam"
)
bot.open_page()
bot.login()
driver = bot.driver
wait = WebDriverWait(driver, 15)

time.sleep(2)
original_window = driver.current_window_handle
for handle in driver.window_handles:
    if handle != original_window:
        driver.switch_to.window(handle)
        break

frames = driver.find_elements(By.TAG_NAME, "iframe") + driver.find_elements(By.TAG_NAME, "frame")
for frame in frames:
    driver.switch_to.default_content()
    try:
        driver.switch_to.frame(frame)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dtree")))
        break
    except:
        continue


dtree = driver.find_element(By.CLASS_NAME, "dtree")


labels = dtree.find_elements(By.XPATH, ".//a")

tree_list = []

for label in labels:
    text = label.text.strip()
    if text:
        tree_list.append(text)


print("\n Tree Structure:")
for i, item in enumerate(tree_list, 1):
    print(f"{i}. {item}")


