from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Like:

    def __init__(self,app):
        self.app = app

    def put_hashtag_name(self,hashtag):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div/div/span[2]").click()
        wd.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").click()
        wd.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input").send_keys(hashtag)
        wd.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div[2]/span").click()

    def open_first_image(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[1]/div/div[1]/div[1]/a/div/div[2]").click()

    def start_like(self,count):
        wd = self.app.wd
        i = 1
        for i in range(count):
            try:
                waitElement = WebDriverWait(wd, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[2]/div/article/div[2]/section[1]/a[1]/span"))
                )
                #wd.find_element_by_link_text("Нравится").click()
                wd.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/article/div[2]/section[1]/a[1]/span").click()
                wd.find_element_by_link_text("Далее").click()
                time.sleep(0.8)



            except NoSuchElementException:
                wd.find_element_by_link_text("Далее").click()
                time.sleep(0.8)