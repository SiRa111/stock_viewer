

import os
from PIL import Image

# Assuming the script and myfile.gif are in the same directory
file_path ="C:\\Users\\Administrator\\Downloads\\costume1.gif"

# Constructing the absolute path
full_path = os.path.join(os.getcwd(), file_path)

if os.path.exists(full_path):
    try:
        img = Image.open(full_path)
        # Do something with img
        print("Image loaded successfully.")
    except IOError as e:
        print(f"Error opening image: {e}")
else:
    print(f"File not found: {full_path}")
