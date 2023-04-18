import os

downloads_path = os.path.expanduser("~/Downloads")

# Check if the Downloads folder exists
if os.path.isdir(downloads_path):
    # Open the Downloads folder
    os.startfile(downloads_path)
else:
    print("Downloads folder not found.")
