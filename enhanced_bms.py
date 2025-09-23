from monitor_enhanced import evaluate_vitals

scenarios = [
    {"temperature_f": 98, "pulse_bpm": 70, "spo2_pct": 95},
    {"temperature_f": 100.5, "pulse_bpm": 99, "spo2_pct": 92},
    {"temperature_f": 103, "pulse_bpm": 50, "spo2_pct": 85},
]

for s in scenarios:
    print("Input:", s)
    result = evaluate_vitals(s, lang="en")
    print("Result:", result)
    print("-" * 40)
