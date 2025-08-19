from time import sleep
import sys

# Constants for thresholds
TEMP_MIN = 95.0
TEMP_MAX = 102.0
PULSE_MIN = 60
PULSE_MAX = 100
SPO2_MIN = 90


def blink_alert(message: str, times: int = 6, delay: float = 1.0):
    """Show a blinking alert with the given message."""
    print(message)
    for _ in range(times):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(delay)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(delay)
    print()  # new line after blinking


def vitals_ok(temperature: float, pulse_rate: int, spo2: int) -> bool:
    """
    Check if vitals are within safe range.
    Returns True if all are okay, False otherwise.
    """
    if temperature > TEMP_MAX or temperature < TEMP_MIN:
        blink_alert(f"Temperature critical! (Current: {temperature}°F)")
        return False

    if pulse_rate < PULSE_MIN or pulse_rate > PULSE_MAX:
        blink_alert(f"Pulse Rate out of range! (Current: {pulse_rate} bpm)")
        return False

    if spo2 < SPO2_MIN:
        blink_alert(f"Oxygen Saturation too low! (Current: {spo2}%)")
        return False

    print("All vitals are within normal range ✅")
    return True


def vitals_status(temperature: float, pulse_rate: int, spo2: int) -> dict:
    """
    Return a detailed status report of all vitals.
    Example:
    {
      "temperature": "OK",
      "pulse_rate": "HIGH",
      "spo2": "OK"
    }
    """
    status = {}

    status["temperature"] = (
        "LOW" if temperature < TEMP_MIN else
        "HIGH" if temperature > TEMP_MAX else "OK"
    )

    status["pulse_rate"] = (
        "LOW" if pulse_rate < PULSE_MIN else
        "HIGH" if pulse_rate > PULSE_MAX else "OK"
    )

    status["spo2"] = "LOW" if spo2 < SPO2_MIN else "OK"

    return status
