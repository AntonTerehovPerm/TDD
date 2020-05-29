#Выполнить в консоли python functional_tests.py
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://www.google.com')

assert 'Django' in browser.title