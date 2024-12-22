import os
import time
import math
from pynput import keyboard
from PIL import Image
from time import sleep

# Directory to save screenshots
screenshot_directory = "screenshots"
if not os.path.exists(screenshot_directory):
    os.makedirs(screenshot_directory)

# Function to take a screenshot using ADB and save it as a PNG image
def take_screenshot():
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_path = f"{screenshot_directory}/screenshot_{timestamp}.png"

    # Use ADB to take a screenshot of the phone and pull it to the Mac
    os.system(f"adb shell screencap -p /sdcard/screenshot.png")
    os.system(f"adb pull /sdcard/screenshot.png {screenshot_path}")
    
    # Open the screenshot and display it
    try:
        image = Image.open(screenshot_path)
        image.show()
        print(f"Screenshot saved at: {screenshot_path}")
    except Exception as e:
        print(f"Failed to display the image: {e}")

def swipe(dimension, duration=20):
    print(f"SWIPING {dimension}")
    output = os.popen("adb shell wm size").read()
    width, height = map(int, output.split()[-1].split('x'))
    cx, cy = width // 2, height // 2
    radius = width // 3  # Distance from the center to the end point
    
    angles = [270, 90, 150, 330, 30, 210]  # List of angles (in degrees) for the 6 directions
    # angles = [0, 60, 120, 180, 240, 300]
    angle = math.radians(angles[dimension])  # Convert the angle to radians
    
    endX = int(cx + radius * math.cos(angle))  # Calculate the endX using cos
    endY = int(cy + radius * math.sin(angle))  # Calculate the endY using sin
        
    # os.system(f"adb shell input tab {endX} {endY}")
    os.system(f"adb shell input swipe {cx} {cy} {endX} {endY} {duration}")
  

# SOLUTION FOR LEVEL 19      
swipes = [2, 4, 3, 0, 2, 4, 1, 2, 0, 3, 5, 2, 1, 3, 1, 3, 1]

for dim in swipes:
  swipe(dim)
  sleep(2.5)

# take_screenshot()