from alerts import AlertSystem


class VitalsMonitor:
    def __init__(self, alert_system: AlertSystem, tolerance: float = 0.015):
        self.alert_system = alert_system
        self.tolerance = tolerance

        # Define safe ranges for vitals (min, max, severity)
        self.vital_ranges = {
            "temperature": {"min": 95, "max": 102, "severity": "HIGH"},
            "pulse_rate": {"min": 60, "max": 100, "severity": "MEDIUM"},
            "spo2": {"min": 90, "max": 100, "severity": "HIGH"},
        }

    def _check_vital(self, name, value):
        """Check individual vital sign and trigger alert if out of range."""
        v = self.vital_ranges[name]
        min_val, max_val, severity = v["min"], v["max"], v["severity"]

        # Early warning range with tolerance
        warn_min = min_val * (1 + self.tolerance) if name != "spo2" else min_val * (1 + self.tolerance)
        warn_max = max_val * (1 - self.tolerance)

        if value < min_val or value > max_val:
            self.alert_system.alert(f"{name.capitalize()} CRITICAL! Value={value}", severity=severity)
            return False
        elif value < warn_min or value > warn_max:
            self.alert_system.alert(f"{name.capitalize()} WARNING! Approaching limit. Value={value}", severity="LOW")
            # Still considered OK but near threshold
        return True

    def vitals_ok(self, temperature, pulse_rate, spo2):
        """Check all vitals."""
        results = [
            self._check_vital("temperature", temperature),
            self._check_vital("pulse_rate", pulse_rate),
            self._check_vital("spo2", spo2),
        ]
        return all(results)
