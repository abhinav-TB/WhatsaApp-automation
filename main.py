# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from selenium import webdriver


# %%
browser=webdriver.Chrome('./chromedriver')

# %% [markdown]
# # sending messages to target

# %%
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# %%
browser=webdriver.Chrome('./chromedriver')
browser.get("https://web.whatsapp.com/")
wait=WebDriverWait(browser,600)
target='"Abhinav"'
string="message from bot"
X_arg ='//span[contains(@title, '+target+')]'
target=wait.until(ec.presence_of_element_located((By.XPATH,X_arg)))
target.click()


# %%
target='"Abhinav"'
string="message from bot"
X_arg ='//span[contains(@title,'+target+')]'
target=wait.until(ec.presence_of_element_located((By.XPATH,X_arg)))
target.click()


# %%
input_box=browser.find_element_by_class_name('_1Plpp')

for i in range(5):
    input_box.send_keys(string+Keys.ENTER)


# %%


