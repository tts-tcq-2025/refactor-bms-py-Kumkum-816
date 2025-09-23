import unittest
from monitor_enhanced import evaluate_vitals


class TestEnhancedMonitor(unittest.TestCase):
    def test_normal_range(self):
        result = evaluate_vitals({"temperature_f": 98, "pulse_bpm": 70, "spo2_pct": 95})
        self.assertEqual(result["overall"], "Normal")

    def test_warning_range(self):
        result = evaluate_vitals({"temperature_f": 100.5, "pulse_bpm": 99, "spo2_pct": 92})
        self.assertEqual(result["overall"], "Warning")

    def test_critical_range(self):
        result = evaluate_vitals({"temperature_f": 103, "pulse_bpm": 50, "spo2_pct": 85})
        self.assertEqual(result["overall"], "Critical")

    def test_unit_conversion(self):
        result = evaluate_vitals({"temperature_c": 37, "pulse_bpm": 70, "spo2_pct": 96})
        self.assertAlmostEqual(result["standardized"]["temperature_f"], 98.6, places=1)

    def test_multi_language(self):
        result = evaluate_vitals({"temperature_f": 103}, lang="de")
        self.assertEqual(result["messages"]["temperature_f"], "Kritisch Hoch")
