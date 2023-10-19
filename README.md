# Twt-Video-Downloader

This is a Python project that uses Selenium to request to download videos from Twitter using a third party video downloader.

## Requirements
* Python 3.x
* Selenium
* MS Edge webdriver
* Requests
* tkinter

## Installation and Use
1. Download [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/), ensure the version matches your browser. Also take note of the location where you saved the msedgewebdriver.exe

2. Download the project files as zip or clone the repository:
    ```shell
    git clone https://github.com/RD2P/Twt-Video-Downloader.git
3. Navigate to the project directory:
    ```shell
    cd Twt-Video-Downloader
4. Go into script.py and change the webdriver path in line 18 to the one in your machine
    ```py
    browser = webdriver.Edge("<<Location of your driver here>>\msedgedriver.exe")
5. Run script.py
    ```shell
    python script.py
## Behaviour
Upon running the script, a pop-up window will appear asking for the Twitter link of the video to download. Once the link is entered, the script will automate the process of navigating to a video downloader website, inputting the link, and clicking the download button. After the video has been downloaded, it will be saved in the project's "Downloads" folder and the folder will open automatically.
Note: Web pages involved change over time, so this script may not work the same way 🙂