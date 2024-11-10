from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Kanggoautomationtest:
    def __init__(self):
        self.driver= webdriver.Chrome()
        self.driver.maximize_window()
        self.url = 'https://www.kanggo.id/'

    def buka_browser(self):
        self.driver.get(self.url)
        time.sleep(2)

    def konsumen (self):
        button_selengkapnya = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
            (By. XPATH,"//*[@id='__next']/div[1]/div/div/main/div/div/section[2]/div[5]/div[1]/div[3]/button")
            )
        )
        button_selengkapnya.click()
        time.sleep(3)

        button_detail = "//*[@id='__next']/div[1]/div/div/main/div/div/section[2]/div[5]/div[1]/div[1]/a"
        self.driver.find_element(By.XPATH,button_detail).click()
        time.sleep(3)

    def layanan (self):
        button_layanan = WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(
            (By.XPATH,"//*[@id='__next']/div[1]/div/div/main/div/div/section[1]/div[6]/button")
            )
        )
        button_layanan.click()
        time.sleep(5)

    def menu_bangunan (self):
        button_bangunan = self.driver.find_element(By.XPATH,"//*[@id='headlessui-menu-button-:R2l36:']")
        button_bangunan.click()
        time.sleep(3)

    def perusahaan (self):
        button_perusahaan = self.driver.find_element(By.XPATH, "//*[@id='headlessui-menu-items-:R4l36:']/div[1]/a[2]/span")
        button_perusahaan.click()
        time.sleep(3)

    def jagoan (self):
        button_jagoan = self.driver.find_element(By.XPATH,"//*[@id='headlessui-menu-items-:R4l36:']/div[1]/a[3]/span")
        button_jagoan.click()
        time.sleep(3)

    def tutup_browser (self):
        self.driver.quit()

if __name__=="__main__":
    test = Kanggoautomationtest ()
    test.buka_browser()
    test.konsumen()
    test.layanan()
    test.menu_bangunan()
    test.perusahaan()
    test.menu_bangunan()
    test.jagoan()
    test.tutup_browser()