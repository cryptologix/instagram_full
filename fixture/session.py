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

