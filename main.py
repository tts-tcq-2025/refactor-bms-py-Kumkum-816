from monitor import VitalsMonitor
from alerts import AlertSystem

def main():
    alert_system = AlertSystem()
    monitor = VitalsMonitor(alert_system)

    # Example vitals data (could come from sensors later)
    test_data = [
        (98.6, 72, 99),   # Normal
        (103, 75, 97),    # High temperature
        (98.1, 120, 96),  # High pulse rate
        (97, 80, 85)      # Low SpO2
    ]

    for temp, pulse, spo2 in test_data:
        print(f"\nChecking vitals: Temp={temp}, Pulse={pulse}, SpO2={spo2}")
        ok = monitor.vitals_ok(temp, pulse, spo2)
        print("Vitals OK ✅" if ok else "Vitals NOT OK ❌")

if __name__ == "__main__":
    main()
