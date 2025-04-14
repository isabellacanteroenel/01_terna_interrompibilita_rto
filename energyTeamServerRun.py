from extract_data import get_energy_team_server
from login import LoginBot
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Step 1: Setup
names_list = get_energy_team_server()
print("Names to match:", names_list)

bot = LoginBot(
    url="http://80.76.69.149:8080/datascope/login.do",
    username="mirko",
    password="energyteam"
)
bot.open_page()
bot.login()

driver = bot.driver
wait = WebDriverWait(driver, 15)

# Step 2: Wait a bit after login
time.sleep(2)

# Step 3: Switch to new window if it opened
original_window = driver.current_window_handle
for handle in driver.window_handles:
    if handle != original_window:
        driver.switch_to.window(handle)
        break

# Step 4: List all frames (iframe + frame)
frames = driver.find_elements(By.TAG_NAME, "iframe") + driver.find_elements(By.TAG_NAME, "frame")
print("🔍 Found total frames:", len(frames))

# Step 5: Try switching to each frame to find the image
found = False
for index, frame in enumerate(frames):
    driver.switch_to.default_content()  # Reset before switching
    print(f"➡️ Trying frame #{index}...")

    try:
        driver.switch_to.frame(frame)

        # Optional: wait for dtree to appear in the frame
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dtree")))

        # Try to find the target image inside the frame
        img = driver.find_element(By.ID, "jd129")
        print(f"✅ Found image with ID 'jd129' inside frame #{index}")
        print("src:", img.get_attribute("src"))
        print("outerHTML:", img.get_attribute("outerHTML"))
        found = True
        break

    except Exception as e:
        print(f"❌ Not found in frame #{index}: {e}")
        continue

if not found:
    print("🚫 jd129 not found in any frame.")
