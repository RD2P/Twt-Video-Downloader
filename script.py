from selenium import webdriver
import os
import requests
import tkinter as tk
from tkinter import simpledialog
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Pop up asking for the link
root = tk.Tk()
root.withdraw()

# Paste link of twitter video in the pop up
user_input = simpledialog.askstring("Link", "Please enter the link:")

# Instantiate the webdriver
browser = webdriver.Edge("C:\Program Files (x86)\msedgedriver.exe")

# Use third party video downloader
browser.get('https://twittervideodownloader.com/')

# Grab the input box element (it has name "tweet")
input_field = browser.find_element_by_name("tweet")

# Send link input by user into input field on browser
input_field.send_keys(user_input)

# Find and click the "Download" button
submit_button = browser.find_element_by_class_name("button")
submit_button.click()

# Search for and click another download button
download_button = browser.find_element_by_link_text("Download Video")
wait = WebDriverWait(browser, 5)  # Wait up to 5 seconds
download_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Download Video")))
download_button.click()

# DOWNLOAD
# the URL of the video file to download
url = browser.current_url

# Get current dir
current_dir = os.getcwd()

# Specify video download location
file_path = os.path.join(current_dir + "\Downloads", "video.mp4")

# send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
# If successful, open the specified download location and write the video as binary data in it
if response.status_code == 200:
    with open(file_path, "wb") as f:
        f.write(response.content)
    print("Video downloaded successfully!")
else:
    print(f"Error downloading video: {response.status_code} {response.reason}")

browser.quit()


# Open downloads folder to view downloaded video
downloads_path = os.path.join(current_dir, "Downloads")
os.startfile(downloads_path)
