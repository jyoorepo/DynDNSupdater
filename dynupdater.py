'''

Auto Dyndns.org Updating Script.
Compiled by JYOO 11/21/2021.

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
from encrypt import USER_ID
from encrypt import USER_PW
# import urllib.request
# import time

driver = webdriver.Chrome()

driver.get('https://dyndns.org')

# Log user's info into the proper inputs.
userName = driver.find_element(By.NAME, 'username')
userName.send_keys(USER_ID)

password = driver.find_element(By.NAME, 'password')
password.send_keys(USER_PW)

driver.find_element(By.NAME, 'submit').click()

# Find clients profile by text search.
driver.find_element(By.LINK_TEXT, 'pythontest.dvrdns.org').click()

# This calls for public WAN IP to compare with clients profile.
#externalIp = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')

# Finds the IP that's currently registered on clients profile.
#dynIp = driver.find_element(By.NAME, 'cur_ip')

# dynIp.send_keys(externalIp)

driver.find_element(By.ID, 'a_clone').click()

# time.sleep(1)

driver.find_element(By.NAME, 'submit').click()
