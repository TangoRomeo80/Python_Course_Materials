"""
This module contains functions to compute total marks, percentage, grade, and pass/fail status
"""

from __future__ import annotations

def compute_total_and_percentage(marks: list[float]) -> tuple[float, float]:
    total = 0.0
    for m in marks:
        total += m
    percentage = total / len(marks)
    return total, percentage

def grade_from_percentage(pct: float) -> str:
    if pct >= 90:
        return "A+"
    elif pct >= 85:
        return "A"
    elif pct >= 80:
        return "B+"
    elif pct >= 75:
        return "B"
    elif pct >= 70:
        return "C+"
    elif pct >= 65:
        return "C"
    elif pct >= 60:
        return "D+"
    elif pct >= 50:
        return "D"
    else:
        return "F"
    
def status_from_percentage(pct: float) -> str:
    return "Pass" if pct >= 50 else "Fail"