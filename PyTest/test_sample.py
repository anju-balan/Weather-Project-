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

    

    driver.implicitly_wait(10)
    #driver.maximize_window()

def test_webpage():
    print("Test case 1 - Check the connection")
    driver.get('http://localhost:5000/')
    print("Test case 1 Passed")
    
def test_datetime():
    print("Test case 2 - Check the timestamp element is present")
    output_str = driver.find_element_by_id("ct").text
    if output_str != "":
        print("Test case 2 Passed")

def test_location():
    print("Test case 3 - Check the location element is present")
    output_str = driver.find_element_by_id("loc").text
    if output_str != "":
        print("Test case 3 Passed")

def test_temperature():
    print("Test case 4 - Check the Temperature element is present")
    output_str = driver.find_element_by_id("temperatureCelsius").text
    if output_str != "":
        print("Test case 4 Passed")
    

def test_teardown():
    driver.close()

