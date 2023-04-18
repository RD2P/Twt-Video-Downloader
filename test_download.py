import requests
import os

# the URL of the video file to download
url = "https://video.twimg.com/ext_tw_video/1634699563339481088/pu/vid/320x568/-PC_YGvHSSa6U2od.mp4?tag=12"

current_dir = os.getcwd()
file_path = os.path.join(current_dir, "video.mp4")


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