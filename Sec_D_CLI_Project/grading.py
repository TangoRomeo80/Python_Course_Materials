"""
This module will contain all the grading related functionalities
"""
from __future__ import annotations

def compute_total_and_percentage(marks: list[float]) -> tuple[float, float]:
    # total = sum(marks)
    total = 0.0
    for m in marks:
        total += m
    percentage = total / len(marks)
    return total, percentage

def grade_from_percentage(pct: float) -> str:
    if pct >= 90.0:
        return "A"
    elif pct >= 80.0:
        return "B"
    elif pct >= 70.0:
        return "C"
    elif pct >= 60.0:
        return "D"
    else:
        return "F"
