# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fixture.session import sessionHelper
from fixture.like import Like


class Application:

    #инициация вебдрайвера
    def  __init__(self):
        self.wd = webdriver.Chrome("C:/chromedriver.exe")
        self.wd.implicitly_wait(60)
        self.session = sessionHelper(self)
        self.like = Like(self)

    def open_home_page(self):
        self.wd.get("https://www.instagram.com/")

    #закрытие драйвера
    def destroy(self):
        self.wd.quit()

