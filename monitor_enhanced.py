# monitor_enhanced.py
from typing import Dict, Any


# ---------------------------
# 1. Vital Thresholds (Data-driven)
# ---------------------------
VITAL_THRESHOLDS = {
    "temperature_f": {
        "normal": (97.0, 99.0),
        "warning_low": (95.0, 96.53),
        "warning_high": (100.47, 102.0),
        "critical_low": (0, 95.0),
        "critical_high": (102.0, float("inf")),
    },
    "pulse_bpm": {
        "normal": (62, 98),
        "warning_low": (60, 61.5),
        "warning_high": (98.5, 100),
        "critical_low": (0, 60),
        "critical_high": (100, float("inf")),
    },
    "spo2_pct": {
        "normal": (92, 98),
        "warning_low": (90, 91.5),
        "warning_high": (98.5, 100),
        "critical_low": (0, 90),
        "critical_high": (100, float("inf")),
    },
}


# ---------------------------
# 2. Multi-language messages
# ---------------------------
MESSAGES = {
    "en": {
        "normal": "Normal",
        "warning_low": "Near Low",
        "warning_high": "Near High",
        "critical_low": "Critical Low",
        "critical_high": "Critical High",
    },
    "de": {
        "normal": "Normal",
        "warning_low": "Nahe Niedrig",
        "warning_high": "Nahe Hoch",
        "critical_low": "Kritisch Niedrig",
        "critical_high": "Kritisch Hoch",
    },
}


# ---------------------------
# 3. Unit Conversion
# ---------------------------
def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32


def translate_to_common_units(vitals: Dict[str, Any]) -> Dict[str, float]:
    """Translate mixed unit input into Fahrenheit / bpm / %"""
    result = {}
    if "temperature_c" in vitals:
        result["temperature_f"] = celsius_to_fahrenheit(vitals["temperature_c"])
    if "temperature_f" in vitals:
        result["temperature_f"] = vitals["temperature_f"]

    if "pulse_bpm" in vitals:
        result["pulse_bpm"] = vitals["pulse_bpm"]

    if "spo2_pct" in vitals:
        result["spo2_pct"] = vitals["spo2_pct"]

    return result


# ---------------------------
# 4. Mapping values to conditions
# ---------------------------
def map_value_to_condition(param: str, value: float) -> str:
    """Check the thresholds and return the condition keyword"""
    ranges = VITAL_THRESHOLDS[param]
    for cond, (low, high) in ranges.items():
        if low <= value <= high:
            return cond
    return "unknown"


def get_condition_message(condition: str, lang: str = "en") -> str:
    return MESSAGES[lang].get(condition, "Unknown")


# ---------------------------
# 5. Overall inference
# ---------------------------
def infer_overall_vitals(conditions: Dict[str, str]) -> str:
    """Infer overall status: Critical > Warning > Normal"""
    if any(c.startswith("critical") for c in conditions.values()):
        return "Critical"
    if any(c.startswith("warning") for c in conditions.values()):
        return "Warning"
    return "Normal"


# ---------------------------
# 6. Main pipeline
# ---------------------------
def evaluate_vitals(vitals: Dict[str, Any], lang: str = "en") -> Dict[str, Any]:
    # Step 1: Convert to common units
    standardized = translate_to_common_units(vitals)

    # Step 2: Map each vital to a condition
    conditions = {
        k: map_value_to_condition(k, v) for k, v in standardized.items()
    }

    # Step 3: Translate condition to messages
    messages = {k: get_condition_message(c, lang) for k, c in conditions.items()}

    # Step 4: Infer overall
    overall = infer_overall_vitals(conditions)

    return {
        "standardized": standardized,
        "conditions": conditions,
        "messages": messages,
        "overall": overall,
    }
