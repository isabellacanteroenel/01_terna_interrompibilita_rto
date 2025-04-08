from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class LoginBot:
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def open_page(self):
        self.driver.get(self.url)
        print(f"Página carregada: {self.driver.title}")

    def login():
        user_element = driver.find_element(By.NAME, "userName")
        pass_element = driver.find_element(By.NAME, "password")

        user_element.send_keys(username)
        pass_element.send_keys(password)

        login_button = self.driver.find_element(By.CLASS_NAME, "cal_butt")
        login_button.click()
        print("Login enviado.")
        return driver

    def close_browser(self):
        self.driver.quit()



if __name__ == "__main__":
    bot = LoginBot(
        url="http://80.76.69.149:8080/datascope/login.do;jsessionid=0CF37BF03D85A016942848535F51483D",
        username="mirko",
        password="energyteam"
    )

    bot.open_page()
    bot.login()
    # bot.close_browser() 