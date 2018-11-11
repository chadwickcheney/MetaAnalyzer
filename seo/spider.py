from bs4 import BeautifulSoup
import time
import requests
import fake_useragent
import lxml

class Browser:
    def __init__(self, url):
        self.url = url
        self.headers={'User-Agent':str(self.get_random_user_agent())}
        self.response=self.get_response(self.url)
        self.html=BeautifulSoup(self.response.text, 'lxml')

    def get_random_user_agent(self):
        ua = fake_useragent.UserAgent()
        return ua.random

    def get_response(self,url):
        while True:
            resp = requests.get(self.url)#, headers=self.headers)
            try:
                return resp
            except Exception as e:
                user.prompt(feed=e)
            time.sleep(2)
        user.prompt(feed=str("Response acquired successfully with "+str(self.headers)))
