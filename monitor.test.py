# monitor_test.py
import unittest
from monitor import vitals_ok


class MonitorTest(unittest.TestCase):
    def test_not_ok_when_any_vital_out_of_range(self):
        # Pulse too high
        self.assertFalse(vitals_ok(99, 102, 95))
        # Oxygen too low
        self.assertFalse(vitals_ok(98.1, 70, 70))

    def test_ok_when_all_vitals_in_normal_range(self):
        self.assertTrue(vitals_ok(98.1, 70, 98))

    def test_warning_when_temperature_near_low(self):
        # 95.5 is within warning range
        self.assertTrue(vitals_ok(95.5, 70, 95))

    def test_warning_when_temperature_near_high(self):
        # 101 is within warning range
        self.assertTrue(vitals_ok(101, 70, 95))

    def test_warning_when_pulse_near_low(self):
        self.assertTrue(vitals_ok(60.5, 70, 95))

    def test_warning_when_pulse_near_high(self):
        self.assertTrue(vitals_ok(99, 70, 95))

    def test_warning_when_spo2_near_low(self):
        self.assertTrue(vitals_ok(98.1, 70, 90.5))


if __name__ == '__main__':
    unittest.main()
