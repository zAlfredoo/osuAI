import sys
import numpy as np
import pyautogui
import win32gui
from time import sleep

def get_window_handle(window_name):
    """Get the handle of a window by its name."""
    return win32gui.FindWindow(None, window_name)

def capture_window_screenshot(window_name):
    """Capture a screenshot of a window by its name."""
    # Get the handle of the window
    hwnd = get_window_handle(window_name)
    print(hwnd)

    # Bring the window to the front
    win32gui.SetForegroundWindow(hwnd)

    # Get the dimensions of the window
    rect = win32gui.GetWindowRect(hwnd)

    # Capture a screenshot of the window
    screenshot = pyautogui.screenshot(region=rect)

    return screenshot


if __name__ == '__main__':
    name = 'osu!cuttingedge b20230101'
    sc = capture_window_screenshot(name)
    sc = np.array(sc)
    print(sc)
    print("hiii")

