import unittest
from monitor import vitals_ok, vitals_status


class MonitorTest(unittest.TestCase):
    def test_not_ok_when_any_vital_out_of_range(self):
        # Pulse too high, SpO2 too low
        self.assertFalse(vitals_ok(99, 102, 70))
        # All within normal range
        self.assertTrue(vitals_ok(98.1, 70, 98))

    def test_vitals_status_report(self):
        # Case: pulse too high
        status = vitals_status(98.1, 120, 96)
        self.assertEqual(status["pulse_rate"], "HIGH")
        self.assertEqual(status["temperature"], "OK")
        self.assertEqual(status["spo2"], "OK")

        # Case: temperature too low
        status = vitals_status(90, 80, 96)
        self.assertEqual(status["temperature"], "LOW")

        # Case: oxygen too low
        status = vitals_status(98.1, 80, 85)
        self.assertEqual(status["spo2"], "LOW")


if __name__ == '__main__':
    unittest.main()
