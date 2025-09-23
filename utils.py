import sys
import time


def blink_text(message, times=3, interval=0.5, enable=True, symbol="⚠️"):
    """
    Blink text in the console to simulate an alarm.

    Args:
        message (str): The message to blink.
        times (int): How many times to blink.
        interval (float): Time in seconds between blinks.
        enable (bool): Disable blinking if False (useful for logs/production).
        symbol (str): Prefix symbol (⚠️, ❌, ✅, etc.).
    """
    if not enable:
        print(f"{symbol} {message}")
        return

    for _ in range(times):
        # Show message
        print(f"\r{symbol} {message}", end="")
        sys.stdout.flush()
        time.sleep(interval)

        # Clear message
        print("\r" + " " * (len(message) + len(symbol) + 1), end="")
        sys.stdout.flush()
        time.sleep(interval)

    print()  # Move cursor to a new line at the end

