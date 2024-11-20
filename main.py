import pyautogui
import time
import ctypes

# Function to get the current foreground window title
def get_foreground_window_title():
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
    buff = ctypes.create_unicode_buffer(length + 1)
    ctypes.windll.user32.GetWindowTextW(hwnd, buff, length + 1)
    return buff.value

# Main function to lock the mouse if it touches the screen edges
def lock_mouse_if_at_edge():
    # Get screen resolution
    screen_width, screen_height = pyautogui.size()
    edge_threshold = 5  # Define how close to the edge triggers recentering
    center_x, center_y = screen_width // 2, screen_height // 2

    print("Press Ctrl+C to exit.")
    try:
        while True:
            # Check if Minecraft Bedrock is the active window
            active_window_title = get_foreground_window_title()
            if "Minecraft" in active_window_title:
                # Get the current mouse position
                mouse_x, mouse_y = pyautogui.position()

                # Check if the mouse is at the screen edge
                if (mouse_x <= edge_threshold or
                    mouse_x >= screen_width - edge_threshold or
                    mouse_y <= edge_threshold or
                    mouse_y >= screen_height - edge_threshold):
                    # Recenter the mouse
                    pyautogui.moveTo(center_x, center_y)

            time.sleep(0.01)  # Adjust as necessary to reduce CPU usage
    except KeyboardInterrupt:
        print("\nExiting...")
        pass

if __name__ == "__main__":
    lock_mouse_if_at_edge()
