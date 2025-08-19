import sys
import time

def blink_text(message, times=3):
    """Blink text in the console to simulate alarm."""
    for _ in range(times):
        print(f"\r⚠️ {message} ", end="")
        sys.stdout.flush()
        time.sleep(0.5)
        print("\r" + " " * len(message), end="")
        sys.stdout.flush()
        time.sleep(0.5)
    print()  # move cursor to new line
