from PIL import Image

try:
    img = Image.open("C:\\Users\\Administrator\\Downloads\\costume1.gif")
    # Do something with img
except IOError as e:
    print("Error opening image:", e)
