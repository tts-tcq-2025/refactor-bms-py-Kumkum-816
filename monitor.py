# monitor.py
from time import sleep
import sys


def alarm(message: str):
    """Display blinking alarm with message."""
    print(message)
    for _ in range(6):
        print('\r* ', end='')
        sys.stdout.flush()
        sleep(1)
        print('\r *', end='')
        sys.stdout.flush()
        sleep(1)


def vitals_ok(temperature: float, pulseRate: float, spo2: float) -> bool:
    """
    Checks the vitals and prints alarms or warnings.
    Returns False if any critical limit is breached, True otherwise.
    """
    # Temperature checks
    if temperature < 95:
        alarm('Temperature critical! Hypothermia risk.')
        return False
    elif 95 <= temperature <= 95 + (102 * 0.015):
        print('Warning: Approaching hypothermia')
    elif temperature > 102:
        alarm('Temperature critical! Hyperthermia risk.')
        return False
    elif 102 - (102 * 0.015) <= temperature <= 102:
        print('Warning: Approaching hyperthermia')

    # Pulse checks
    if pulseRate < 60:
        alarm('Pulse Rate critical! Too low.')
        return False
    elif 60 <= pulseRate <= 60 + (100 * 0.015):
        print('Warning: Approaching bradycardia')
    elif pulseRate > 100:
        alarm('Pulse Rate critical! Too high.')
        return False
    elif 100 - (100 * 0.015) <= pulseRate <= 100:
        print('Warning: Approaching tachycardia')

    # SPO2 checks
    if spo2 < 90:
        alarm('Oxygen Saturation critical! Hypoxemia risk.')
        return False
    elif 90 <= spo2 <= 90 + (90 * 0.015):
        print('Warning: Approaching low oxygen saturation')

    return True
