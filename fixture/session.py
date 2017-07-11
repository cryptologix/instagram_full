# -*- coding: utf-8 -*-
class sessionHelper:

    def __init__(self,app):
        self.app = app

    #выход
    def logout(self):
        wd = self.app.wd

    #вход
    def login(self, username, password):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a").click()

        #логин
        wd.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[1]/input").click()
        wd.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[1]/input").send_keys(username)

        #пароль
        wd.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/input").click()
        wd.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/input").send_keys(password)

        #submit
        wd.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/span/button").click()
