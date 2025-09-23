from alerts import AlertSystem
from monitor import VitalsMonitor


def main():
    # Initialize the alert system (console for now, can extend later to email/SMS)
    alert_system = AlertSystem(use_console=True)

    # Initialize vitals monitor with the alert system
    monitor = VitalsMonitor(alert_system)

    # Example patient vitals for testing
    test_vitals = [
        {"temperature": 98.6, "pulse_rate": 72, "spo2": 97},   # ✅ Normal
        {"temperature": 103.0, "pulse_rate": 80, "spo2": 95},  # ❌ High temperature
        {"temperature": 97.0, "pulse_rate": 120, "spo2": 96},  # ❌ High pulse
        {"temperature": 94.0, "pulse_rate": 65, "spo2": 89},   # ❌ Low temp + Low SpO2
    ]

    for i, vitals in enumerate(test_vitals, start=1):
        print(f"\n--- Checking patient {i} ---")
        status = monitor.vitals_ok(
            vitals["temperature"], vitals["pulse_rate"], vitals["spo2"]
        )
        print("Vitals OK:", status)


if __name__ == "__main__":
    main()
