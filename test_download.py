'''
Testing video download
'''


import requests
import os

# Hardcoded URL of the video file to download
url = "https://twitter.com/BestMoment_Vids/status/1712467861942513719"

current_dir = os.getcwd()
file_path = os.path.join(current_dir, "Downloads", "video.mp4")


# send GET request to URL
response = requests.get(url)

# check if request was successful
if response.status_code == 200:
    # request successful, save video file
    # wb is "write binary" mode, to write binary data to file
    with open(file_path, "wb") as f:
        f.write(response.content)
    print("Video downloaded successfully!")
else:
    # request failed, print the error message
    print(f"Error downloading video: {response.status_code} {response.reason}")