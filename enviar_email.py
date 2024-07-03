from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
import time
import os

class EnviarEmail:

    def __init__(self, url, email, title, content):
        self.url = url
        self.email = email
        self.title = title
        self.content = content
        
        self.abrir_pagina()
        self.login()

        time.sleep(10)
        self.mandar_email()
        self.fechar_pagina()

    def abrir_pagina(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)

    def login(self):
        load_dotenv("dotenv_files/.env")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.CLASS_NAME, "mectrl_topHeader"
            ))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.ID, "i0116"
            ))
        ).send_keys(
            os.getenv("EMAIL")
        )

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.ID, "idSIButton9"
            ))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.ID, "i0118"
            ))
        ).send_keys(
            os.getenv("PASSWORD")
        )

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.ID, "idSIButton9"
            ))
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((
                By.ID, "declineButton"
            ))
        ).click()

    def mandar_email(self):
        self.driver.find_element(
            By.CSS_SELECTOR, ".root-191"
        ).click()

        time.sleep(5)

        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[3]/div[1]/div/div[3]/div/div/div[1]"
        ).send_keys(self.email)

        time.sleep(5)

        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[3]/div[2]/div[2]/div/div/div/input"
        ).send_keys(self.title)

        time.sleep(5)

        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[4]/div/div/div"
        ).send_keys(self.content)

        time.sleep(5)

        self.driver.find_element(
            By.XPATH, "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/span/button[1]"
        ).click()

    def fechar_pagina(self):
        time.sleep(10)
        self.driver.close()


if __name__ == "__main__":

    title = "Esse é o meu nome"

    content = """
    Olá, 
    Meu nome é Fernando
    """

    EnviarEmail("https://outlook.com", "seuemail@gmail.com", title, content)