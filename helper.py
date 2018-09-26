import os
import sys
currDirectory = os.path.dirname(os.path.abspath(__file__))
import re
import glob

from selenium import webdriver
import time

import json

def open_driver(browser):
    options = webdriver.ChromeOptions() 
    download_dir = currDirectory + "\\downloads"
    if not browser:
        options.add_argument("--headless")
    driver = webdriver.Chrome(currDirectory + "\\chromedriver_win32\\chromedriver.exe", chrome_options=options)
    driver.get("https://chunagon.ninjal.ac.jp/chj/search")
    
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    driver.execute("send_command", params)
    return driver

def login(driver):
    sys.stdout.write("logging in")
    
    with open(currDirectory + '\\login.json') as f:
        login_info = json.load(f)
    username = login_info['username']
    password = login_info['password']
    
    login_field = driver.find_element_by_id("username")
    login_field.send_keys(username)
    sys.stdout.write(".")
    sys.stdout.flush()
    
    password_field = driver.find_element_by_id("password")
    password_field.send_keys(password)
    sys.stdout.write(".")
    sys.stdout.flush()
    
    enter_button = driver.find_element_by_id("submit")
    enter_button.click()
    sys.stdout.write(".")
    sys.stdout.flush()
    sys.stdout.write(".")
    sys.stdout.flush()
    sys.stdout.write("logged in\n")
    sys.stdout.flush()

def move_to_search(driver):
    search_button = driver.find_element_by_id("str-search")
    entire_button = driver.find_element_by_class_name("entire-string")
    
    search_button.click()
    entire_button.click()

def search_term(driver, term):
    
    sys.stdout.write("searching" + term)
    sys.stdout.flush()
    search_bar = driver.find_element_by_name("queryString")
    search_bar.send_keys(term + '\n')
    search_over = False
    while not search_over:
        try:
            driver.find_element_by_id("table-search-result")
            search_over = True;
        except:
            time.sleep(1)
            sys.stdout.write(".")
            sys.stdout.flush()
    sys.stdout.write("search complete\n")
    sys.stdout.write("downloading")
    sys.stdout.flush()
    count_at_start = len(glob.glob1(currDirectory + "\\downloads","*.csv"))

    dwnl_buton = driver.find_element_by_class_name("btn-download")
    dwnl_buton.click()
    
    count_file_dwnl = len(glob.glob1(currDirectory + "\\downloads","*.csv"))

    while count_file_dwnl == count_at_start:
        time.sleep(1)
        sys.stdout.write(".")
        sys.stdout.flush()
        count_file_dwnl = len(glob.glob1(currDirectory + "\\downloads","*.csv"))
    sys.stdout.write("download complete\n")
    

def get_list_characters(filename):
    string = ""
    with open(filename, 'r', encoding='utf8') as f:
        for line in f:
            string += line
    return re.sub(r"\s+", "", string)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    