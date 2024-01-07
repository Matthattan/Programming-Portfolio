import keyboard
import time
import threading

autoclicker_running = False

def autoclicker():
    global autoclicker_running
    try:
        fixed_bar_capacity = 8350
        bar_depletion_per_r = 7
        bar_recharge_rate_per_second = 200

        while autoclicker_running:
            # Perform your autoclicking action here
            # For demonstration purposes, we'll just print a message
            total_r_press_time = (fixed_bar_capacity / bar_depletion_per_r) * 1.0

            # Deplete the fixed bar by pressing 'r'
            total_delay = 0.1  # Shorter delay for each 'r' press
            iterations = int(total_r_press_time / total_delay)
            for _ in range(iterations):
                keyboard.press('r')
                time.sleep(total_delay)
                keyboard.release('r')

            # Calculate the time needed to recharge the fixed bar while holding down 'c'
            recharge_time = (fixed_bar_capacity / bar_recharge_rate_per_second) * 1.0

            # Hold down 'c' for the calculated recharge time
            keyboard.press('c')
            time.sleep(recharge_time)
            keyboard.release('c')

    except KeyboardInterrupt:
        print("Autoclicker terminated.")

def start_autoclicker():
    global autoclicker_running
    if not autoclicker_running:
        autoclicker_running = True
        print("Autoclicker started.")
        threading.Thread(target=autoclicker).start()

def stop_autoclicker():
    global autoclicker_running
    autoclicker_running = False
    print("Autoclicker stopped.")

if __name__ == "__main__":
    keyboard.add_hotkey('l', start_autoclicker)
    keyboard.add_hotkey('k', stop_autoclicker)

    try:
        keyboard.wait('esc')  # Wait for the 'esc' key to exit the program
    except KeyboardInterrupt:
        pass
