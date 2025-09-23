import unittest
from monitor import VitalsMonitor
from alerts import AlertSystem

class MockAlertSystem(AlertSystem):
    def __init__(self):
        super().__init__(use_console=False)
        self.messages = []

    def alert(self, message, severity="LOW"):
        self.messages.append((message, severity))

class MonitorTest(unittest.TestCase):
    def setUp(self):
        self.mock_alert = MockAlertSystem()
        self.monitor = VitalsMonitor(self.mock_alert)

    def test_temperature_out_of_range(self):
        result = self.monitor.vitals_ok(103, 80, 98)
        self.assertFalse(result)
        self.assertIn(("Temperature critical!", "HIGH"), self.mock_alert.messages)

    def test_normal_vitals(self):
        result = self.monitor.vitals_ok(98.6, 75, 98)
        self.assertTrue(result)
        self.assertEqual(len(self.mock_alert.messages), 0)

if __name__ == "__main__":
    unittest.main()
