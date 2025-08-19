from alerts import AlertSystem

class VitalsMonitor:
    def __init__(self, alert_system: AlertSystem):
        self.alert_system = alert_system

    def vitals_ok(self, temperature, pulse_rate, spo2):
        """Check vitals and trigger alerts if out of range."""
        if temperature > 102 or temperature < 95:
            self.alert_system.alert("Temperature critical!", severity="HIGH")
            return False
        elif pulse_rate < 60 or pulse_rate > 100:
            self.alert_system.alert("Pulse Rate is out of range!", severity="MEDIUM")
            return False
        elif spo2 < 90:
            self.alert_system.alert("Oxygen Saturation out of range!", severity="HIGH")
            return False
        return True
