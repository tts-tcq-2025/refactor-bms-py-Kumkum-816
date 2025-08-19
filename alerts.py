import sys
import time
from utils import blink_text

class AlertSystem:
    def __init__(self, use_console=True):
        self.use_console = use_console

    def alert(self, message: str, severity: str = "LOW"):
        """Send an alert (console for now, can extend to email/SMS)."""
        if self.use_console:
            print(f"[ALERT - {severity}] {message}")
            blink_text(message, times=3)
