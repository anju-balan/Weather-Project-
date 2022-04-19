# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 00:16:05 2022

@author: Karthik Mohan
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_setup():
    global driver 
    options = Options()
    options.add_argument("--headless")
    
    
    

    driver = webdriver.Chrome(executable_path='/home/travis/virtualenv/python3.8.13/chromedriver',chrome_options=options)

    
    #driver.maximize_window()

def test_webpage():
    print("Test case 1 - Check the connection")
    driver.get('http://ec2-3-14-146-73.us-east-2.compute.amazonaws.com:5000/')
    print("Test case 1 Passed")


def test_teardown():
    driver.close()

