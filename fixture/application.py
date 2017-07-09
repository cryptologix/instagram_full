# -*- coding: utf-8 -*-
from selenium import webdriver
from fixture.session import sessionHelper

class Application:

    #инициация вебдрайвера
    def  __init__(self):
        self.wd = webdriver.Chrome("C:/python27/chromedriver.exe")
        self.wd.implicitly_wait(60)
        self.session = sessionHelper(self)

    def open_home_page(self):
        self.wd.get("https://www.instagram.com/")

    #закрытие драйвера
    def destroy(self):
        self.wd.quit()

