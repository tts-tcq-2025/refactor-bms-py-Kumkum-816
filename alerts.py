import sys
import time
from utils import blink_text


class AlertSystem:
    def __init__(self, use_console=True, log_file=None, language="EN"):
        self.use_console = use_console
        self.log_file = log_file
        self.language = language

        # Messages can be translated easily
        self.translations = {
            "EN": {
                "CRITICAL": "CRITICAL CONDITION!",
                "WARNING": "Warning - approaching unsafe range",
                "OK": "Vitals are normal",
            },
            "DE": {  # German support
                "CRITICAL": "KRITISCHER ZUSTAND!",
                "WARNING": "Warnung - Bereich unsicher",
                "OK": "Vitalwerte sind normal",
            },
        }

    def _translate(self, key: str) -> str:
        """Translate based on chosen language."""
        return self.translations.get(self.language, {}).get(key, key)

    def alert(self, message: str, severity: str = "LOW"):
        """Send an alert (console, log file, etc.)."""
        translated_severity = self._translate(severity.upper()) if severity else severity
        final_message = f"[ALERT - {severity}] {message} | {translated_severity}"

        if self.use_console:
            print(final_message)
            blink_text(message, times=2)

        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(final_message + "\n")

