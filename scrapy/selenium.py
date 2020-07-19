import requests

from selenium.webdriver.chrome.webdriver import WebDriver
from bs4 import BeautifulSoup


class SeleniumModule():

    def __init__(self):
        self.selenium = WebDriver(executable_path='Chromeドライバのパス')

    def quit(self):
        self.selenium.quit()

    def login(self, login_url):
        self.selenium.get(login_url)
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('username')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('password')
        self.selenium.find_element_by_class_name('btn').click()

    def get_page_data(self, url, tag, attribute):
        res = requests.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        # example
        # soup.find_all('a', {'class': 'r'})
        link_list = soup.find_all(tag, attribute)
        return link_list
