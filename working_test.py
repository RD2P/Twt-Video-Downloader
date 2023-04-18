from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from time import sleep
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.opera.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import os
import requests
import tkinter as tk
from tkinter import simpledialog

#Pop up asking for the link
root = tk.Tk()
root.withdraw()
user_input = simpledialog.askstring("Link", "Please enter the link:")
print(user_input)

# Instantiate the webdriver with the executable location of MS Edge web driver
browser = webdriver.Edge("C:\Program Files (x86)\msedgedriver.exe")
browser.maximize_window()
browser.get('https://twittervideodownloader.com/')
# Find the element by ID or other locator
input_field = browser.find_element_by_name("tweet")
#send link input by user into input field on browser
input_field.send_keys(user_input)
submit_button = browser.find_element_by_class_name("button")
submit_button.click()

#time.sleep(3)
#Search for download button
download_button = browser.find_element_by_link_text("Download Video")
download_button.click()

#DOWNLOAD
# the URL of the video file to download
url = browser.current_url

current_dir = os.getcwd()
file_path = os.path.join(current_dir + "\Downloads", "video.mp4")

# send a GET request to the URL
response = requests.get(url)
# check if the request was successful
if response.status_code == 200:
    # the request was successful, so save the video file
    with open(file_path, "wb") as f:
        f.write(response.content)
    print("Video downloaded successfully!")
else:
    # the request failed, so print the error message
    print(f"Error downloading video: {response.status_code} {response.reason}")

browser.quit()

downloads_path = os.path.expanduser(r"C:\Users\radit\Desktop\Python Practice\twt-vid-downloader\Downloads")
os.startfile(downloads_path)

    
    